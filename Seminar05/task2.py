# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность.
# Порядок элементов менять нельзя.

# *Пример: *

# [1, 5, 2, 3, 4, 6, 1, 7] = > [1, 2, 3, 4, 6, 7]

def get_sequence_list(lst1, lst2):
    for i in range(len(lst1)):
        if lst1[i] == max(lst1[:i + 1:]) and lst1[i] not in lst2:
            lst2.append(lst1[i])
    return lst2


a_list = [10, 9, 11, 8, 7, 6, 5, 4, 1]
b_list = []
print(a_list)

b_list = get_sequence_list(a_list, b_list)

while len(b_list) == 1:
    b_list.clear()
    a_list.pop(0)
    b_list = get_sequence_list(a_list, b_list)

if len(b_list) == 0:
    print("Возрастающей последовательности нет")
else:
    print(b_list)
