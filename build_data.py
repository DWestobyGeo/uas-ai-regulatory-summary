import csv, json, glob, os, shutil, datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_ROOT = os.path.join(SCRIPT_DIR, "States")
OUT_ROOT = os.path.join(SCRIPT_DIR, "docs")
DATA_DIR = os.path.join(OUT_ROOT, "data", "v1")
SOURCES_DIR = os.path.join(DATA_DIR, "sources")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(SOURCES_DIR, exist_ok=True)

state_dirs = sorted([d for d in glob.glob(os.path.join(SRC_ROOT, "*")) if os.path.isdir(d)])

index = {
    "schema_version": "1.0",
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

    mtime = os.path.getmtime(csv_path)
    last_updated = datetime.date.fromtimestamp(mtime).isoformat()

    state_obj = {
        "schema_version": "1.0",
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
