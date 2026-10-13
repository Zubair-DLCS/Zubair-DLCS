"""Apply descriptions and topics from repos.yml to each GitHub repository.

Run by the "Repo metadata" workflow. Needs a token in REPO_METADATA_TOKEN that can
edit the listed repos (classic token with the `public_repo` scope).

    python scripts/apply_repo_metadata.py repos.yml            # apply
    python scripts/apply_repo_metadata.py repos.yml --dry-run  # print only
"""
from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request

import yaml

API = "https://api.github.com"
TOPIC_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,49}$")


def validate(cfg: dict) -> list[str]:
    errors = []
    for r in cfg.get("repos", []):
        name = r.get("name", "?")
        if not r.get("description"):
            errors.append(f"{name}: missing description")
        elif len(r["description"]) > 350:
            errors.append(f"{name}: description longer than 350 characters")
        topics = r.get("topics", [])
        if len(topics) > 20:
            errors.append(f"{name}: more than 20 topics")
        for t in topics:
            if not TOPIC_RE.match(str(t)):
                errors.append(f"{name}: invalid topic '{t}' (lowercase letters, numbers, hyphens)")
    return errors


def call(method: str, path: str, body: dict, token: str) -> None:
    req = urllib.request.Request(
        API + path, method=method, data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json",
                 "X-GitHub-Api-Version": "2022-11-28", "Content-Type": "application/json"})
    with urllib.request.urlopen(req) as resp:
        resp.read()


def main() -> int:
    path = sys.argv[1] if len(sys.argv) > 1 else "repos.yml"
    dry = "--dry-run" in sys.argv
    cfg = yaml.safe_load(open(path, encoding="utf-8"))
    errors = validate(cfg)
    if errors:
        print("repos.yml has problems:\n  " + "\n  ".join(errors))
        return 1
    owner = cfg["owner"]
    token = os.environ.get("REPO_METADATA_TOKEN", "")
    if not dry and not token:
        print("REPO_METADATA_TOKEN is not set. Add it under Settings -> Secrets and variables -> Actions.")
        return 1

    failed = 0
    for r in cfg["repos"]:
        name, topics = r["name"], [str(t) for t in r.get("topics", [])]
        if dry:
            print(f"[dry-run] {owner}/{name}\n  description: {r['description']}\n  topics: {', '.join(topics)}")
            continue
        try:
            call("PATCH", f"/repos/{owner}/{name}", {"description": r["description"]}, token)
            call("PUT", f"/repos/{owner}/{name}/topics", {"names": topics}, token)
            print(f"updated {owner}/{name}")
        except urllib.error.HTTPError as e:
            failed += 1
            print(f"FAILED {owner}/{name}: HTTP {e.code} {e.read().decode()[:200]}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
