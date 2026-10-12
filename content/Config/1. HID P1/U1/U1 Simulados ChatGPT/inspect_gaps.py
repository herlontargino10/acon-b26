import json
import glob

files = sorted(glob.glob("JSON_Simulacore/*.json"))

for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    gaps = [q for q in data if q.get("type") == "gap"]
    print(f"{fpath}: {len(gaps)} gap questions")
    for g in gaps:
        q_text = g.get("question", "")
        corr = g.get("correct", "")
        # print if contains math or underscores
        print(f"  Q: {q_text[:70]}... | Ans: {corr}")
