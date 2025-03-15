# Создаем список-фрактал
def create_fractal():
    # Исходный список
    original_list = [1, 1]

    # Формируем фрактал
    global fractal  # Объявляем переменную fractal глобальной
    fractal = [0, original_list, original_list, 2]  # 0 и 2 по краям, оригинальный список дважды между ними


# Вызываем функцию для создания фрактала
create_fractal()

# Выводим результат
print(fractal)
