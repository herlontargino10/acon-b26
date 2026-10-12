import glob, json, re

all_display_blocks = set()
for f in sorted(glob.glob('JSON_Simulacore/*.json')):
    data = json.load(open(f, encoding='utf-8'))
    for idx, q in enumerate(data):
        for fld in ['question', 'explanation'] + q.get('options', []):
            for m in re.findall(r'\$\$(.*?)\$\$', fld, re.DOTALL):
                all_display_blocks.add(m.strip())

print(f"Total unique display math blocks: {len(all_display_blocks)}")
for b in sorted(all_display_blocks):
    print("--- BLOCK ---")
    print(b)
