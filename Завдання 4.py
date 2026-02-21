users = ["Mark", "Tom", "Bob", "Alice", "Tom", "Bill", "Tom", "Alex", "Shaun", "Mark"]

print("Tom:", users.count("Tom"))
print("Mark:", users.count("Mark"))
print("Alice:", users.count("Alice"))
print("John:", users.count("John"))

# Видаляємо третій елемент (індекс 2)
users.pop(2)

# Видаляємо один Tom
users.remove("Tom")

print("Оновлений список:", users)
