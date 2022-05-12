import random
import time

nucleotides = {1: ['A', 'T'], 2: ['T', 'A'], 3: ['G', 'C'], 4: ['C', 'G']}

ROWS = [
	'         ##',
	'       #{}-{}#',
	'      #{}---{}#',
	'     #{}-----{}#',
	'    #{}------{}#',
	'   #{}------{}#',
	'   #{}-----{}#',
	'    #{}---{}#',
	'    #{}-{}#',
	'      ##',
	'     #{}-{}#',
	'     #{}---{}#',
	'    #{}-----{}#',
	'    #{}------{}#',
	'     #{}------{}#',
	'      #{}-----{}#',
	'       #{}---{}#',
	'         #{}-{}#']

rowIndex = 0

while True:
	time.sleep(0.1)
	if rowIndex == len(ROWS) - 1:
		rowIndex = 0
	else:
		if "{}" not in ROWS[rowIndex]:
			print(ROWS[rowIndex])
			rowIndex += 1
		else:
			rowIndex += 1
			nuc = nucleotides[random.randint(1, 4)]
			print(ROWS[rowIndex].format(nuc[0], nuc[1]))
