import os
import glob
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

orig_dir = "JSON_Simulacore"
corr_dir = "JSON_Simulacore_CORRIGIDOS"

orig_files = sorted(glob.glob(os.path.join(orig_dir, "*.json")))
corr_files = sorted(glob.glob(os.path.join(corr_dir, "*.json")))

print(f"Orig files count: {len(orig_files)}, Corr files count: {len(corr_files)}")
assert len(orig_files) == 8 and len(corr_files) == 8

total_orig_q = 0
total_corr_q = 0

all_valid = True

for f_orig, f_corr in zip(orig_files, corr_files):
    fname = os.path.basename(f_orig)
    print(f"\n--- Validating {fname} ---")
    
    # 1. Valid syntax
    try:
        with open(f_orig, "r", encoding="utf-8") as f:
            d_orig = json.load(f)
        with open(f_corr, "r", encoding="utf-8") as f:
            d_corr = json.load(f)
    except Exception as e:
        print(f"FAILED syntax check: {e}")
        all_valid = False
        continue
        
    total_orig_q += len(d_orig)
    total_corr_q += len(d_corr)
    
    # 2. Count comparison
    if len(d_orig) != len(d_corr):
        print(f"MISMATCH question count: orig={len(d_orig)}, corr={len(d_corr)}")
        all_valid = False
    else:
        print(f"Question count matches: {len(d_corr)}")
        
    # Check each question
    for idx, (q_o, q_c) in enumerate(zip(d_orig, d_corr)):
        q_num = idx + 1
        
        # Check keys
        if set(q_o.keys()) != set(q_c.keys()):
            print(f"MISMATCH keys in Q{q_num}: {q_o.keys()} vs {q_c.keys()}")
            all_valid = False
            
        # Check type
        if q_o["type"] != q_c["type"]:
            print(f"MISMATCH type in Q{q_num}: {q_o['type']} vs {q_c['type']}")
            all_valid = False
            
        # Check category
        if q_o["category"] != q_c["category"]:
            print(f"MISMATCH category in Q{q_num}")
            all_valid = False
            
        # Check correct answer preservation
        t = q_o["type"]
        if t == "mc":
            if q_o["correct"] != q_c["correct"]:
                print(f"MISMATCH MC correct in Q{q_num}: {q_o['correct']} vs {q_c['correct']}")
                all_valid = False
            if len(q_c["options"]) != len(q_o["options"]):
                print(f"MISMATCH MC options length in Q{q_num}")
                all_valid = False
        elif t == "tf":
            if q_o["correct"] != q_c["correct"]:
                print(f"MISMATCH TF correct in Q{q_num}: {q_o['correct']} vs {q_c['correct']}")
                all_valid = False
        elif t == "gap":
            # In gap, correct was converted from LaTeX if needed
            if not isinstance(q_c["correct"], str) or len(q_c["correct"].strip()) == 0:
                print(f"EMPTY gap correct in Q{q_num}")
                all_valid = False
                
        # Check explanation presence
        if not q_c.get("explanation") or len(q_c["explanation"].strip()) == 0:
            print(f"MISSING explanation in Q{q_num}")
            all_valid = False
            
        # Check for dollar signs or raw latex commands in all string fields
        strings_to_check = [q_c.get("question", ""), q_c.get("explanation", "")]
        if isinstance(q_c.get("correct"), str):
            strings_to_check.append(q_c["correct"])
        if isinstance(q_c.get("options"), list):
            for opt in q_c["options"]:
                if isinstance(opt, str):
                    strings_to_check.append(opt)
                    
        for s in strings_to_check:
            if "$" in s:
                print(f"DOLLAR SIGN in Q{q_num}: {repr(s)}")
                all_valid = False
            # Check for unrendered latex commands
            cmds = re.findall(r'\\[a-zA-Z]+', s)
            real_cmds = [c for c in cmds if c not in ['\\n', '\\t', '\\r']]
            if real_cmds:
                print(f"LATEX COMMAND {real_cmds} in Q{q_num}: {repr(s)}")
                all_valid = False

print(f"\n==========================================")
print(f"Total questions validated: {total_corr_q} (Orig: {total_orig_q})")
print(f"Overall Validation Result: {'PASSED (100% OK)' if all_valid else 'FAILED'}")
