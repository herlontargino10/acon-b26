import glob, json, re

odd_count = 0
for f in sorted(glob.glob('JSON_Simulacore/*.json')):
    data = json.load(open(f, encoding='utf-8'))
    for idx, q in enumerate(data):
        for fld in ['question', 'explanation'] + q.get('options', []):
            m = re.findall(r'\$\$', fld)
            if len(m) % 2 != 0:
                print(f"{f} Q{idx} has odd number of $$: {len(m)}")
                odd_count += 1
            # strip $$...$$
            sub_clean = re.sub(r'\$\$[^\$]+\$\$', '', fld, flags=re.DOTALL)
            m_s = re.findall(r'\$', sub_clean)
            if len(m_s) % 2 != 0:
                print(f"{f} Q{idx} has odd number of single $: {len(m_s)}")
                odd_count += 1

print("Total odd delimiters:", odd_count)
