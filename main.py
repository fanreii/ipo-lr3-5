number = int(input("Введите целое число: ")) # ввод числа с клавиатуры
absolute_value = number if number >= 0 else -number # тернарное выражение 
print("Абсолютное значение:", absolute_value) # вывод результата 