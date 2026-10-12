import glob, json, re

for f in sorted(glob.glob('JSON_Simulacore/*.json')):
    data = json.load(open(f, encoding='utf-8'))
    for idx, q in enumerate(data):
        for fld in ['question', 'explanation'] + q.get('options', []):
            for m in re.findall(r'\$\$([^\$]+)\$\$', fld, re.DOTALL):
                print(f"{f.split('/')[-1]} Q{idx} block: {repr(m.strip())}")
