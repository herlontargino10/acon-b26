import glob, re, json, os

CATEGORIES = {
    1: "Hidrodinâmica — Conservação da Massa",
    2: "Hidrodinâmica — Quantidade de Movimento e Derivada Material",
    3: "Hidrodinâmica — Forças em Elemento Fluido e Navier-Stokes",
    4: "Hidrodinâmica — Conservação da Energia e Hipóteses Fundamentais",
    5: "Hidrodinâmica — Roteiro de Resolução de Escoamentos Internos",
    6: "Hidrodinâmica — Poiseuille e Escoamento Conduzido por Pressão",
    7: "Hidrodinâmica — Canal Inclinado e Escoamento Conduzido por Gravidade",
    8: "Hidrodinâmica — Couette e Escoamento Conduzido por Cisalhamento"
}

OUTPUT_DIR = "JSON_Simulacore"

def clean_gap_answer(raw_ans):
    ans = raw_ans.strip()
    
    # Check for cases with explanatory suffix:
    # e.g., "$W$ (trabalho), pois a expressão completa é $E=Q-W$."
    # e.g., "$E$, representada na taxa temporal por $\dot{E}$."
    # e.g., "$gz$, completando a expressão $e=\hat{u}+\frac{1}{2}V^2+gz$."
    m_expl = re.search(r'^(.*?)(?:,\s*pois\s+(.*)|\s*\(.*?\)\s*,\s*pois\s+(.*)|,\s*representada\s+(.*)|,\s*completando\s+(.*))', ans, re.IGNORECASE)
    if m_expl:
        ans_part = m_expl.group(1).strip()
        expl_part = ans.strip()
        ans_part = re.sub(r'\.+$', '', ans_part).strip()
        ans_part = re.sub(r'^\*+|\*+$', '', ans_part).strip()
        return ans_part, expl_part
    
    # Handle bold markers like "**parada** ou **estacionária**." -> "parada ou estacionária"
    # Replace "**" throughout the answer:
    ans_clean = ans.replace('**', '').replace('__', '').strip()
    ans_clean = re.sub(r'\.+$', '', ans_clean).strip()
    
    return ans_clean, None

def convert_chapter(cap_num):
    fname = f"SIMULADO_U1_CAPITULO_{cap_num}_NIVEL_FACIL_AMPLIADO_AUDITADO.md"
    content = open(fname, encoding='utf-8').read()
    
    idx_gab = content.find('# Gabarito')
    if idx_gab == -1: idx_gab = content.find('## Gabarito')
    q_part = content[:idx_gab]
    g_part = content[idx_gab:]
    
    cat = CATEGORIES[cap_num]
    converted_questions = []
    
    # ----------------------------------------------------
    # QUESTÃO 1 (mc)
    # ----------------------------------------------------
    m_q1 = re.search(r'##\s*(?:1ª Questão|Questão 1).*?(?=##\s*(?:2ª Questão|Questão 2))', q_part, re.DOTALL)
    m_g1 = re.search(r'##\s*(?:1ª Questão|Questão 1)(.*?)(?=##\s*(?:2ª Questão|Questão 2))', g_part, re.DOTALL)
    
    q1_text = m_q1.group(0).strip()
    g1_text = m_g1.group(1).strip()
    
    opt_matches = re.findall(r'(?:^|\n)\s*(?:-\s*)?\(([a-e])\)\s*(.*?)(?=\n\s*(?:-\s*)?\([a-e]\)|\n\s*---|\Z)', q1_text, re.DOTALL)
    options_1 = [m[1].strip() for m in opt_matches]
    letters_1 = [m[0].lower() for m in opt_matches]
    
    prompt_1 = q1_text
    first_opt_idx = re.search(r'(?:^|\n)\s*(?:-\s*)?\([a-e]\)', q1_text)
    if first_opt_idx:
        prompt_1 = q1_text[:first_opt_idx.start()].strip()
    prompt_1 = re.sub(r'^##\s*[^\n]+\n*', '', prompt_1).strip()
    
    m_cor1 = re.search(r'(?:Resposta|correta)[^a-e\n]*\(([a-e])\)', g1_text, re.IGNORECASE)
    if not m_cor1:
        m_cor1 = re.search(r'\(([a-e])\)', g1_text)
    cor_letter_1 = m_cor1.group(1).lower()
    correct_idx_1 = letters_1.index(cor_letter_1)
    
    expl_1 = re.sub(r'^\s*\*\*(?:Resposta|Alternativa correta):[^\*]+\*\*\s*', '', g1_text).strip()
    expl_1 = re.sub(r'\s*\n*---\s*$', '', expl_1).strip()
    
    q1_obj = {
        "type": "mc",
        "question": prompt_1,
        "category": cat,
        "options": options_1,
        "correct": correct_idx_1,
        "explanation": expl_1
    }
    converted_questions.append(q1_obj)
    
    # ----------------------------------------------------
    # QUESTÃO 2 (gap)
    # ----------------------------------------------------
    m_q2 = re.search(r'##\s*(?:2ª Questão|Questão 2).*?(?=##\s*(?:3ª Questão|Questão 3))', q_part, re.DOTALL)
    m_g2 = re.search(r'##\s*(?:2ª Questão|Questão 2)(.*?)(?=##\s*(?:3ª Questão|Questão 3))', g_part, re.DOTALL)
    
    q2_text = m_q2.group(0).strip()
    g2_text = m_g2.group(1).strip()
    
    q2_items = re.findall(r'(?:^|\n)\s*(\d+)\.\s*(.*?)(?=\n\s*\d+\.|\n\s*---|\Z)', q2_text, re.DOTALL)
    
    g2_lines = g2_text.split('\n')
    g2_answers = {}
    g2_extra_expl = ""
    
    for line in g2_lines:
        m_line = re.match(r'^\s*(\d+)\.\s*(.*)', line)
        if m_line:
            num = int(m_line.group(1))
            val = m_line.group(2).strip()
            g2_answers[num] = val
        elif "**Por que" in line or "**Nota" in line or g2_extra_expl:
            clean_l = re.sub(r'^\s*---\s*$', '', line).strip()
            if clean_l:
                g2_extra_expl += ("\n" + clean_l if g2_extra_expl else clean_l)
            
    for num_str, prompt in q2_items:
        num = int(num_str)
        raw_ans = g2_answers.get(num, "")
        
        ans_clean, specific_expl = clean_gap_answer(raw_ans)
        
        if specific_expl:
            final_expl = specific_expl
        elif g2_extra_expl.strip():
            final_expl = g2_extra_expl.strip()
        else:
            final_expl = f"Resposta esperada para a lacuna: {ans_clean}."
            
        final_expl = re.sub(r'\s*\n*---\s*$', '', final_expl).strip()
            
        q2_obj = {
            "type": "gap",
            "question": prompt.strip(),
            "category": cat,
            "correct": ans_clean,
            "explanation": final_expl
        }
        converted_questions.append(q2_obj)
        
    # ----------------------------------------------------
    # QUESTÃO 3 (tf)
    # ----------------------------------------------------
    m_q3 = re.search(r'##\s*(?:3ª Questão|Questão 3).*?(?=##\s*(?:4ª Questão|Questão 4))', q_part, re.DOTALL)
    m_g3 = re.search(r'##\s*(?:3ª Questão|Questão 3)(.*?)(?=##\s*(?:4ª Questão|Questão 4))', g_part, re.DOTALL)
    
    q3_text = m_q3.group(0).strip()
    g3_text = m_g3.group(1).strip()
    
    q3_items = re.findall(r'(?:^|\n)\s*(\d+)\.\s*(?:\([^\)]*\)\s*)?(.*?)(?=\n\s*\d+\.|\n\s*---|\Z)', q3_text, re.DOTALL)
    g3_items = re.findall(r'(?:^|\n)\s*(\d+)\.\s*(.*?)(?=\n\s*\d+\.|\n\s*---|\Z)', g3_text, re.DOTALL)
    
    g3_dict = {}
    for num_str, body in g3_items:
        num = int(num_str)
        m_vf = re.match(r'^\s*\*\*(Verdadeir[ao]|Fals[ao]|V|F)\.?\*\*\s*([—–-]?\s*.*)', body.strip(), re.DOTALL | re.IGNORECASE)
        if m_vf:
            v_or_f = m_vf.group(1).upper()
            is_true = v_or_f.startswith('V')
            expl = m_vf.group(2).strip()
            expl = re.sub(r'^[—–-]\s*', '', expl).strip()
            g3_dict[num] = (is_true, expl)
            
    for num_str, prompt in q3_items:
        num = int(num_str)
        is_true, expl = g3_dict[num]
        
        q3_obj = {
            "type": "tf",
            "question": prompt.strip(),
            "category": cat,
            "options": ["Verdadeiro", "Falso"],
            "correct": is_true,
            "explanation": expl if expl else ("Afirmativa verdadeira segundo o material." if is_true else "Afirmativa falsa segundo o material.")
        }
        converted_questions.append(q3_obj)
        
    # ----------------------------------------------------
    # QUESTÃO 4 (mc)
    # ----------------------------------------------------
    m_q4 = re.search(r'##\s*(?:4ª Questão|Questão 4).*?(?=##\s*(?:5ª Questão|Questão 5))', q_part, re.DOTALL)
    m_g4 = re.search(r'##\s*(?:4ª Questão|Questão 4)(.*?)(?=##\s*(?:5ª Questão|Questão 5))', g_part, re.DOTALL)
    
    q4_text = m_q4.group(0).strip()
    g4_text = m_g4.group(1).strip()
    
    q4_blocks = re.split(r'\n###\s*', q4_text)
    q4_items = []
    for b in q4_blocks:
        if not b.strip(): continue
        m_sub = re.match(r'^(?:Questão\s*)?4\.(\d+)[^\n]*\n+(.*)', b, re.DOTALL)
        if m_sub:
            num = int(m_sub.group(1))
            first_line = b.split('\n')[0].strip()
            body = m_sub.group(2).strip()
            lines = body.split('\n')
            prompt_lines = []
            opt_lines = []
            for line in lines:
                m_opt = re.match(r'^\s*(?:-\s*)?\(([a-e])\)\s*(.*)', line)
                if m_opt:
                    opt_lines.append((m_opt.group(1).lower(), m_opt.group(2).strip()))
                elif not opt_lines:
                    prompt_lines.append(line)
                else:
                    if opt_lines:
                        last_letter, last_text = opt_lines[-1]
                        opt_lines[-1] = (last_letter, (last_text + ' ' + line.strip()).strip())
            
            body_prompt = '\n'.join(prompt_lines).strip()
            if body_prompt:
                final_q_text = body_prompt
            else:
                # In chapters 5, 6, 7 the prompt is in the header line: "### 4.1. Por que o resumo..."
                # Strip leading "4.1." or "Questão 4.1."
                header_prompt = re.sub(r'^(?:Questão\s*)?4\.\d+\.?\s*(?:[—–-]\s*)?', '', first_line).strip()
                final_q_text = header_prompt

            clean_options = []
            for opt_letter, opt_text in opt_lines:
                opt_cleaned = re.sub(r'\s*\n*---\s*$', '', opt_text).strip()
                clean_options.append((opt_letter, opt_cleaned))

            q4_items.append({
                'num': num,
                'prompt': final_q_text,
                'options': [o[1] for o in clean_options],
                'opt_letters': [o[0] for o in clean_options]
            })
            
    g4_ans = {}
    blocks_a = re.split(r'\n###\s*', '\n' + g4_text)
    for b in blocks_a:
        m_a = re.match(r'^(?:Questão\s*)?4\.(\d+)[^\n]*?(?:\(([a-e])\)|Resposta\s*\(([a-e])\))[^\n]*\n*(.*)', b, re.DOTALL)
        if m_a:
            sub_num = int(m_a.group(1))
            letter = (m_a.group(2) or m_a.group(3)).lower()
            expl = m_a.group(4).strip()
            expl = re.sub(r'\s*\n*---\s*$', '', expl).strip()
            g4_ans[sub_num] = (letter, expl)
            
    if not g4_ans:
        for line in g4_text.split('\n'):
            m_b = re.match(r'^\s*-\s*\*\*4\.(\d+)\s*[—–-]\s*\(([a-e])\)\.?\*\*\s*(.*)', line)
            if m_b:
                sub_num = int(m_b.group(1))
                letter = m_b.group(2).lower()
                expl = m_b.group(3).strip()
                expl = re.sub(r'\s*\n*---\s*$', '', expl).strip()
                g4_ans[sub_num] = (letter, expl)
                
    if not g4_ans:
        for line in g4_text.split('\n'):
            m_c = re.match(r'^\s*(\d+)\.\s*\*\*\(([a-e])\)\*\*\s*[—–-]\s*(.*)', line)
            if m_c:
                sub_num = int(m_c.group(1))
                letter = m_c.group(2).lower()
                expl = m_c.group(3).strip()
                expl = re.sub(r'\s*\n*---\s*$', '', expl).strip()
                g4_ans[sub_num] = (letter, expl)
                
    for item in q4_items:
        num = item['num']
        cor_letter, expl = g4_ans[num]
        cor_idx = item['opt_letters'].index(cor_letter)
        
        q4_obj = {
            "type": "mc",
            "question": item['prompt'],
            "category": cat,
            "options": item['options'],
            "correct": cor_idx,
            "explanation": expl
        }
        converted_questions.append(q4_obj)
        
    out_name = f"SIMULADO_U1_CAPITULO_{cap_num}_NIVEL_FACIL_AMPLIADO_AUDITADO.json"
    out_path = os.path.join(OUTPUT_DIR, out_name)
    with open(out_path, 'w', encoding='utf-8') as out_f:
        json.dump(converted_questions, out_f, ensure_ascii=False, indent=2)
        out_f.write('\n')
        
    print(f"Generated {out_path}: {len(converted_questions)} questions.")

for c in range(1, 9):
    convert_chapter(c)
