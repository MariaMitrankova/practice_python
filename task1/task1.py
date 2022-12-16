DELIMETER = '#<!---end--->'

def read_data(file):
    with open(file) as f:
        content = f.read()
    return content

def write_data(content, file):
    with open(file, 'a+') as md:
        md.write(content)

def prepare_data(content):
    if len(content) > 0:
        description, code = content.split(DELIMETER)
    else:
        description = ''
        code = ''
    return description, code

def get_titles(description):
    new_title, new_description = None, None
    lines = description.split('\n')
    for line in lines:
        if line.startswith('# title'):
            new_title = line.replace('# title ', '')
        if line.startswith('# description'):
            new_description = line.replace('# description ', '')
    return new_title, new_description

def add_new_data(data):
    new_des, new_code = prepare_data(data)
    new_title, new_description = get_titles(new_des)
    link = new_title.lower().replace(' ', '-')
    out = '+ [{}](#{})\n## {}\n{}\n\n'.format(new_title, link, new_title, new_description)
    fcode = '```python\n{}\n```'.format(new_code)
    output = '\n' + out + '\n' + DELIMETER[1:] + '\n' + fcode
    return output


new_data = read_data('solution.py')
out = add_new_data(new_data)
#print(out)
write_data(out, 'solutions.md')

