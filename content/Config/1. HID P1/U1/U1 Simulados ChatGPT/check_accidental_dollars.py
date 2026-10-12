import glob, json, re

for f in sorted(glob.glob('JSON_Simulacore/*.json')):
    data = json.load(open(f, encoding='utf-8'))
    for idx, q in enumerate(data):
        for fld in ['question', 'explanation'] + q.get('options', []):
            matches = re.findall(r'\$([^\$]+)\$', fld)
            for m in matches:
                # check if m contains words like 'então', 'expressão', etc.
                if any(w in m for w in ['então', 'expressão', 'Nessa', 'constante', 'Se ']):
                    print(f"{f} Q{idx}: ${m}$")
