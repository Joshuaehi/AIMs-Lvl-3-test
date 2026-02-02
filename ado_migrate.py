
---

# ✅ `ado_migrate.py`

```python
import os
import base64
import json
import requests
from dotenv import load_dotenv

load_dotenv()

ADO_PAT = os.getenv("ADO_PAT")

ORG_SOURCE = os.getenv("ADO_ORG_SOURCE")
PROJECT_SOURCE = os.getenv("ADO_PROJECT_SOURCE")

ORG_TARGET = os.getenv("ADO_ORG_TARGET")
PROJECT_TARGET = os.getenv("ADO_PROJECT_TARGET")

API_VERSION = "7.1-preview.3"

OUTPUT_DIR = "output"
MAPPING_FILE = os.path.join(OUTPUT_DIR, "migration_map.json")


def auth_header():
    token = f":{ADO_PAT}".encode("utf-8")
    b64 = base64.b64encode(token).decode("utf-8")
    return {
        "Authorization": f"Basic {b64}",
        "Content-Type": "application/json-patch+json"
    }


def get_work_item(org, work_item_id):
    url = (
        f"https://dev.azure.com/{org}/_apis/wit/workitems/{work_item_id}"
        f"?api-version={API_VERSION}&$expand=fields"
    )
    r = requests.get(url, headers=auth_header())
    r.raise_for_status()
    return r.json()


def create_work_item(org, project, work_item_type, fields):
    url = (
        f"https://dev.azure.com/{org}/{project}/_apis/wit/workitems/${work_item_type}"
        f"?api-version={API_VERSION}"
    )

    patch = []
    for k, v in fields.items():
        patch.append({"op": "add", "path": f"/fields/{k}", "value": v})

    r = requests.post(url, headers=auth_header(), data=json.dumps(patch))
    r.raise_for_status()
    return r.json()


def migrate_single_work_item(source_id, target_type="User Story"):
    source = get_work_item(ORG_SOURCE, source_id)
    f = source.get("fields", {})

    new_fields = {
        "System.Title": f.get("System.Title", f"Migrated Item {source_id}"),
        "System.Description": f.get("System.Description", ""),
        "System.Tags": f.get("System.Tags", ""),
    }

    # Optional: Only set these if they exist and match target project paths
    if "System.AreaPath" in f:
        new_fields["System.AreaPath"] = f["System.AreaPath"]
    if "System.IterationPath" in f:
        new_fields["System.IterationPath"] = f["System.IterationPath"]

    created = create_work_item(
        ORG_TARGET,
        PROJECT_TARGET,
        target_type,
        new_fields
    )

    return {
        "source_id": source_id,
        "target_id": created["id"],
        "target_url": created["url"]
    }


def main():
    if not ADO_PAT:
        raise ValueError("Missing ADO_PAT in .env")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # TODO: Replace with your real list of IDs or WIQL query logic
    ids_to_migrate = [101, 102, 103]

    results = []
    for wid in ids_to_migrate:
        try:
            res = migrate_single_work_item(wid, target_type="User Story")
            results.append(res)
            print(f"✅ Migrated {wid} -> {res['target_id']}")
        except Exception as e:
            print(f"❌ Failed {wid}: {e}")

    with open(MAPPING_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print(f"\nDone. Mapping saved to {MAPPING_FILE}")


if __name__ == "__main__":
    main()
