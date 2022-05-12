import random
import shutil
import sys
import time

MIN_STREAM_LENGHT = 6
MAX_STREAM_LENGHT = 14
PAUSE = 0.1
STREAM_CHARS = ['0', '1']

DENSITY = 1

WIGTH = shutil.get_terminal_size()[0]
WIGTH -= 1

try:
	columns = [0] * WIGTH
	while True:
		for i in range(WIGTH):
			if columns[i] == 0:
				if random.random() <= DENSITY:
					columns[i] = random.randint(MIN_STREAM_LENGHT, MAX_STREAM_LENGHT)

			elif columns[i] > 0:
				print(random.choice(STREAM_CHARS), end='')
				columns[i] -= 1
			else:
				print(' ', end='')
			print()
			sys.stdout.flush()
			time.sleep(PAUSE)
except KeyboardInterrupt:
	sys.exit()
