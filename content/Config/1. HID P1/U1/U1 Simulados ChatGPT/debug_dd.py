import glob

for f in sorted(glob.glob('JSON_Simulacore/*.json')):
    text = open(f, encoding='utf-8').read()
    idx = text.find('$$')
    print(f"{f}: first $$ at {idx}")
    if idx != -1:
        print(repr(text[idx-20:idx+60]))
