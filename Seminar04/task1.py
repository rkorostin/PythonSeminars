"""Строка содержит набор чисел. Показать большее и меньшее число
В качестве символа-разделителя используйте пробел.
"""

    string = '1 2 3 4 5 6 7 8 12 54 32 -1 0 -23 5 7'
    print(string)

    list_str = []
    for i in string.split():
        i = int(i)
        list_str.append(i)

    print(max(list_str), min(list_str))

