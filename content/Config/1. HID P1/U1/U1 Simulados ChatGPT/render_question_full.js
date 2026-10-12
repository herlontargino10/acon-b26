function renderQuestion() {
  S.phase = 'quiz';
  const q     = S.deck[S.idx];
  const val   = S.validated[S.idx];
  const flag  = S.flagged[S.idx];
  const ans   = S.answers[S.idx];
  const study = S.mode === 'study';
  /* DISC em Prova não revela gabarito nem autoavaliação — mas Revisão
     (S.reviewMode) nunca deve ser tratada como Prova aqui, mesmo que
     S.mode tenha ficado com valor de uma sessão anterior (ex.: o aluno
     volta à Biblioteca após uma Prova e depois abre a Revisão de outra
     matéria sem passar por startNew()/restart(), que resetam S.mode) */
  const discProva = q.type === 'disc' && !study && !S.reviewMode;

  /* consumir flags de animação antes de construir o HTML */
  const entering      = S.entering;      S.entering      = false;
  const justValidated = S.justValidated; S.justValidated = false;

  /* — corpo: opções MC, V/F, lacuna, discursiva ou associação — */
  let bodyHTML = '';

  if (q.type === 'mc') {
    bodyHTML = '<div class="options">' +
      q.shuffledOptions.map((opt, i) => {
        let cls = 'option';
        let sym = String.fromCharCode(65 + i);  // símbolo no círculo (A, B, C, D, E... conforme o índice)
        if (val) {
          cls += ' locked';
          /* Prova: trava a opção sem revelar certo/errado — só o Treino
             mostra a cor e a animação de acerto/erro */
          if (study) {
            if (i === q.shuffledCorrect) { cls += ' correct'; sym = icon('check'); }
            else if (ans === i)          { cls += ' wrong';   sym = icon('x'); }
            if (justValidated && (i === q.shuffledCorrect || ans === i)) cls += ' anim';
          } else if (ans === i) {
            cls += ' selected';
          }
        } else if (ans === i) {
          cls += ' selected';
        }
        const click = val ? '' : `onclick="App.pick(${i})"`;
        return `<div class="${cls}" ${click}>
          <span class="opt-ltr">${sym}</span>${esc(opt)}
        </div>`;
      }).join('') + '</div>';

  } else if (q.type === 'tf') {
    const correctBool = (q.correct === true || q.correct === 'true' || q.correct === 1);
    const opts = [{ label: 'Verdadeiro', val: true, sym: 'V' }, { label: 'Falso', val: false, sym: 'F' }];
    bodyHTML = '<div class="options">' +
      opts.map(o => {
        let cls = 'option';
        let sym = o.sym;
        if (val) {
          cls += ' locked';
          if (study) {
            if (o.val === correctBool) { cls += ' correct'; sym = icon('check'); }
            else if (ans === o.val)    { cls += ' wrong';   sym = icon('x'); }
            if (justValidated && (o.val === correctBool || ans === o.val)) cls += ' anim';
          } else if (ans === o.val) {
            cls += ' selected';
          }
        } else if (ans === o.val) {
          cls += ' selected';
        }
        const click = val ? '' : `onclick="App.pickTF(${o.val})"`;
        return `<div class="${cls}" ${click}>
          <span class="opt-ltr">${sym}</span>${o.label}
        </div>`;
      }).join('') + '</div>';

  } else if (q.type === 'gap') {
    let inputCls = 'gap-input';
    let hint     = '';
    /* Prova: input trava (disabled) mas sem cor nem gabarito revelado */
    if (val && study) {
      const ok = isCorrectAt(S.idx);
      inputCls += ok ? ' correct' : ' wrong';
      if (!ok) {
        hint = `<div class="gap-answer-hint show">${icon('check')} Resposta esperada: <strong>${esc(q.correct)}</strong></div>`;
      }
    }
    bodyHTML = `<div class="gap-wrap">
      <div class="gap-label">Digite a palavra ou expressão que completa a frase:</div>
      <input type="text" id="gap-input" class="${inputCls}"
        value="${esc(String(ans ?? ''))}"
        ${val ? 'disabled' : ''}
        placeholder="Sua resposta..."
        oninput="App.typeGap(this.value)"
        onkeydown="if(event.key==='Enter')App.verify()"
      />
      ${hint}
    </div>`;

  } else if (q.type === 'disc') {
    if (!val) {
      bodyHTML = `<div class="gap-wrap">
        <div class="gap-label">Digite sua resposta:</div>
        <textarea id="disc-input" class="gap-input" rows="4"
          placeholder="Sua resposta..."
          oninput="App.typeDisc(this.value)">${esc(String(ans ?? ''))}</textarea>
      </div>`;
    } else if (discProva) {
      /* Prova: resposta fica registrada, sem gabarito nem autoavaliação —
         a avaliação da discursiva fica pendente até depois de finalizar */
      bodyHTML = `<div class="gap-wrap">
        <div class="gap-label">Sua resposta (registrada):</div>
        <div class="gap-input" style="white-space:pre-wrap">${esc(String(ans || '(sem resposta)'))}</div>
      </div>`;
    } else {
      const evVal = S.discEval[S.idx];
      bodyHTML = `<div class="gap-wrap">
        <div class="gap-label">Sua resposta:</div>
        <div class="gap-input" style="white-space:pre-wrap">${esc(String(ans || '(sem resposta)'))}</div>
        ${q.correct ? `<div class="gap-label" style="margin-top:10px">Gabarito / resposta esperada:</div>
        <div class="gap-input" style="white-space:pre-wrap;border-color:var(--blue)">${esc(String(q.correct))}</div>` : ''}
        <div class="gap-label" style="margin-top:12px">Você acertou?</div>
        <div style="display:flex;gap:10px">
          <button class="${evVal==='correct' ? 'btn-ok' : 'btn-s'}" onclick="App.selfGradeDisc(true)">${icon('check')} Acertei</button>
          <button class="${evVal==='wrong'   ? 'btn-d'  : 'btn-s'}" onclick="App.selfGradeDisc(false)">${icon('x')} Errei</button>
        </div>
      </div>`;
    }

  } else if (q.type === 'assoc') {
    const n            = (q.options || []).length;
    const order        = q.assocOrder || [...Array(n).keys()];
    const currentAns   = Array.isArray(ans) ? ans : Array(n).fill(undefined);
    bodyHTML = '<div style="display:flex;flex-direction:column;gap:10px">' +
      q.options.map((pair, li) => {
        const leftLabel  = pair[0];
        const selected   = currentAns[li];
        const correctIdx = (q.correct && q.correct[li] !== undefined) ? q.correct[li] : li;
        let rowCls = 'option';
        if (val) {
          rowCls += ' locked';
          /* Prova: trava a linha sem indicar se o par está certo */
          if (study) rowCls += (selected === correctIdx) ? ' correct' : ' wrong';
        }
        const optsHTML = `<option value="" ${selected===undefined?'selected':''}>Selecione...</option>` +
          order.map(origIdx =>
            `<option value="${origIdx}" ${selected===origIdx?'selected':''}>${esc(q.options[origIdx][1])}</option>`
          ).join('');
        return `<div class="${rowCls}" style="justify-content:space-between;gap:12px;flex-wrap:wrap">
          <span style="flex:1;min-width:0;overflow-wrap:break-word">${esc(leftLabel)}</span>
          <select class="gap-input" style="width:auto;min-width:170px;margin:0;flex-shrink:0"
            ${val ? 'disabled' : ''} onchange="App.pickAssoc(${li}, this.value)">
            ${optsHTML}
          </select>
        </div>`;
      }).join('') + '</div>';
  }

  /* — explicação — */
  let expHTML = '';
  if (val) {
    if (q.type === 'disc' && !discProva) {
      const ev = S.discEval[S.idx];
      if (ev == null) {
        expHTML = q.explanation ? `<div class="explanation show">
          <div class="exp-res neutral">Marque acima se você acertou ou errou</div>
          ${esc(q.explanation)}
        </div>` : '';
      } else {
        expHTML = `<div class="explanation show">
          <div class="exp-res ${ev==='correct' ? 'ok' : 'bad'}">${ev==='correct' ? icon('check') + ' Você marcou: Acertei' : icon('x') + ' Você marcou: Errei'}</div>
          ${esc(q.explanation || '')}
        </div>`;
      }
    } else if (q.type !== 'disc' && (study || S.reviewMode)) {
      /* Prova (não-DISC): nenhum painel de explicação/feedback — só o
         estado travado das opções já indica que a resposta foi registrada */
      const ok = isCorrectAt(S.idx);
      expHTML = `<div class="explanation show">
    