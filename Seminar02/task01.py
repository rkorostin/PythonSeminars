# def InputNumbers(inputText):
#     is_OK = False
#     while not is_OK:
#         try:
#             number = int(input(f"{inputText}"))
#             is_OK = True
#         except ValueError:
#             print('Ошибка. Требуется ввод числа')
#     return number

def InputNumbers2(inputText):
    number = input(f"{inputText}")
    if number.isdigit():
        pass
    else:
        print('Ошибка. Требуется ввод числа')

InputNumbers2("Введите число:")