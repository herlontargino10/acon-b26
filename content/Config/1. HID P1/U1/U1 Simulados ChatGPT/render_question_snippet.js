function renderQuestionForm(key, qIdx) {
  S.phase = 'question-form';
  S.editorSubjectKey = key;
  S.editorQIdx = qIdx;
  renderHeader();

  const subj = SUBJECTS[key];
  const isNew = qIdx === -1;
  const base  = isNew
    ? { type:'mc', category:'', question:'', options:['','','',''], correct:0, explanation:'' }
    : { ...subj.questions[qIdx], options:[...(subj.questions[qIdx].options||[])] };
  /* padding de 4 alternativas vazias só se aplica ao tipo mc */
  if (base.type === 'mc') { while ((base.options||[]).length < 4) base.options.push(''); }

  const tabs = ['mc','tf','gap','disc','assoc'].map(t =>
    `<button class="qtype-tab${base.type===t?' active':''}" data-type="${t}"
       onclick="App.switchQType('${t}')">${t.toUpperCase()}</button>`).join('');

  $('app').innerHTML = `
    <div class="card entering" style="max-width:680px;margin:0 auto;padding:24px">
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:20px">
        <button class="btn-s" style="padding:6px 11px;font-size:12px"
          onclick="App.cancelQuestionEdit()">${icon('chevron-left')} Cancelar</button>
        <div class="home-title" style="margin:0">${isNew ? icon('plus') + ' Nova Questão' : icon('pencil') + ' Editar Questão'}</div>
      </div>

      <div class="form-group" style="margin-bottom:14px">
        <label class="gap-label">Tipo</label>
        <div class="qtype-tabs">${tabs}</div>
      </div>

      <div class="form-group" style="margin-bottom:14px">
        <label class="gap-label">Categoria</label>
        <input type="text" id="qf-category" class="gap-input"
          value="${esc(base.category)}" placeholder="Ex: Caldeiras, CO₂, Segurança...">
      </div>

      <div class="form-group" style="margin-bottom:14px">
        <label class="gap-label">Enunciado</label>
        <textarea id="qf-question" class="gap-input" rows="3"
          placeholder="Texto da questão...">${esc(base.question)}</textarea>
      </div>

      <div id="qf-dynamic">${buildDynamicFields(base)}</div>

      <div class="form-group" style="margin-top:14px">
        <label class="gap-label">Explicação (opcional)</label>
        <textarea id="qf-explanation" class="gap-input" rows="2"
          placeholder="Explicação da resposta correta...">${esc(base.explanation||'')}</textarea>
      </div>

      <div class="btn-bar" style="margin-top:22px">
        <button class="btn-s" onclick="App.cancelQuestionEdit()">Cancelar</button>
        <span class="spacer"></span>
        <button class="btn-p" onclick="App.saveQuestion()">${icon('save')} Salvar Questão</button>
      </div>
    </div>
  `;
  const qEl = $('qf-question'); if (qEl && isNew) qEl.focus();
}

/* Remove progresso, revisões, favoritos e histórico de uma matéria */
function cleanupSubjectData(key) {
  try { localStorage.removeItem(subjectProgressKey(KEY, key)); } catch(_) {}
  try { localStorage.removeItem(subjectProgressKey(REVIEW_PROGRESS_KEY, key)); } catch(_) {}
  try {
    const queue = loadReview().filter(r => r.subject !== key);
    saveReview(queue);
  } catch(_) {}
  try {
    const favs = loadFavs().filter(f => !f.startsWith(key + '::'));
    localStorage.setItem(userScopedKey(FAV_KEY), JSON.stringify(favs));
  } catch(_) {}
  try { clearSubjectHistory(key); } catch(_) {}
}

/* ═══════════════════════════════════════════════════
   RENDER — GERENCIAR MATÉRIAS
   ═══════════════════════════════════════════════════ */
function renderManageSubjects() {
  S.phase = 'manage';
  renderHeader();
  const customs = Object.values(SUBJECTS).filter(s => s.isCustom);
  const visible = customs.filter(s => !s.hidden);
  const hidden  = customs.filter(s =>  s.hidden);

  /* botões de uma matéria — visível ou oculta. Todas as matérias do
     usuário disponibilizam o mesmo conjunto de ações (Abrir, Editar,
     Exportar, Duplicar, Ocultar/Restaurar, Proteger, Excluir); só a
     ação de ocultar/restaurar e o estilo mudam conforme o estado. */
  function subjectRow(s) {
    const prot   = 