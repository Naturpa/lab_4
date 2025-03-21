# Пример 1: Оба выражения дают одинаковый результат
value = 10
addition = 5

# Используем первое выражение
value1 = value + addition  # value1 будет равно 15
print(f"Результат value = value + addition: {value1}")

# Используем второе выражение
value2 = value  # Сохраняем текущее значение
value2 += addition  # value2 будет равно 15
print(f"Результат value += addition: {value2}")

# В данном случае оба выражения дают одинаковый результат

# Пример 2: Разные результаты при работе со списками
list1 = [1, 2, 3]
list2 = list1

# Используем первое выражение
list1 = list1 + [4]  # Создаем новый список [1, 2, 3, 4]
print(f"Результат list1 = list1 + [4]: {list1}")
print(f"list2: {list2}")  # Вывод: [1, 2, 3], не изменился

# Используем второе выражение
list2 += [5]  # Изменяем список, к которому ссылается list2
print(f"Результат list2 += [5]: {list2}")  # Вывод: [1, 2, 3, 5]
