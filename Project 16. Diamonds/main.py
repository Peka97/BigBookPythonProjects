def main():
	# Отображает ромбы размера с 0 по 6:
	for diamondSize in range(0, 6):
		displayOutlineDiamond(diamondSize)
		print() # Выводит символ новой строки.
		displayFilledDiamond(diamondSize)
		print() # Выводит символ новой строки.


def displayOutlineDiamond(size):
	# Отображает верхнюю половину ромба:
	for i in range(size):
		print(' ' * (size - i - 1), end='') # Пробелы слева.
		print('/', end='') # Левая сторона ромба.
		print(' ' * (i * 2), end='') # Внутренность ромба.
		print('\\') # Правая сторона ромба.

	# Отображает нижнюю половину ромба:
	for i in range(size):
		print(' ' * i, end='') # Пробелы слева.
		print('\\', end='') # Левая сторона ромба.
		print(' ' * ((size - i - 1) * 2), end='') # Внутренность ромба.
		print('/') # Правая сторона ромба.


def displayFilledDiamond(size):
	# Отображает верхнюю половину ромба:
	for i in range(size):
		print(' ' * (size - i - 1), end='') # Пробелы слева.
		print('/' * (i + 1), end='') # Левая сторона ромба.
		print('\\' * (i + 1)) # Правая сторона ромба.

	# Отображает нижнюю половину ромба:
	for i in range(size):
		print(' ' * i, end='') # Пробелы слева.
		print('\\' * (size - i), end='') # Левая сторона ромба.
		print('/' * (size - i)) # Правая сторона ромба.


# Если программа не импортируется, а запускается, производим запуск:
if __name__ == '__main__':
	main()