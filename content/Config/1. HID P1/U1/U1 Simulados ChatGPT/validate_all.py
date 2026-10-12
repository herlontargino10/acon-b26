import glob, re, json, os

JSON_DIR = "JSON_Simulacore"
EXPECTED_FILES = [
    "SIMULADO_U1_CAPITULO_1_NIVEL_FACIL_AMPLIADO_AUDITADO.json",
    "SIMULADO_U1_CAPITULO_2_NIVEL_FACIL_AMPLIADO_AUDITADO.json",
    "SIMULADO_U1_CAPITULO_3_NIVEL_FACIL_AMPLIADO_AUDITADO.json",
    "SIMULADO_U1_CAPITULO_4_NIVEL_FACIL_AMPLIADO_AUDITADO.json",
    "SIMULADO_U1_CAPITULO_5_NIVEL_FACIL_AMPLIADO_AUDITADO.json",
    "SIMULADO_U1_CAPITULO_6_NIVEL_FACIL_AMPLIADO_AUDITADO.json",
    "SIMULADO_U1_CAPITULO_7_NIVEL_FACIL_AMPLIADO_AUDITADO.json",
    "SIMULADO_U1_CAPITULO_8_NIVEL_FACIL_AMPLIADO_AUDITADO.json"
]

def validate_all():
    print("=================== VALIDAÇÃO TÉCNICA E ESTRUTURAL ===================")
    total_converted = 0
    errors = []
    
    for fname in EXPECTED_FILES:
        fpath = os.path.join(JSON_DIR, fname)
        if not os.path.exists(fpath):
            errors.append(f"Arquivo ausente: {fpath}")
            continue
            
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            errors.append(f"Erro de sintaxe JSON em {fname}: {e}")
            continue
            
        if not isinstance(data, list):
            errors.append(f"{fname}: raiz não é uma lista")
            continue
            
        print(f"\n--- {fname} ---")
        print(f"Total de questões: {len(data)}")
        total_converted += len(data)
        
        type_counts = {}
        for idx, q in enumerate(data):
            qtype = q.get("type")
            type_counts[qtype] = type_counts.get(qtype, 0) + 1
            
            # Check required fields
            for fld in ["type", "question", "category", "explanation"]:
                if fld not in q:
                    errors.append(f"{fname} Q{idx}: campo obrigatório '{fld}' ausente")
                elif not q[fld] or (isinstance(q[fld], str) and not q[fld].strip()):
                    errors.append(f"{fname} Q{idx}: campo '{fld}' está vazio")
                    
            if qtype == "mc":
                if "options" not in q or not isinstance(q["options"], list) or len(q["options"]) < 2:
                    errors.append(f"{fname} Q{idx} (mc): options inválidas")
                if "correct" not in q or not isinstance(q["correct"], int):
                    errors.append(f"{fname} Q{idx} (mc): correct deve ser int")
                elif q["correct"] < 0 or q["correct"] >= len(q["options"]):
                    errors.append(f"{fname} Q{idx} (mc): índice correct ({q['correct']}) fora do alcance das opções (len={len(q['options'])})")
            elif qtype == "tf":
                if "options" not in q or q["options"] != ["Verdadeiro", "Falso"]:
                    errors.append(f"{fname} Q{idx} (tf): options deve ser ['Verdadeiro', 'Falso']")
                if "correct" not in q or not isinstance(q["correct"], bool):
                    errors.append(f"{fname} Q{idx} (tf): correct deve ser bool real")
            elif qtype == "gap":
                if "correct" not in q or not isinstance(q["correct"], str) or not q["correct"].strip():
                    errors.append(f"{fname} Q{idx} (gap): correct deve ser string não vazia")
                if "options" in q:
                    errors.append(f"{fname} Q{idx} (gap): gap não deve conter options")
            else:
                errors.append(f"{fname} Q{idx}: tipo desconhecido '{qtype}'")
                
        print(f"Distribuição de tipos: {type_counts}")
        
    print("\n=================== RESULTADO FINAL ===================")
    print(f"Total de questões convertidas em 8 arquivos: {total_converted}")
    if errors:
        print(f"ENCONTRADOS {len(errors)} ERROS:")
        for err in errors:
            print("  -", err)
    else:
        print("TODOS OS ARQUIVOS PASSARAM COM SUCESSO EM TODAS AS VALIDAÇÕES!")

validate_all()
