import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

ref_path = r"c:\Users\Herlon Targino\Documents\quartz\content\Config\1. HID P1\U1\U1 Simulacore\44_Questões_P1_Leis_de_Conservação(Versão_sem_calculo).json"

with open(ref_path, "r", encoding="utf-8") as f:
    ref_data = json.load(f)

print(f"Reference file total questions: {len(ref_data)}")

types = {}
for q in ref_data:
    t = q.get("type", "unknown")
    types[t] = types.get(t, 0) + 1
print(f"Type breakdown: {types}")

print("\n--- SAMPLE GAP QUESTIONS IN REFERENCE ---")
gap_count = 0
for q in ref_data:
    if q.get("type") == "gap":
        gap_count += 1
        print(f"[{gap_count}] Q: {q.get('question')}")
        print(f"    Correct: {repr(q.get('correct'))}")
        print(f"    Options: {q.get('options')}")
        print(f"    Explanation: {q.get('explanation')[:80]}...\n")

print("\n--- SAMPLE MC QUESTIONS WITH FORMULAS IN REFERENCE ---")
mc_count = 0
for q in ref_data:
    if q.get("type") == "mc" and any(sym in q.get("question", "") for sym in ["∇", "∂", "ρ", "μ", "τ"]):
        mc_count += 1
        print(f"[{mc_count}] Q: {q.get('question')}")
        print(f"    Options: {q.get('options')}")
        print(f"    Correct: {q.get('correct')}")
        print(f"    Explanation: {q.get('explanation')[:80]}...\n")
        if mc_count >= 5: break
