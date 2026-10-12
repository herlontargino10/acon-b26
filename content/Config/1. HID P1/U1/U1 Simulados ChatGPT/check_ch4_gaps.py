import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("JSON_Simulacore/SIMULADO_U1_CAPITULO_4_NIVEL_FACIL_AMPLIADO_AUDITADO.json", "r", encoding="utf-8") as f:
    data = json.load(f)

gaps = [q for q in data if q.get("type") == "gap"]
print(f"Chapter 4: {len(gaps)} gaps")
for i, g in enumerate(gaps):
    print(f"Gap {i+1}:")
    print(f"  Q: {g.get('question')}")
    print(f"  Ans: {g.get('correct')}")
