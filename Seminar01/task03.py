#3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

def inputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f'{inputText}'))
            is_OK = True
        except ValueError:
            print('Ошибка! Введите число')
    return number

numA = inputNumbers('Введите число А:')