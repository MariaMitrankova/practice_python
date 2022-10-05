# Vivelapaix

with open("solution.py") as f:
    content = f.read()
    description, code = content.split('# ---end----')
    lines = description.split('\n')
    for line in lines:
        if line.startswith('# title'):
            title = line.split('# title')
        if line.startswith('# description'):
            description = line.split('# description')

with open("out.txt", 'w') as md:
    link = '-'.join(''.join(title[1].lower().split()))
    out = '+ [{}](#{})\n\n## {}\n\n'.format(title[1], link, description[1])
    md.write(out)
    fcode = '```pyhon\n\n{}```'.format(code)
    md.write(fcode)