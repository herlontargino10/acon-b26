path = r'C:\Users\Herlon Targino\Documents\quartz\content\Config\0. Simulacore\App Simula Core\Simula_Core.html'
content = open(path, encoding='utf-8').read()

idx = content.find('function renderQuestion')
if idx != -1:
    open('render_question_snippet.js', 'w', encoding='utf-8').write(content[idx:idx+4000])
    print('Wrote render_question_snippet.js')
