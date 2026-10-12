import glob, json, re

snippets = set()
for f in sorted(glob.glob('JSON_Simulacore/*.json')):
    data = json.load(open(f, encoding='utf-8'))
    for q in data:
        for fld in ['question', 'explanation'] + q.get('options', []):
            for m in re.findall(r'\$\$([^\$]+)\$\$', fld, re.DOTALL):
                snippets.add(m.strip())
            # remove $$...$$ first to find inline $...$
            clean_fld = re.sub(r'\$\$[^\$]+\$\$', '', fld, flags=re.DOTALL)
            for m in re.findall(r'\$([^\$]+)\$', clean_fld):
                snippets.add(m.strip())

open('all_snippets_raw.txt', 'w', encoding='utf-8').write('\n'.join(sorted(snippets)))
print(f'Total unique raw math snippets: {len(snippets)}')
