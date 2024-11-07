# Список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Пустые списки для простых и непростых чисел
primes = []
not_primes = []

for i in numbers:
    is_prime = True

    # Проверка делимости только если число больше 1
    if i < 2:
        is_prime = False
    else:
        # Цикл для поиска делителей от 2 до i-1
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break

    # Добавление чисел в зависимости от значения is_prime
    if is_prime:
        primes.append(i)
    else:
        if i != 1:
            not_primes.append(i)

# Вывод списков primes и not_primes
print("Primes:", primes)
print("Not Primes:", not_primes)
