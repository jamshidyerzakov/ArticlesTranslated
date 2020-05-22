def polindrom():
    for number in range(1, 2000):  # 1 dan 2000 gacha bo'lgan sonlar (2000 kirmaydi)
        if str(number) == str(number)[::-1]:  # agar satr teskarisi originaliga teng bo'lsa
            print(number)  # aynan shu sikl takroridagi sonni chiqramiz

# polindrom()


def sum_of_numbers():
    output = 0
    for number in range(1, 1000): # 1 dan 1000 gacha bo'lgan sonlar (1000 kirmaydi)
        if number % 3 == 0 and number % 5 == 0: # 3 va 5 ga bo'linishini tekshirish
            output += number  # yig'indini hisoblash
    return output

# print(sum_of_numbers())


def factorial(n):
    sum_of_factorial = 1
    for number in range(1, n+1):  # n gacha bo'lgan sonlar
        sum_of_factorial = sum_of_factorial * number
    return sum_of_factorial

print(factorial(6))