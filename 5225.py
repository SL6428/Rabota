import random

start = int(input("Введите начальное значение диапазона: "))
endo = int(input("Введите конечное значение диапазона: "))

random_number = random.randint(start, endo)
print(f"Случайное число между {start} и {endo}: {random_number}")
