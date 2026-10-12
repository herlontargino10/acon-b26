import json
import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

from test_snippet_mapping import SNIPPET_MAP

# Add the multi-line and extra snippets
EXTENDED_MAP = dict(SNIPPET_MAP)
EXTENDED_MAP[r'\frac{\partial(\rho u)}{\partial x}' + "\n" + r'+\frac{\partial(\rho v)}{\partial y}' + "\n" + r'+\frac{\partial(\rho w)}{\partial z}' + "\n" + r'+\frac{\partial\rho}{\partial t}=0'] = '∂(ρu)/∂x + ∂(ρv)/∂y + ∂(ρw)/∂z + ∂ρ/∂t = 0'
EXTENDED_MAP[r'a_x=\frac{\partial u}{\partial t}' + "\n" + r'+u\frac{\partial u}{\partial x}' + "\n" + r'+v\frac{\partial u}{\partial y}' + "\n" + r'+w\frac{\partial u}{\partial z}'] = 'a_x = ∂u/∂t + u(∂u/∂x) + v(∂u/∂y) + w(∂u/∂z)'
EXTENDED_MAP[r'\rho V'] = 'ρV'
EXTENDED_MAP[r'\rho uA'] = 'ρuA'
EXTENDED_MAP[r'\rho_2'] = 'ρ₂'
EXTENDED_MAP[r'u_1A_1'] = 'u₁A₁'

# Let's inspect all files
files = sorted(glob.glob("JSON_Simulacore/*.json"))

double_dollar_regex = re.compile(r'\$\$([^\$]+)\$\$', re.DOTALL)
dollar_regex = re.compile(r'\$([^\$]+)\$')

def replace_math_in_str(s):
    # First replace display math $$ ... $$
    def replace_double(m):
        raw = m.group(1).strip()
        if raw in EXTENDED_MAP:
            return EXTENDED_MAP[raw]
        norm = " ".join(raw.split())
        if norm in EXTENDED_MAP:
            return EXTENDED_MAP[norm]
        raise ValueError(f"Unmapped display math: {repr(raw)}")
    
    s = double_dollar_regex.sub(replace_double, s)
    
    # Then replace inline math $ ... $
    def replace_single(m):
        raw = m.group(1).strip()
        if raw in EXTENDED_MAP:
            return EXTENDED_MAP[raw]
        norm = " ".join(raw.split())
        if norm in EXTENDED_MAP:
            return EXTENDED_MAP[norm]
        raise ValueError(f"Unmapped inline math: {repr(raw)}")
        
    s = dollar_regex.sub(replace_single, s)
    return s

all_ok = True
total_strings_processed = 0
total_replacements = 0

for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    for q_idx, q in enumerate(data):
        for key in ["question", "explanation"]:
            if key in q and isinstance(q[key], str):
                orig = q[key]
                new = replace_math_in_str(orig)
                if orig != new: total_replacements += 1
                if '$' in new:
                    print(f"Warning: '$' found in {fpath} Q{q_idx+1} {key}: {new}")
                    all_ok = False
        if "options" in q and isinstance(q["options"], list):
            for opt_idx, opt in enumerate(q["options"]):
                if isinstance(opt, str):
                    new = replace_math_in_str(opt)
                    if opt != new: total_replacements += 1
                    if '$' in new:
                        print(f"Warning: '$' found in {fpath} Q{q_idx+1} opt[{opt_idx}]: {new}")
                        all_ok = False
        if "correct" in q and isinstance(q["correct"], str):
            orig = q["correct"]
            new = replace_math_in_str(orig)
            if orig != new: total_replacements += 1
            if '$' in new:
                print(f"Warning: '$' found in {fpath} Q{q_idx+1} correct: {new}")
                all_ok = False

print(f"All OK: {all_ok}")
print(f"Total string replacements made: {total_replacements}")
