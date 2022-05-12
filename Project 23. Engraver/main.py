import shutil, sys

UP_DOWN_CHAR = chr(9474)  # Символ 9474 — '│'
LEFT_RIGHT_CHAR = chr(9472)  # Символ 9472 — '─'
DOWN_RIGHT_CHAR = chr(9484)  # Символ 9484 —'┌'
DOWN_LEFT_CHAR = chr(9488)  # Символ 9488 — '┐'
UP_RIGHT_CHAR = chr(9492)  # Символ 9492 — '└'
UP_LEFT_CHAR = chr(9496)  # Символ 9496 — '┘'
UP_DOWN_RIGHT_CHAR = chr(9500)  # Символ 9500 — '├'
UP_DOWN_LEFT_CHAR = chr(9508)  # Символ 9508 — '┤'
DOWN_LEFT_RIGHT_CHAR = chr(9516)  # Символ 9516 — '┬'
UP_LEFT_RIGHT_CHAR = chr(9524)  # Символ 9524 — '┴'
CROSS_CHAR = chr(9532)  # Символ 9532 — '┼'

CANVAS_WIDTH, CANVAS_HEIGHT = shutil.get_terminal_size()
CANVAS_WIDTH -= 1
CANVAS_HEIGHT -= 5

canvas = {}
cursorX = 0
cursorY = 0


def getCanvasString(canvasData, cx, cy):
	canvasStr = ''

	for rowNum in range(CANVAS_HEIGHT):
		for columnNum in range(CANVAS_WIDTH):
			if columnNum == cx and rowNum == cy:
				canvasStr += '#'
				continue

			cell = canvasData.get((columnNum, rowNum))
			if cell in (set(['W', 'S']), set(['W']), set(['S'])):
				canvasStr += UP_DOWN_CHAR
			elif cell in (set(['A', 'D']), set(['A']), set(['D'])):
				canvasStr += LEFT_RIGHT_CHAR
			elif cell == set(['S', 'D']):
				canvasStr += DOWN_RIGHT_CHAR
			elif cell == set(['A', 'S']):
				canvasStr += DOWN_LEFT_CHAR
			elif cell == set(['W', 'D']):
				canvasStr += UP_RIGHT_CHAR
			elif cell == set(['W', 'A']):
				canvasStr += UP_LEFT_CHAR
			elif cell == set(['W', 'S', 'D']):
				canvasStr += UP_DOWN_RIGHT_CHAR
			elif cell == set(['W', 'S', 'A']):
				canvasStr += UP_DOWN_LEFT_CHAR
			elif cell == set(['A', 'S', 'D']):
				canvasStr += DOWN_LEFT_RIGHT_CHAR
			elif cell == set(['W', 'A', 'D']):
				canvasStr += UP_LEFT_RIGHT_CHAR
			elif cell == set(['W', 'A', 'S', 'D']):
				canvasStr += CROSS_CHAR
			elif cell == None:
				canvasStr += ' '
		canvasStr += '\n'
	return canvasStr


moves = []
while True:
	print(getCanvasString(canvas, cursorX, cursorY))
	print('WASD keys to move, H for help, C to clear, F to save, or QUIT.')
	responce = input('> ').upper()

	if responce == 'QUIT':
		print('Think for playing')
		sys.exit()
	elif responce == 'H':
		print("Press Enter to return to the programm")
		continue
	elif responce == 'C':
		canvas = {}
		moves.append('C')
	elif responce == 'F':
		with open('filename.txt', 'w', encoding='utf-8') as f:
			f.write(''.join(moves) + '\n')
			f.write(getCanvasString(canvas, None, None))
	for command in responce:
		if command not in ('W', 'A', 'S', 'D'):
			continue
		moves.append(command)

		if canvas == {}:
			if command in ('W', 'S'):
				canvas[(cursorX, cursorY)] = set(['W', "S"])
			elif command in ('A', 'D'):
				canvas[(cursorX, cursorY)] = set(['A', 'D'])

		if command == 'W' and cursorY > 0:
			canvas[(cursorX, cursorY)].add(command)
			cursorY -= 1
		elif command == 'S' and cursorY < CANVAS_HEIGHT - 1:
			canvas[(cursorX, cursorY)].add(command)
			cursorY += 1
		elif command == 'A' and cursorX > 0:
			canvas[(cursorX, cursorY)].add(command)
			cursorX -= 1
		elif command == 'D' and cursorX < CANVAS_WIDTH - 1:
			canvas[(cursorX, cursorY)].add(command)
			cursorX += 1
		else:
			continue

		if (cursorX, cursorY) not in canvas:
			canvas[(cursorX, cursorY)] = set()

		if command == 'W':
			canvas[(cursorX, cursorY)].add('S')
		elif command == 'S':
			canvas[(cursorX, cursorY)].add('W')
		elif command == 'A':
			canvas[(cursorX, cursorY)].add('D')
		elif command == 'D':
			canvas[(cursorX, cursorY)].add('A')
