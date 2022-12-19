import random

number = random.randrange(100)
print(f"Случайное число через ramdom: {number}")


import datetime

# time = datetime.datetime.now()
# mic_second = datetime.datetime.now().second
# print(time)
# print(mic_second)

num_radn = datetime.datetime.now().microsecond%100

print(f"Случайное число через алгоритм: {num_radn}")