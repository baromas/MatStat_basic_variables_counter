import math

data = list(map(int, input().split()))


def average_sample():
    return sum(data) / len(data)


def dispersion():
    y = average_sample()
    summ = 0
    for i in data:
        summ += (i - y) ** 2
    return summ / len(data)


def sel_dispersion():
    y = average_sample()
    summ = 0
    for i in data:
        summ += (i - y) ** 2
    return summ / (len(data) - 1)


def standard_deviation(element):
    return math.sqrt(element)


def selection_coefficient():
    return standard_deviation(sel_dispersion()) / average_sample()


def sturgess_method():
    return int(1 + math.log2(len(data)))


def scope():
    return (max(data) - min(data)) / sturgess_method()


def get_count(number):
    s = str(number)
    if '.' in s:
        return abs(s.find('.') - len(s)) - 1
    else:
        return 0


def print_table():
    interval = list()
    frequency = list()
    n = min(data)
    a = get_count(scope())
    while n <= float(max(data)):
        interval.append(round(n, a))
        n += scope()
    print("X:", interval)
    data.sort()
    number = 0
    for count, interv in enumerate(interval):
        for value in data:
            if interv <= value < interval[count]:
                number += 1
        frequency.append(number)






if __name__ == '__main__':
    print(sum(data))
    print(len(data))
    print(data)
    print('Среднее выборочное значение:', average_sample())
    print('Генеральная дисперсия:', dispersion())
    print('Дисперсия выборочной совокупности:', sel_dispersion())
    print('Стандартное отклонение дисперсии:', standard_deviation(dispersion()))
    print('Стандартное отклонение выборочной дисперсии:', standard_deviation(sel_dispersion()))
    print('Коэффициент вариации:', selection_coefficient())
    if selection_coefficient() < 0.33:
        print("Совокупность однородна")
    else:
        print("Совокупность неоднородна")

    print('Количество интервалов по формуле Стёрджесса:', sturgess_method())
    print('Размах:', scope())
    print_table()
