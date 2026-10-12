import re

path = r'C:\Users\Herlon Targino\Documents\quartz\content\Config\0. Simulacore\App Simula Core\Simula_Core.html'
content = open(path, encoding='utf-8').read()

print('MathJax?', 'mathjax' in content.lower())
print('KaTeX?', 'katex' in content.lower())
print('LaTeX?', 'latex' in content.lower())
print('Math?', 'math' in content.lower())

scripts = re.findall(r'<script[^>]*src=[\'"]([^\'"]+)[\'"]', content, re.IGNORECASE)
print('Script src tags:', scripts)

# Search for render or format or markdown or html functions
matches = re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\(', content)
print('Functions containing render or math or text:')
for m in matches:
    if any(k in m.lower() for k in ['render', 'math', 'text', 'format', 'escape', 'parse']):
        print(' ', m)
