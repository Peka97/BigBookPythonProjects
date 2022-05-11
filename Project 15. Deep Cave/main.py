import random, sys, time

# Задаем константы:
WIDTH = 70 # (!) Попробуйте заменить на 10 или 30.
PAUSE_AMOUNT = 0.05 # (!) Попробуйте заменить на 0 или 1.0.
print('Deep Cave, by Al Sweigart al@inventwithpython.com')
print('Press Ctrl-C to stop.')
time.sleep(2)

leftWidth = 20
gapWidth = 10

while True:
# Отображает фрагмент туннеля:
	rightWidth = WIDTH - gapWidth - leftWidth
	print(('#' * leftWidth) + (' ' * gapWidth) + ('#' * rightWidth))
# Проверяем, не нажато ли Ctrl+C, во время короткой паузы:
	try:
		time.sleep(PAUSE_AMOUNT)
	except KeyboardInterrupt:
		sys.exit() # Если нажато сочетание клавиш Ctrl+C — завершаем программу.

	# Подбираем ширину левой части:
	diceRoll = random.randint(1, 6)
	if diceRoll == 1 and leftWidth > 1:
		leftWidth = leftWidth - 1 # Уменьшаем ширину левой части.
	elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
		leftWidth = leftWidth + 1 # Увеличиваем ширину левой части.
	else:
		pass # Ничего не делаем; ширина левой части не меняется
	# Подбираем ширину зазора:
	# (!) Попробуйте раскомментировать весь следующий код:
	diceRoll = random.randint(1, 6)
	if diceRoll == 1 and gapWidth > 1:
		gapWidth = gapWidth - 1 # Уменьшаем.
	elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
		gapWidth = gapWidth + 1 # Увеличиваем ширину зазора.
	else:
		pass # Ничего не делаем; ширина зазора не меняется.