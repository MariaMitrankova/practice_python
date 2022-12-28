class StrategyDeal:
    def __init__(self, deal):
        self.bank = deal['bank']
        self.entry = deal['entry']
        self.targets = deal['targets']
        self.close = deal['close']

    def get_targets(self):
        # вернуть список таргетов в виде числовых значений float [21.5, 22.8, 23.5]
        return self.targets

    def get_target_percents(self):
        # вернуть список процентов, как в примере, округленные до 3 знака [6.912, 13.376, 16.857]
        return [round((target/self.entry - 1)*100, 3) for target in self.get_targets()]

    def get_target_banks(self):
        # список значений банков, если продавать активы по таргетам, как в пример, округленные до 3 знака [1069.12, 1133.764, 1168.573]
        return [round(self.bank*(100+percent)/100, 3) for percent in self.get_target_percents()]

    def __str__(self):
        # текстовое представление сделки
        txt = '''BANK: {}
START_PRICE: {}
STOP_PRICE: {}
        '''.format(self.bank, self.entry, self.close)
        for i in range(len(self.targets)):
            new_txt = '''
{} target: {}
Percent: {}%
Bank: {}
'''.format(i+1, self.get_targets()[i], self.get_target_percents()[i], self.get_target_banks()[i])
            txt += new_txt
        return txt



def read_data(file_name):
    file = open(file_name)
    content = file.read().split('-----')
    file.close()
    return content


def write_data(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()


def parse_data(content):
    deals = []
    for case in content:
        deal = {}
        lines = case.split('\n')
        for line in lines:
            if line.startswith('Bank: '):
                parsed = line.replace('Bank: ', '')[:-3]
                deal['bank'] = float(parsed)
            elif line.startswith('Entry: '):
                parsed = line.replace('Entry: ', '')[:-3]
                deal['entry'] = float(parsed)
            elif line.startswith('Target: '):
                parsed = line.replace('Target: ', '').split(';')
                parsed = [float(target[:-3]) for target in parsed]
                deal['targets'] = parsed

            elif line.startswith('Close: '):
                parsed = line.replace('Close: ', '')[:-3]
                deal['close'] = float(parsed)
        if len(deal) > 0:
            deals.append(deal)

    return deals

def main():
    content = read_data('deals.txt')
    deals = parse_data(content)
    result = []
    for deal in deals:
        manager = StrategyDeal(deal)
        result.append(str(manager))
        result.append('\n-----\n\n')
    result = ''.join(result[:-1])
    write_data('out.txt', result)


if __name__ == '__main__':
    main()