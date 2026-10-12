import glob, json, re

latex_patterns = set()
for f in sorted(glob.glob('JSON_Simulacore/*.json')):
    data = json.load(open(f, encoding='utf-8'))
    for q in data:
        for text in [q.get('question',''), q.get('explanation','')] + q.get('options', []):
            if isinstance(text, str):
                inline = re.findall(r'\$([^\$]+)\$', text)
                for item in inline:
                    latex_patterns.add(item.strip())

open('all_latex_snippets.txt', 'w', encoding='utf-8').write('\n'.join(sorted(latex_patterns)))
print(f'Total unique latex snippets: {len(latex_patterns)}')
