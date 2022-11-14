DELIMETER = '#<!---end--->'

def read_data(file):
    with open(file) as f:
        content = f.read()
    return content

def write_data(content, file):
    with open(file, 'w') as md:
        md.write(content)

def prepare_data(content):
    if len(content) > 0:
        description, code = content.split(DELIMETER)
    else:
        description = ''
        code = ''
    return description, code

def add_new_data(old_data, data):
    new_title, new_description = None, None
    new_des, new_code = prepare_data(data)
    lines = new_des.split('\n')
    for line in lines:
        if line.startswith('# title'):
            new_title = line.split('# title')
        if line.startswith('# description'):
            new_description = line.split('# description')

    link = new_title[1].lower().replace(' ', '-')
    out = '+ [{}](#{})\n\n## {}\n\n'.format(new_title[1], link, new_description[1])
    fcode = '```python\n{}\n```'.format(new_code)
    output = old_data + '\n' + out + '\n' + DELIMETER[1:] + '\n' + fcode
    return output


old_data = read_data('solutions.md')
new_data = read_data('solution.py')
out = add_new_data(old_data, new_data)
#print(out)
write_data(out, 'solutions.md')

