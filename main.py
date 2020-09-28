from tests.test_system import create_tests, test_system


def text2num(string):
    """Преобразовывает число строкового представления в число с типом int"""
    dict = {'ноль': (0, 0), 'один': (1, 0), 'два': (2, 0), 'три': (3, 0), 'четыре': (4, 0), 'пять': (5, 0),
            'шесть': (6, 0), 'семь': (7, 0), 'восемь': (8, 0), 'девять': (9, 0), 'десять': (10, 1),
            'одинадцать': (11, 1),
            'двенядцать': (12, 1), 'тринадцать': (13, 1), 'четырнадцать': (14, 1), 'пятнадцать': (15, 1),
            'шестнадцать': (16, 1), 'семнадцать': (17, 1), 'восемнадцать': (18, 1), 'девятнадцать': (19, 1),
            'двадцать': (20, 1), 'тридцать': (30, 1), 'сорок': (40, 1), 'пятьдесят': (50, 1), 'шестьдесят': (60, 1),
            'семьдесят': (70, 1), 'восемьдесят': (80, 1), 'девяноста': (90, 1), 'сто': (100, 2), 'двести': (200, 2),
            'триста': (300, 2), 'четыреста': (400, 2), 'пятьсот': (500, 2), 'шестьсот': (600, 2), 'семьсот': (700, 2),
            'восемьсот': (800, 2), 'девятьсот': (900, 2)}

    res = []
    last_word = ''
    data = string.lower().split()
    for i in range(len(data)):
        word = data[i]
        if last_word:

            if word == 'ноль':
                res.append(dict[word][0])
                last_word = data[i]
            else:
                if dict[word][1] < dict[last_word][1]:
                    res[-1] += dict[word][0]
                    last_word = data[i]
                else:
                    res.append(dict[word][0])
                    last_word = data[i]

        else:
            res.append(dict[word][0])
            last_word = data[i]
    res = ''.join([str(i) for i in res])
    return res


if __name__ == "__main__":
    tests_file_name = 'tests.txt'
    output_file_name = 'output.txt'
    verdict_file_name = 'verdict.txt'
    create_tests(test_file_name=f'tests/{tests_file_name}', count=15000)
    tests = open(f'tests/{tests_file_name}', 'r')
    output = open(f'build/{output_file_name}', 'w')
    for i in tests:
        string = i.rstrip('\n').split('_')[1]
        output.write(
            f"{text2num(string.split('/')[0])} {text2num(string.split('/')[1])} {text2num(string.split('/')[2])}" + "\n")

    test_system(output_file_name=f'build/{output_file_name}',
                test_file_name=f'tests/{tests_file_name}', verdict_file_name=f'tests/{verdict_file_name}')
    tests.close()
    output.close()
