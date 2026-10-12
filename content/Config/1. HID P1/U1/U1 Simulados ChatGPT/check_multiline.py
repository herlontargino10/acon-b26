import glob, json, re

for f in sorted(glob.glob('JSON_Simulacore/*.json')):
    data = json.load(open(f, encoding='utf-8'))
    for idx, q in enumerate(data):
        for fld in ['question', 'explanation'] + q.get('options', []):
            if '$' in fld:
                # check if there's any multiline $...$
                s = re.sub(r'\$\$[^\$]+\$\$', '', fld, flags=re.DOTALL)
                for item in re.findall(r'\$([^\$]+)\$', s, re.DOTALL):
                    if '\n' in item:
                        print(f"{f} Q{idx} has newline in inline $: {repr(item)}")
