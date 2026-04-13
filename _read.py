content = open(r'f:\Gonzalo\Nutricion\Registro semanal.html', encoding='utf-8').read()
start = content.find('PDF EXPORT')
end = content.find('INIT', start)
section = content[start:end]
for i, line in enumerate(section.split('\n')):
    if 'JVB' not in line and len(line) < 200:
        print(f'{i:3}: {line}')
