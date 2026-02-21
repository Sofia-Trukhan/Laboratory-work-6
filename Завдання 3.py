numbers = [-10, 5, 20, -3, 7, -8, 15, -1, 9, -12,
           4, -6, 11, -14, 18, -2, 6, -9, 13, -4,
           2, -7, 16, -11, 8]

A1 = []
A2 = []

for num in numbers:
    if num > 0:
        A1.append(num)
    if num < 0:
        A2.append(num)

print("Додатні:", A1)
print("Від'ємні:", A2)

