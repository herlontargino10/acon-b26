import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("JSON_Simulacore/SIMULADO_U1_CAPITULO_2_NIVEL_FACIL_AMPLIADO_AUDITADO.json", "r", encoding="utf-8") as f:
    data = json.load(f)

gaps = [q for q in data if q.get("type") == "gap"]
print("Chapter 2 Gap 14:", json.dumps(gaps[13], ensure_ascii=False, indent=2))
