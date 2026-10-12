import json
import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

from test_snippet_mapping import SNIPPET_MAP

EXTENDED_MAP = dict(SNIPPET_MAP)
EXTENDED_MAP[r'\frac{\partial(\rho u)}{\partial x}' + "\n" + r'+\frac{\partial(\rho v)}{\partial y}' + "\n" + r'+\frac{\partial(\rho w)}{\partial z}' + "\n" + r'+\frac{\partial\rho}{\partial t}=0'] = '∂(ρu)/∂x + ∂(ρv)/∂y + ∂(ρw)/∂z + ∂ρ/∂t = 0'
EXTENDED_MAP[r'a_x=\frac{\partial u}{\partial t}' + "\n" + r'+u\frac{\partial u}{\partial x}' + "\n" + r'+v\frac{\partial u}{\partial y}' + "\n" + r'+w\frac{\partial u}{\partial z}'] = 'a_x = ∂u/∂t + u(∂u/∂x) + v(∂u/∂y) + w(∂u/∂z)'
EXTENDED_MAP[r'\rho V'] = 'ρV'
EXTENDED_MAP[r'\rho uA'] = 'ρuA'
EXTENDED_MAP[r'\rho_2'] = 'ρ₂'
EXTENDED_MAP[r'u_1A_1'] = 'u₁A₁'

double_dollar_regex = re.compile(r'\$\$([^\$]+)\$\$', re.DOTALL)
dollar_regex = re.compile(r'\$([^\$]+)\$')

def replace_math_in_str(s):
    if not isinstance(s, str): return s
    def replace_double(m):
        raw = m.group(1).strip()
        if raw in EXTENDED_MAP: return EXTENDED_MAP[raw]
        norm = " ".join(raw.split())
        return EXTENDED_MAP[norm]
    s = double_dollar_regex.sub(replace_double, s)
    def replace_single(m):
        raw = m.group(1).strip()
        if raw in EXTENDED_MAP: return EXTENDED_MAP[raw]
        norm = " ".join(raw.split())
        return EXTENDED_MAP[norm]
    s = dollar_regex.sub(replace_single, s)
    return s

files = sorted(glob.glob("JSON_Simulacore/*.json"))

latex_cmd_regex = re.compile(r'\\[a-zA-Z]+')

for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"\nChecking {fpath}...")
    issues = []
    for i, q in enumerate(data):
        texts = [("question", q.get("question", "")), ("explanation", q.get("explanation", ""))]
        if "options" in q and isinstance(q["options"], list):
            for opt_idx, opt in enumerate(q["options"]):
                texts.append((f"opt[{opt_idx}]", opt))
        if "correct" in q and isinstance(q["correct"], str):
            texts.append(("correct", q["correct"]))
            
        for field, t in texts:
            if not isinstance(t, str): continue
            t_new = replace_math_in_str(t)
            if '$' in t_new:
                issues.append(f"Q{i+1} {field}: '$' in text: {t_new}")
            cmds = latex_cmd_regex.findall(t_new)
            # filter out valid escapes like \n, \t if any
            real_cmds = [c for c in cmds if c not in [r'\n', r'\t', r'\r']]
            if real_cmds:
                issues.append(f"Q{i+1} {field}: possible LaTeX command: {real_cmds} in: {t_new}")
                
    if issues:
        print(f"  Found {len(issues)} issues:")
        for iss in issues[:10]:
            print("   ", iss)
    else:
        print("  Clean! No stray '$' or LaTeX commands found.")
