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

for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"=== {fpath} ===")
    gaps = [q for q in data if q.get("type") == "gap"]
    for i, g in enumerate(gaps):
        q_new = replace_math_in_str(g.get("question", ""))
        c_new = replace_math_in_str(g.get("correct", ""))
        # Only print if math was in question or answer
        if g.get("question") != q_new or g.get("correct") != c_new:
            print(f"  Gap #{i+1}:")
            print(f"    Orig Q: {g.get('question')}")
            print(f"    New  Q: {q_new}")
            print(f"    Orig Ans: {g.get('correct')} -> New Ans: {c_new}")
