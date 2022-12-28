class StrategyDeal:
    def __init__(self, bank, entry, targets, close):
        self.bank = bank
        self.entry = entry
        self.targets = targets
        self.close = close

    def get_targets(self):
        # вернуть список таргетов в виде числовых значений float [21.5, 22.8, 23.5]
        return self.targets

    def get_target_percents(self):
        # вернуть список процентов, как в примере, округленные до 3 знака [6.912, 13.376, 16.857]
        return [round((target/self.entry - 1)*100, 3) for target in self.get_targets()]

    def get_target_banks(self):
        # список значений банков, если продавать активы по таргетам, как в пример, округленные до 3 знака [1069.12, 1133.764, 1168.573]
        return [self.bank*percent for percent in self.get_target_percents()]

    def __str__(self):
        # текстовое представление сделки
        txt = '''
        BANK: {}
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
    pass


def parse_data(content):
    bank, entry, targets, close = [], [], [], []
    for case in content:
        lines = case.split('\n')
        for line in lines:
            if line.startswith('Bank: '):
                parsed = line.replace('Bank: ', '')[:-4]
                bank.append(float(parsed))
            elif line.startswith('Entry: '):
                parsed = line.replace('Entry: ', '')[:-4]
                entry.append(float(parsed))
            elif line.startswith('Target: '):
                parsed = line.replace('Target: ', '').split(';')
                parsed = [float(target[:-3]) for target in parsed]
                targets.append(parsed)

            elif line.startswith('Close: '):
                parsed = line.replace('Close: ', '')[:-4]
                close.append(float(parsed))

    return bank, entry, targets, close

def main():
    content = read_data('deals.txt')
    deals = parse_data(content)
    result = content
    write_data('out.txt', result)


if __name__ == '__main__':
    main()