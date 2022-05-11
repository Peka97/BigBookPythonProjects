import re
import random


def init_dices():
	cast = input("Enter dices:\n >:")
	RE_CAST = re.compile('\d+\w+([+-]\d+)?')
	if not RE_CAST.match(cast):
		print("Not valid text, try again.")
	amount = int(cast.split('d')[0])
	if '+' in cast:
		facets = int(str(cast.split('d')[1]).split('+')[0])
		bonus = int(cast.split('+')[-1])
		print_cast(amount, facets, bonus)
	elif '-' in cast:
		facets = int(str(cast.split('d')[1]).split('-')[0])
		debonus = int(cast.split('-')[-1])
		print_cast(amount, facets, debonus)
	else:
		facets = int(cast.split('d')[1])
		print_cast(amount, facets)


def print_cast(amount: int, facets: int, bonus=0):
	dices = []
	print(facets)
	for _ in range(amount):
		dices.append(random.randint(1, facets))
	if bonus != 0:
		print(f'({amount}, {dices}, {bonus})')
	else:
		print(f'({amount}, {dices})')
	init_dices()


init_dices()

