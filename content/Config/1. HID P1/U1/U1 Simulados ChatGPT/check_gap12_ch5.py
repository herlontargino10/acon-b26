import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("JSON_Simulacore/SIMULADO_U1_CAPITULO_5_NIVEL_FACIL_AMPLIADO_AUDITADO.json", "r", encoding="utf-8") as f:
    data = json.load(f)

gaps = [q for q in data if q.get("type") == "gap"]
print("Gap 12:", json.dumps(gaps[11], ensure_ascii=False, indent=2))
