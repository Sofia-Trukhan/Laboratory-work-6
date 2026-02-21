C = ["Хліб", "Молоко", "Сир", "Масло", "Цукор"]
A = [50, 30, 20, 15, 40]
B = [30, 80, 120, 80, 30]

# Загальна вартість
total = 0
for i in range(len(C)):
    total += A[i] * B[i]

# Середня ціна
average = sum(B) / len(B)

# Товар якого найбільше
max = max(A)
index = A.index(max)

print("Загальна вартість товарів:", total)
print("Середня ціна:", average)
print("Найбільше на складі товару:", C[index])
