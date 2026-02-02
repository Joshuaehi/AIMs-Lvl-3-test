# DevOps Migration Tool (Azure DevOps Work Item Migration)

A simple Python tool to migrate Azure DevOps work items from a **source org/project** to a **target org/project** using the Azure DevOps REST API.

---

## ✅ Features

- Migrates work items by ID
- Copies common fields:
  - Title
  - Description
  - Tags
  - Area Path (optional)
  - Iteration Path (optional)
- Creates a `migration_map.json` file for source → target mapping

---

## 📦 Requirements

- Python 3.9+
- Azure DevOps PAT (Personal Access Token)
- PAT permissions:
  - Work Items: Read & Write

---

## 🚀 Setup

### 1) Install dependencies

```bash
pip install -r requirements.txt

