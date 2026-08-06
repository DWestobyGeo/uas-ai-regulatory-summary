import csv, json, glob, os, shutil, datetime, subprocess

try:
    import yaml
except ImportError:
    yaml = None

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_ROOT = os.path.join(SCRIPT_DIR, "States")
OUT_ROOT = os.path.join(SCRIPT_DIR, "docs")
DATA_DIR = os.path.join(OUT_ROOT, "data", "v1")
SOURCES_DIR = os.path.join(DATA_DIR, "sources")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(SOURCES_DIR, exist_ok=True)

state_dirs = sorted([d for d in glob.glob(os.path.join(SRC_ROOT, "*")) if os.path.isdir(d)])

def get_last_updated(script_dir, csv_path, state_dir):
    """Return the most defensible "last updated" date for a state's data.

    Preference order:
      1. The state's research manifest's `last_currency_check` (Workstream 2), if present --
         this is an explicit, human/agent-verified "we confirmed this is still current" date,
         not a filesystem artifact.
      2. The date of the most recent git commit that actually changed the source register CSV
         -- stable across a fresh clone/checkout (unlike filesystem mtime, which is reset by
         checkout regardless of whether content changed).
      3. Filesystem mtime, only as a last resort if this isn't a git checkout at all (e.g. a
         zip download) or git is unavailable.
    """
    if yaml is not None:
        manifest_files = glob.glob(os.path.join(state_dir, "*_UAS_Research_Manifest.yaml"))
        if manifest_files:
            try:
                with open(manifest_files[0], encoding="utf-8") as mf:
                    manifest = yaml.safe_load(mf) or {}
                check_date = manifest.get("last_currency_check")
                if check_date:
                    return str(check_date)
            except (OSError, yaml.YAMLError):
                pass

    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%ad", "--date=short", "--", csv_path],
            cwd=script_dir, capture_output=True, text=True, timeout=10,
        )
        date_str = result.stdout.strip()
        if result.returncode == 0 and date_str:
            return date_str
    except (OSError, subprocess.SubprocessError):
        pass

    mtime = os.path.getmtime(csv_path)
    return datetime.date.fromtimestamp(mtime).isoformat()


def load_news(state_dir, folder_name):
    """Workstream: news-aggregator role support (see agents/roles/news-aggregator.md).

    Reads an optional, purely additive `*_UAS_News.yaml` file and returns a dict of
    record_id -> list of news-item dicts, to be merged onto matching source-register
    records by the caller. This intentionally does NOT touch the 33-field CSV schema
    or scripts/validate_phase2.py's EXPECTED column list -- the news file is a
    separate, optional artifact, and a state with no news file (the overwhelming
    majority, by design -- most authorities will never have genuinely on-topic,
    verified news) simply contributes no `news` key to any of its records.

    Each item is expected to provide: record_id, headline, url, source_name,
    publish_date, jurisdiction_match ("in_state" or "out_of_state"),
    out_of_state_name (only when jurisdiction_match == "out_of_state"),
    relevance_note, and date_accessed. Malformed items (missing record_id,
    headline, or an invalid jurisdiction_match) are skipped with a warning rather
    than silently guessed at or included -- precision over recall, per the role's
    own governing instructions.
    """
    news_by_id = {}
    if yaml is None:
        return news_by_id
    news_files = glob.glob(os.path.join(state_dir, "*_UAS_News.yaml"))
    if not news_files:
        return news_by_id
    try:
        with open(news_files[0], encoding="utf-8") as nf:
            doc = yaml.safe_load(nf) or {}
    except (OSError, yaml.YAMLError) as exc:
        print(f"WARN ({folder_name}): could not parse {news_files[0]}: {exc}")
        return news_by_id

    for item in doc.get("items", []) or []:
        record_id = (item.get("record_id") or "").strip()
        headline = (item.get("headline") or "").strip()
        jurisdiction_match = (item.get("jurisdiction_match") or "").strip()
        if not record_id or not headline:
            print(f"WARN ({folder_name}): skipping news item missing record_id or headline: {item!r}")
            continue
        if jurisdiction_match not in ("in_state", "out_of_state"):
            print(f"WARN ({folder_name}): skipping news item {record_id!r} with invalid jurisdiction_match {jurisdiction_match!r}")
            continue
        news_by_id.setdefault(record_id, []).append({
            "record_id": record_id,
            "headline": headline,
            "url": item.get("url"),
            "source_name": item.get("source_name"),
            "publish_date": item.get("publish_date"),
            "jurisdiction_match": jurisdiction_match,
            "out_of_state_name": item.get("out_of_state_name"),
            "relevance_note": item.get("relevance_note"),
            "date_accessed": item.get("date_accessed"),
        })
    return news_by_id


def get_research_status(state_dir):
    """Workstream 9 (retrofit visibility): report a state's research_status per the controlled
    vocabulary in States/RESEARCH_MANIFEST_SCHEMA.md, so the live site can visibly distinguish a
    "current method" (Phase B pilot) state from a "legacy, not yet retrofitted" one -- a Definition
    of Done acceptance criterion ("legacy and current-method status is visible").

    A state with a research manifest reports whatever research_status the manifest declares.
    A state without one has not been through the current-method process at all yet (manifests
    are piloted for five states only as of this writing -- see evals/pilot_states.md), so it is
    reported as legacy_needs_retrofit -- not an error, just the honest state of the nationwide
    rollout. See planning/national_retrofit_queue.md for the risk-ordered plan to work through it.
    """
    if yaml is not None:
        manifest_files = glob.glob(os.path.join(state_dir, "*_UAS_Research_Manifest.yaml"))
        if manifest_files:
            try:
                with open(manifest_files[0], encoding="utf-8") as mf:
                    manifest = yaml.safe_load(mf) or {}
                status = manifest.get("research_status")
                if status:
                    return str(status)
            except (OSError, yaml.YAMLError):
                pass
    return "legacy_needs_retrofit"


index = {
    "schema_version": "1.1",
    "generated_at": datetime.date.today().isoformat(),
    "disclaimer": "AI-compiled regulatory research. Not legal advice. See /DISCLAIMER for full terms.",
    "states": []
}

for sd in state_dirs:
    folder_name = os.path.basename(sd)  # e.g. TX_Texas
    csv_files = glob.glob(os.path.join(sd, "*_UAS_Source_Register.csv"))
    md_files = glob.glob(os.path.join(sd, "*_UAS_Regulatory_Summary.md"))
    if not csv_files or not md_files:
        print("SKIP (missing files):", folder_name)
        continue
    csv_path = csv_files[0]
    md_path = md_files[0]

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        records = list(reader)

    if not records:
        print("SKIP (empty csv):", folder_name)
        continue

    abbr = records[0]["state_abbr"].strip()
    name = records[0]["state"].strip()
    fips = records[0]["state_fips"].strip()

    with open(md_path, encoding="utf-8") as f:
        summary_md = f.read()

    last_updated = get_last_updated(SCRIPT_DIR, csv_path, sd)
    research_status = get_research_status(sd)

    news_by_id = load_news(sd, folder_name)
    news_record_count = 0
    if news_by_id:
        for rec in records:
            matched = news_by_id.get(rec.get("record_id", ""))
            if matched:
                rec["news"] = matched
                news_record_count += len(matched)

    state_obj = {
        "schema_version": "1.1",
        "state": name,
        "state_abbr": abbr,
        "state_fips": fips,
        "last_updated": last_updated,
        "research_status": research_status,
        "record_count": len(records),
        "summary_markdown": summary_md,
        "records": records,
        "source_files": {
            "summary_markdown": f"data/v1/sources/{folder_name}/{os.path.basename(md_path)}",
            "source_register_csv": f"data/v1/sources/{folder_name}/{os.path.basename(csv_path)}"
        },
        "disclaimer": "AI-compiled regulatory research. Not legal advice. Verify all citations against official sources before relying on this record. See /DISCLAIMER for full terms."
    }

    out_path = os.path.join(DATA_DIR, f"{abbr}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(state_obj, f, indent=2, ensure_ascii=False)

    # copy raw source files for download/transparency
    dest_folder = os.path.join(SOURCES_DIR, folder_name)
    os.makedirs(dest_folder, exist_ok=True)
    shutil.copy(csv_path, dest_folder)
    shutil.copy(md_path, dest_folder)

    index["states"].append({
        "state": name,
        "state_abbr": abbr,
        "state_fips": fips,
        "record_count": len(records),
        "last_updated": last_updated,
        "json_url": f"data/v1/{abbr}.json"
    })

    print("Built:", abbr, name, "records:", len(records), (f"news items: {news_record_count}" if news_record_count else ""))

index["states"].sort(key=lambda s: s["state_abbr"])
index["state_count"] = len(index["states"])

with open(os.path.join(DATA_DIR, "index.json"), "w", encoding="utf-8") as f:
    json.dump(index, f, indent=2, ensure_ascii=False)

print("\nTotal states indexed:", len(index["states"]))
