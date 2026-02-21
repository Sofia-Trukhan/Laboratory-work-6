str_data = "Софія КН-3 Компютерні науки"

# Вивести назву групи
group = str_data.split()[1]
print("Група:", group)

# Замінити ім'я на прізвище
new_str = str_data.replace("Софія", "Трухан")
print("Змінений рядок:", new_str)

# Розподіл по пробілу та кількість слів
words = str_data.split()
print("Кількість слів:", len(words))
