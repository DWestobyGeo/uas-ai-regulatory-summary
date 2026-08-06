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

    state_obj = {
        "schema_version": "1.1",
        "state": name,
        "state_abbr": abbr,
        "state_fips": fips,
        "last_updated": last_updated,
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

    print("Built:", abbr, name, "records:", len(records))

index["states"].sort(key=lambda s: s["state_abbr"])
index["state_count"] = len(index["states"])

with open(os.path.join(DATA_DIR, "index.json"), "w", encoding="utf-8") as f:
    json.dump(index, f, indent=2, ensure_ascii=False)

print("\nTotal states indexed:", len(index["states"]))
