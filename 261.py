def f(n):
    """
    Функция, которая получает на входе число и возращает уже приобразованное число по правилам
    :param n:
    :return преобразованное число :
    """
    bin_n = bin(n)[2:]  # превращаем в двоичную форму
    index_last_0 = bin_n.rfind("0")  # получаем индекс последнего 0
    if index_last_0 != -1:
        bin_n = bin_n[:index_last_0] + bin_n[:2] + bin_n[index_last_0 + 1:]  # выкидываю ноль и вставляю туда первые два символа
        bin_n = bin_n[::-1]  # переворот
        return bin_n
    else:
        return "0"


for i in range(2, 1000):
    num = int(f(i), 2)
    if num == 127:
        print(i, f(i), num)
