import random
import time
import dices

# Задаем константы:
DICE_WIDTH = 9
DICE_HEIGHT = 5
CANVAS_WIDTH = 79
CANVAS_HEIGHT = 24 - 3  # -3, чтобы было куда ввести сумму внизу

# Длительность в секундах:
QUIZ_DURATION = 30  # (!) Попробуйте заменить это значение на 10 или 60.
MIN_DICE = 2  # (!) Попробуйте заменить это значение на 1 или 5.
MAX_DICE = 6  # (!) Попробуйте заменить это значение на 14.

# (!) Попробуйте заменить эти значения на различные другие:
REWARD = 4  # (!) Очки, полученные за правильные ответы.
PENAltY = 1  # (!) Очки, отнятые за неправильные ответы.
# (!) Попробуйте задать отрицательное значение PENAltY, чтобы давать
# очки за неправильные ответы!

# Если все кости не помещаются на экране, программа зависает:
assert MAX_DICE <= 14


D1 = (['+-------+',
       '|       |',
       '|   O   |',
       '|       |',
       '+-------+'], 1)


D2a = (['+-------+',
        '|     O |',
        '|       |',
        '| O     |',
        '+-------+'], 2)


D2b = (['+-------+',
        '| O     |',
        '|       |',
        '|     O |',
        '+-------+'], 2)


D3a = (['+-------+',
        '|     O |',
        '|   O   |',
        '| O     |',
        '+-------+'], 3)


D3b = (['+-------+',
        '| O     |',
        '|   O   |',
        '|     O |',
        '+-------+'], 3)


D4 = (['+-------+',
       '| O   O |',
       '|       |',
       '| O   O |',
       '+-------+'], 4)


D5 = (['+-------+',
       '| O   O |',
       '|   O   |',
       '| O   O |',
       '+-------+'], 5)


D6a = (['+-------+',
        '| O   O |',
        '| O   O |',
        '| O   O |',
        '+-------+'], 6)


D6b = (['+-------+',
        '| O O O |',
        '|       |',
        '| O O O |',
        '+-------+'], 6)


ALL_DICE = [D1, D2a, D2b, D3a, D3b, D4, D5, D6a, D6b]

print('''Dice Math, by Al Sweigart al@inventwithpython.com

Add up the sides of all the dice displayed on the screen. You have
{} seconds to answer as many as possible. You get {} points for each
correct answer and lose {} point for each incorrect answer.
'''.format(QUIZ_DURATION, REWARD, PENAltY))
input('Press Enter to begin...')

# Отслеживаем количество правильных и неправильных ответов:
correctAnswers = 0
incorrectAnswers = 0
startTime = time.time()
while time.time() < startTime + QUIZ_DURATION:  # Основной цикл игры.
	# Выбираем кость для отображения:
	sumAnswer = 0
	diceFaces = []
	for i in range(random.randint(MIN_DICE, MAX_DICE)):
		die = random.choice(ALL_DICE)
		# die[0] содержит список лицевых сторон костей в виде строк:
		diceFaces.append(die[0])

		# die[1] содержит количество точек на лицевой стороне в виде чисел:
		sumAnswer += die[1]

	# Содержит кортежи (x, y) с местоположением верхнего левого угла кости.
	topLeftDiceCorners = []

	# Определяем, где должна быть размещена кость:
	for i in range(len(diceFaces)):
		while True:
			# Находим случайное место на холсте для размещения кости:
			left = random.randint(0, CANVAS_WIDTH - 1 - DICE_WIDTH)
			top = random.randint(0, CANVAS_HEIGHT - 1 - DICE_HEIGHT)

			# Получаем координаты x, y всех четырех углов:
			# left
			# v
			# top > +-------+ ^
			# | O | |
			# | O | DICE_HEIGHT (5)
			# | O | |
			# +-------+ v
			# <------->
			# DICE_WIDTH (9)
			topLeftX = left
			topLeftY = top
			topRightX = left + DICE_WIDTH
			topRightY = top
			bottomLeftX = left
			bottomLeftY = top + DICE_HEIGHT
			bottomRightX = left + DICE_WIDTH
			bottomRightY = top + DICE_HEIGHT

			# Проверяем, не пересекается ли эта игральная кость с предыдущей.
			overlaps = False
			for prevDieLeft, prevDieTop in topLeftDiceCorners:
				prevDieRight = prevDieLeft + DICE_WIDTH
				prevDieBottom = prevDieTop + DICE_HEIGHT
				# Проверяем все углы этой кости, не входят ли они
				# в область, занимаемую предыдущей костью:
				for cornerX, cornerY in ((topLeftX, topLeftY),
				                         (topRightX, topRightY),
				                         (bottomLeftX, bottomLeftY),
				                         (bottomRightX, bottomRightY)):
					if prevDieLeft <= cornerX < prevDieRight and prevDieTop <= cornerY < prevDieBottom:
						overlaps = True
					if not overlaps:
						# Если не пересекается, можем ее тут разместить:
						topLeftDiceCorners.append((left, top))
						break

	# Отрисовываем кость на холсте:

	# Ключи представляют собой кортежи (x, y) целочисленных значений,
	# значения — символы на соответствующем месте холста:
	canvas = {}
	# Проходим в цикле по всем костям:
	for i, (dieLeft, dieTop) in enumerate(topLeftDiceCorners):
		# Проходим в цикле по всем символам лицевой стороны кости:
		dieFace = diceFaces[i]
		for dx in range(DICE_WIDTH):
			for dy in range(DICE_HEIGHT):
				# Копируем символ в соответствующее место холста:
				canvasX = dieLeft + dx
				canvasY = dieTop + dy
				# Обратите внимание, что в dieFace, списке строковых
				# значений, x и y поменяны местами:
				canvas[(canvasX, canvasY)] = dieFace[dy][dx]

	# Выводим холст на экран:
	for cy in range(CANVAS_HEIGHT):
		for cx in range(CANVAS_WIDTH):
			print(canvas.get((cx, cy), ' '), end='')
			print()  # Выводим символ новой строки.

	# Даем игроку возможность ввести свой ответ:
	response = input('Enter the sum: ').strip()
	if response.isdecimal() and int(response) == sumAnswer:
		correctAnswers += 1
	else:
		print('Incorrect, the answer is', sumAnswer)
		time.sleep(2)
		incorrectAnswers += 1

	# Отображаем итоговый счет:
	score = (correctAnswers * REWARD) - (incorrectAnswers * PENAltY)
	print('Correct: ', correctAnswers)
	print('Incorrect:', incorrectAnswers)
	print('Score: ', score)
