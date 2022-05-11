import copy, random, sys, time

# Задаем константы:
WIDTH = 79 # Ширина сетки клеток.
HEIGHT = 20 # Высота сетки клеток.

# (!) Попробуйте заменить значение ALIVE на '#' или другой символ:
ALIVE = 'O' # Символ, соответствующий живой клетке.
# (!) Попробуйте заменить значение DEAD на '.' или другой символ:
DEAD = ' ' # Символ, соответствующий мертвой клетке.
# (!) Попробуйте заменить значение ALIVE на '|', а DEAD на '-'.

# cells и nextCells — ассоциативные массивы для хранения состояния игры.

# Роль их ключей играют кортежи (x, y), а значения представляют собой
# одно из значений ALIVE или DEAD.
nextCells = {}
# Вставляем в nextCells случайные живые и мертвые клетки:
for x in range(WIDTH): # Проходим в цикле по всем столбцам.
	for y in range(HEIGHT): # Проходим в цикле по всем строкам.
		# Исходные клетки могут быть живыми или мертвыми с вероятностью 50 %.
		if random.randint(0, 1) == 0:
			nextCells[(x, y)] = ALIVE # Добавляем живую клетку.
		else:
			nextCells[(x, y)] = DEAD # Добавляем мертвую клетку.

while True: # Основной цикл программы.
	# Итерации этого цикла соответствуют шагам моделирования.
	print('\n' * 50) # Разделяем шаги символами новой строки.
	cells = copy.deepcopy(nextCells)

	# Выводим клетки на экран:
	for y in range(HEIGHT):
		for x in range(WIDTH):
			print(cells[(x, y)], end='') # Выводим # или пробел.
		print() # Выводим символ новой строки в конце строки.
	print('Press Ctrl-C to quit.')
	# Вычисляем клетки следующего шага исходя из клеток на текущем шаге:
	for x in range(WIDTH):
		for y in range(HEIGHT):
			# Получаем координаты (x, y) соседних клеток, даже если они
			# выходят за границы:
			left = (x - 1) % WIDTH
			right = (x + 1) % WIDTH
			above = (y - 1) % HEIGHT
			below = (y + 1) % HEIGHT
			# Подсчитываем количество живых соседей:
			numNeighbors = 0
			if cells[(left, above)] == ALIVE:
				numNeighbors += 1 # Сосед вверху слева жив.
			if cells[(x, above)] == ALIVE:
				numNeighbors += 1 # Сосед вверху жив.
			if cells[(right, above)] == ALIVE:
				numNeighbors += 1 # Сосед вверху справа жив.
			if cells[(left, y)] == ALIVE:
				numNeighbors += 1 # Сосед слева жив.
			if cells[(right, y)] == ALIVE:
				numNeighbors += 1 # Сосед справа жив.
			if cells[(left, below)] == ALIVE:
				numNeighbors += 1 # Сосед внизу слева жив.
			if cells[(x, below)] == ALIVE:
				numNeighbors += 1 # Сосед внизу жив.
			if cells[(right, below)] == ALIVE:
				numNeighbors += 1 # Сосед внизу справа жив.

			# Устанавливаем состояние клеток в соответствии с правилами игры
			if cells[(x, y)] == ALIVE and (numNeighbors == 2 or numNeighbors == 3):
				# Живые клетки с двумя или тремя соседями остаются живыми:
				nextCells[(x, y)] = ALIVE
			elif cells[(x, y)] == DEAD and numNeighbors == 3:
				# Мертвые клетки с тремя соседями становятся живыми:
				nextCells[(x, y)] = ALIVE
			else:
				# Все остальные клетки умирают или остаются мертвыми:
				nextCells[(x, y)] = DEAD
	try:
		time.sleep(1) # Добавляем паузу в 1 секунду, чтобы уменьшить мигание.
	except KeyboardInterrupt:
		print("Conway's Game of Life")
		print('By Al Sweigart al@inventwithpython.com')
		sys.exit() # Если нажато Ctrl+C — завершаем программу.