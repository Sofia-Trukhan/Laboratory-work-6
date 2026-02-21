numbers = list(range(1, 11, 1))
print(numbers)

for n in numbers:
    if n % 2 == 0:
        print(f"Число {n} парне, квадрат: {n**2}")
    else:
        print(f"Число {n} непарне, куб: {n**3}")




