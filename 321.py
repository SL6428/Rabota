import random

while True:
    start = int(input("Введите начальное значение диапазона: "))
    endo = int(input("Введите конечное значение диапазона: "))
    random_number = random.randint(start, endo)
    print(f"Случайное число между {start} и {endo}: {random_number}")
    vixod = int(input("1 - выход, 0 - продолжтть: "))
    if vixod == 0:
        continue
    elif vixod == 1:
        break
        
