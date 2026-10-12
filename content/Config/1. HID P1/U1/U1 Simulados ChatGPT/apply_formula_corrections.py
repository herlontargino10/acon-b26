import os
import glob
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

from test_snippet_mapping import SNIPPET_MAP

# Extended mapping with multi-line expressions and extra variants
EXTENDED_MAP = dict(SNIPPET_MAP)
EXTENDED_MAP[r'\frac{\partial(\rho u)}{\partial x}' + "\n" + r'+\frac{\partial(\rho v)}{\partial y}' + "\n" + r'+\frac{\partial(\rho w)}{\partial z}' + "\n" + r'+\frac{\partial\rho}{\partial t}=0'] = '∂(ρu)/∂x + ∂(ρv)/∂y + ∂(ρw)/∂z + ∂ρ/∂t = 0'
EXTENDED_MAP[r'a_x=\frac{\partial u}{\partial t}' + "\n" + r'+u\frac{\partial u}{\partial x}' + "\n" + r'+v\frac{\partial u}{\partial y}' + "\n" + r'+w\frac{\partial u}{\partial z}'] = 'a_x = ∂u/∂t + u(∂u/∂x) + v(∂u/∂y) + w(∂u/∂z)'
EXTENDED_MAP[r'\rho V'] = 'ρV'
EXTENDED_MAP[r'\rho uA'] = 'ρuA'
EXTENDED_MAP[r'\rho_2'] = 'ρ₂'
EXTENDED_MAP[r'u_1A_1'] = 'u₁A₁'

double_dollar_regex = re.compile(r'\$\$([^\$]+)\$\$', re.DOTALL)
dollar_regex = re.compile(r'\$([^\$]+)\$')

def replace_math_in_str(s, stats, ch_idx):
    if not isinstance(s, str):
        return s
        
    def replace_double(m):
        raw = m.group(1).strip()
        stats[ch_idx]['display'] += 1
        stats[ch_idx]['total'] += 1
        if raw in EXTENDED_MAP:
            return EXTENDED_MAP[raw]
        norm = " ".join(raw.split())
        if norm in EXTENDED_MAP:
            return EXTENDED_MAP[norm]
        raise ValueError(f"Unmapped display math: {repr(raw)}")
        
    s = double_dollar_regex.sub(replace_double, s)
    
    def replace_single(m):
        raw = m.group(1).strip()
        stats[ch_idx]['inline'] += 1
        stats[ch_idx]['total'] += 1
        if raw in EXTENDED_MAP:
            return EXTENDED_MAP[raw]
        norm = " ".join(raw.split())
        if norm in EXTENDED_MAP:
            return EXTENDED_MAP[norm]
        raise ValueError(f"Unmapped inline math: {repr(raw)}")
        
    s = dollar_regex.sub(replace_single, s)
    return s

def process_all():
    in_dir = "JSON_Simulacore"
    out_dir = "JSON_Simulacore_CORRIGIDOS"
    os.makedirs(out_dir, exist_ok=True)
    
    files = sorted(glob.glob(os.path.join(in_dir, "*.json")))
    print(f"Processing {len(files)} files...")
    
    stats = {}
    
    for idx, fpath in enumerate(files, 1):
        fname = os.path.basename(fpath)
        out_path = os.path.join(out_dir, fname)
        stats[idx] = {'file': fname, 'total': 0, 'inline': 0, 'display': 0, 'questions': 0}
        
        with open(fpath, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        stats[idx]['questions'] = len(data)
        
        new_data = []
        for q in data:
            new_q = dict(q)
            if "question" in new_q and isinstance(new_q["question"], str):
                new_q["question"] = replace_math_in_str(new_q["question"], stats, idx)
            if "explanation" in new_q and isinstance(new_q["explanation"], str):
                new_q["explanation"] = replace_math_in_str(new_q["explanation"], stats, idx)
            if "options" in new_q and isinstance(new_q["options"], list):
                new_q["options"] = [replace_math_in_str(opt, stats, idx) for opt in new_q["options"]]
            if "correct" in new_q and isinstance(new_q["correct"], str):
                new_q["correct"] = replace_math_in_str(new_q["correct"], stats, idx)
            new_data.append(new_q)
            
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(new_data, f, ensure_ascii=False, indent=2)
            
        print(f"Chapter {idx} ({fname}): {stats[idx]['total']} formulas corrected ({stats[idx]['inline']} inline, {stats[idx]['display']} display).")

    print("\nSummary statistics:")
    total_all = sum(s['total'] for s in stats.values())
    print(f"Total formulas corrected across all chapters: {total_all}")
    
    # Save stats to a json for report generation
    with open("formula_correction_stats.json", "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    process_all()
