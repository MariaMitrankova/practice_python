import json

class Lib:
    def __init__(self, data):
        if len(data) == 0:
            self.title = []
        else:
            self.title = data[0]
        if len(data) <= 1:
            self.values = []
        else:
            self.values = data[1:]

    def convert_data_to_json(self):
        new_data = []
        for row in self.values:
            value = row.strip().split(',')
            d = dict(zip(self.title, value))
            new_data.append(d)
        output = json.dumps(new_data, indent=4)

        return output



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
    converter = Lib(content)
    json_text =  converter.convert_data_to_json()
    write_data('../output.json', json_text)


if __name__ == '__main__':
    main()