import json
import urllib.request
import urllib.error
from pathlib import Path

URL = "http://127.0.0.1:5000"
LOG = Path("logs/audit.jsonl")


def post(path, body):
    req = urllib.request.Request(
        URL + path,
        data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read() or b"{}")


def appeals_logged(cid):
    n = 0
    for line in LOG.read_text(encoding="utf-8").splitlines():
        if line.strip():
            e = json.loads(line)
            if e.get("content_id") == cid and e.get("event") == "appeal":
                n += 1
    return n


texts = [
    "Michigan has some great lakes, lake Superior, Sleeping bear dunes, higgins lake, torch lake.",
    "Gym bros says the rule to bulking or shredding is eating carbs, lean meat and veggies.",
    "There are 50 states in America, each presenting its unique beauty, culture and people.",
    "Data Structures and Algorithms, Sql, Python, Excel are courses in Computer Science.",
    "Los angeles is full of diverse people and it makes the state look like a melting pot",
]

passed = 0
for i, text in enumerate(texts, 1):
    s1, sub = post("/submit", {"text": text, "creator_id": f"appeal_check_{i}"})
    cid = sub.get("content_id")
    s2, app = post("/appeal", {"content_id": cid, "reasoning": "I wrote this myself."})
    ok = s2 == 200 and app.get("status") == "under_review" and appeals_logged(cid) == 1
    passed += ok
    print(f"appeal {i}: submit={s1} appeal={s2} status={app.get('status')} logged={appeals_logged(cid)} -> {'PASS' if ok else 'FAIL'}")

print(f"\nCriterion 4: {passed} of 5 passed")

print("\nCriterion 5 error messages:")
for name, body in [
    ("empty", {"text": "", "creator_id": "check_empty"}),
    ("missing", {"creator_id": "check_missing"}),
]:
    code, resp = post("/submit", body)
    print(name, code, json.dumps(resp))