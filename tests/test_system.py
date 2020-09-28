import random


def num2text(num, len_num=3):
    dict = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть',
            7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять', 11: 'одинадцать', 12: 'двенядцать',
            13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать',
            17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать', 20: 'двадцать',
            30: 'тридцать', 40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят', 80: 'восемьдесят',
            90: 'девяноста', 100: 'сто', 200: 'двести', 300: 'триста', 400: 'четыреста', 500: 'пятьсот',
            600: 'шестьсот', 700: 'семьсот', 800: 'восемьсот', 900: 'девятьсот'}
    res = ['ноль'] * (len_num - len(str(num)))
    str_num = str(num)
    while str_num != '':
        if int(str_num) in dict.keys():
            res += [dict[int(str_num)]]
            str_num = ''
        else:
            res += [dict[int(str_num[0]) * (10**(len(str_num) - 1))]]
            str_num = str_num[1:]
    return ' '.join(res)


def test_system(output_file_name='output.txt', test_file_name='tests.txt', verdict_file_name='verdict.txt'):
    test = open(test_file_name, 'r')
    output = open(output_file_name, 'r')
    verdict = open(verdict_file_name, 'w')
    total_verdict = True
    answer_list = []
    check_list = []
    for answer in output:
        answer_list.append(answer.rstrip('\n'))
    for line in test:
        check_list.append(line.rstrip('\n').split('_')[-1])
    for i in range(len(answer_list)):
        if answer_list[i] != check_list[i]:
            verdict.write('WRONG ANSWER' + '\n')
            verdict.write(str(i + 1) + '\n')
            verdict.write('Ожидаемый ответ:' + '\n')
            verdict.write(check_list[i] + '\n')
            verdict.write('Вывод:' + '\n')
            verdict.write(answer_list[i] + '\n')
            total_verdict = False
    if total_verdict:
        verdict.write('OK')
    test.close()
    output.close()
    verdict.close()


def create_tests(count=50, test_file_name='tests.txt'):

    test = open(test_file_name, 'w')
    for i in range(count):
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999)
        num_str_1 = '0' * (3 - len(str(num1))) + str(num1)
        num_str_2 = '0' * (2 - len(str(num2))) + str(num2)
        num_str_3 = '0' * (3 - len(str(num3))) + str(num3)
        test.write(f'{i+1}_{num2text(num1)}/{num2text(num2, len_num=2)}/{num2text(num3)}_{num_str_1} {num_str_2} {num_str_3}' + '\n')
    test.close()
