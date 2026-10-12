import json
import os
import glob
import re

files = sorted(glob.glob("JSON_Simulacore/*.json"))
print(f"Found {len(files)} files in JSON_Simulacore:")

dollar_regex = re.compile(r'\$([^\$]+)\$')
double_dollar_regex = re.compile(r'\$\$([^\$]+)\$\$')

all_inline_math = set()
all_display_math = set()

for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"\nFile: {os.path.basename(fpath)}, questions: {len(data)}")
    
    # Check all fields recursively or question by question
    for q_idx, item in enumerate(data):
        texts = []
        if "question" in item: texts.append(("question", item["question"]))
        if "explanation" in item: texts.append(("explanation", item["explanation"]))
        if "options" in item and isinstance(item["options"], list):
            for opt_idx, opt in enumerate(item["options"]):
                texts.append((f"opt[{opt_idx}]", opt))
        if "correct" in item and isinstance(item["correct"], str):
            texts.append(("correct", item["correct"]))
            
        for field, text in texts:
            if not isinstance(text, str):
                continue
            # check double dollar
            doubles = double_dollar_regex.findall(text)
            for d in doubles:
                all_display_math.add(d.strip())
            # remove doubles before finding singles
            text_no_doubles = double_dollar_regex.sub('', text)
            singles = dollar_regex.findall(text_no_doubles)
            for s in singles:
                all_inline_math.add(s.strip())

print(f"\nUnique display math ($$...$$): {len(all_display_math)}")
for m in sorted(all_display_math):
    print("  DISPLAY:", repr(m))

print(f"\nUnique inline math ($...$): {len(all_inline_math)}")
for m in sorted(all_inline_math):
    print("  INLINE:", repr(m))
