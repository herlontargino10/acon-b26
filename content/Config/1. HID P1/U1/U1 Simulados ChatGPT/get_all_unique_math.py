import glob, json, re

all_math_found = set()
for f in sorted(glob.glob('JSON_Simulacore/*.json')):
    data = json.load(open(f, encoding='utf-8'))
    for q in data:
        for fld in ['question', 'explanation'] + q.get('options', []):
            # check $$...$$
            for m in re.findall(r'\$\$([^\$]+)\$\$', fld, re.DOTALL):
                all_math_found.add(m.strip())
            # remove $$...$$ first, then find $...$
            clean_fld = re.sub(r'\$\$[^\$]+\$\$', '', fld, flags=re.DOTALL)
            for m in re.findall(r'\$([^\$]+)\$', clean_fld):
                all_math_found.add(m.strip())

open('all_unique_math_in_json.txt', 'w', encoding='utf-8').write('\n'.join(sorted(all_math_found)))
print('Total math snippets found in JSON:', len(all_math_found))
