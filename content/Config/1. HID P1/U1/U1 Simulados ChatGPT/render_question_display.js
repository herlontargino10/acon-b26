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
        <div cla