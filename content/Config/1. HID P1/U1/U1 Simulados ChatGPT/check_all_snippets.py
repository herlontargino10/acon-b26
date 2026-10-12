import json
import glob
import re

files = sorted(glob.glob("JSON_Simulacore/*.json"))

from test_snippet_mapping import SNIPPET_MAP

double_dollar_regex = re.compile(r'\$\$([^\$]+)\$\$', re.DOTALL)
dollar_regex = re.compile(r'\$([^\$]+)\$')

missing = set()
total_occurrences = 0

for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    for q in data:
        texts = []
        if "question" in q: texts.append(q["question"])
        if "explanation" in q: texts.append(q["explanation"])
        if "options" in q: texts.extend(q["options"])
        if "correct" in q and isinstance(q["correct"], str): texts.append(q["correct"])
        
        for t in texts:
            if not isinstance(t, str): continue
            
            # Find display math
            for m in double_dollar_regex.findall(t):
                total_occurrences += 1
                # normalise whitespace inside display math (e.g. newlines)
                m_norm = " ".join(m.split())
                m_clean = m.strip()
                if m_clean not in SNIPPET_MAP and m_norm not in SNIPPET_MAP:
                    missing.add((m_clean, m_norm))
            
            # remove display math
            t_no_disp = double_dollar_regex.sub('', t)
            for m in dollar_regex.findall(t_no_disp):
                total_occurrences += 1
                m_norm = " ".join(m.split())
                m_clean = m.strip()
                if m_clean not in SNIPPET_MAP and m_norm not in SNIPPET_MAP:
                    missing.add((m_clean, m_norm))

print(f"Total math occurrences found: {total_occurrences}")
print(f"Missing from SNIPPET_MAP: {len(missing)}")
for m_clean, m_norm in sorted(missing):
    print("MISSING:", repr(m_clean))
