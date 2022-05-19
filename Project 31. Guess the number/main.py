import random


class Game:
	def __init__(self):
		self.secret = random.randint(0, 100)
		self.num = 0
		self.amount = 0

	def guess(self):
		player_choose = int(input('Я загадал число. Какое?\n >:'))
		while player_choose != self.secret:
			if player_choose > self.secret:
				player_choose = int(input('Нет, меньше. Подумай ещё.\n >:'))
				self.amount += 1
			elif player_choose < self.secret:
				player_choose = int(input('Нет, больше. Подумай ещё.\n >:'))
				self.amount += 1

		print(f"Верно! С {self.amount} попытки!")


Game().guess()
