class Manual:
    def __init__(self, data):
        if len(data) == 0:
            self.title = []
        else:
            self.title = data[0]
        if len(data) <= 1:
            self.values = []
        else:
            self.values = data[1:]


    def prepare_data(self):
        title = self.title.strip().split(',')
        values = [row.strip().split(',') for row in self.values]
        return title, values

    def convert_data_to_json(self):
        title, values = self.prepare_data()
        raw_res = []
        for row in values:
            d = dict(zip(title, row))
            values_form = ",".join([""""{}":    "{}" """.format(key, value) for key, value in d.items()])
            raw_res.append("""{{ {} }}""".format(values_form))

        return "[{}]".format(",".join(raw_res))




def read_data_to_list(file):
    f = open(file)
    content = f.readlines()
    f.close()
    return content


def write_data(file, data):
    f = open(file, 'w')
    f.write(data)
    f.close()

def main():
    content = read_data_to_list('input.txt')
    converter = Manual(content)
    json_text =  converter.convert_data_to_json()
    write_data('output.json', json_text)

if __name__ == '__main__':
    main()

