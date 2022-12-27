# Определить позицию второго вхождения строки в списке либо сообщить, что его нет.

# string.find(value, start, end)

# value = 'съешь еще этих французских булок'
value = '1233456789'
print(value)

value2 = '33'
position = value.find(value2)
position2 = value.find(value2, position + 1)

print(position)
print(position2)

if position2 == -1:
    print("Такой позиции нет")
else:
    print("Позиция", position2)
