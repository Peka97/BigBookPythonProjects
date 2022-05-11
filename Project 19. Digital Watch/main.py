import time
from datetime import datetime


def format_time(dig):
	row = ['', '', '']
	for num in dig:
		if num == ':':
			row[0] += ' '
			row[1] += '*'
			row[2] += '*'
			continue
		num = int(num)
		if num == 0:
			row[0] += ' __ '
			row[1] += '|  |'
			row[2] += '|__|'
		elif num == 1:
			row[0] += '    '
			row[1] += '   |'
			row[2] += '   |'
		elif num == 2:
			row[0] += ' __ '
			row[1] += ' __|'
			row[2] += '|__ '
		elif num == 3:
			row[0] += ' __ '
			row[1] += ' __|'
			row[2] += ' __|'
		elif num == 4:
			row[0] += '    '
			row[1] += '|__|'
			row[2] += '   |'
		elif num == 5:
			row[0] += ' __ '
			row[1] += '|__ '
			row[2] += ' __|'
		elif num == 6:
			row[0] += ' __ '
			row[1] += '|__ '
			row[2] += '|__|'
		elif num == 7:
			row[0] += ' __ '
			row[1] += '   |'
			row[2] += '   |'
		elif num == 8:
			row[0] += ' __ '
			row[1] += '|__|'
			row[2] += '|__|'
		elif num == 9:
			row[0] += ' __ '
			row[1] += '|__|'
			row[2] += ' __|'
		row[0] += ' '
		row[1] += ' '
		row[2] += ' '
	return ' \n'.join(row)


while True:
	print(format_time(datetime.strftime(datetime.now(), "%I:%M:%S")))
	time.sleep(0.5)
	print(format_time(datetime.strftime(datetime.now(), "%I:%M:%S")).replace('*', ' '))
	time.sleep(0.5)

