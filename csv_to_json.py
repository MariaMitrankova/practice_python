class Manual:
    def __init__(self):
        pass

    def convert_data_to_json(self, data):
        if len(data) == 0:
            return data
        title = data[0].strip().split(',')
        new_data = '['
        if len(data) > 1:
            new_data += '\n'
            for row in data[1:]:
                values = row.strip().split(',')
                d = dict(zip(title, values))
                new_data += '    {\n'
                for key in d:
                    new_data += '        "{}": "{}",\n'.format(key, d[key])
                new_data = new_data[:-2] + '\n    },\n'
            new_data = new_data[:-2] + '\n'
        new_data += ']'

        return new_data

    def convert_csv_to_json(self, input, output):
        content = self.read_data_to_list(input)
        json_text =  self.convert_data_to_json(content)
        self.write_data(output, json_text)

    def read_data_to_list(self,file):
        f = open(file)
        content = f.readlines()
        f.close()
        return content


    def write_data(self, file, data):
        f = open(file, 'w')
        f.write(data)
        f.close()

def main():
    converter = Manual()
    converter.convert_csv_to_json('input.txt', 'output.json')

if __name__ == '__main__':
    main()

