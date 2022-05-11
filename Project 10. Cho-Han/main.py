import random


class Game:
	money = 5000
	bet = 0
	x = 0
	y = 0

	def main(self):
		self.bet = int(input(f"Bank: {self.money}. Enter your bet:\n >:"))
		self.x = random.randint(1, 6)
		self.y = random.randint(1, 6)
		answer = input("CHO(even) or HAN(odd)?\n >:").upper()
		print(f"{self.x} | {self.y}")
		if answer == "CHO" and (self.x + self.y) % 2 == 0:
			self.money += self.bet
			input("You WIN! Play again? Y/N\n >:").upper()
			if "Y":
				Game.main(self)
		elif answer == "HAN" and (self.x + self.y) % 2 != 0:
			self.money += self.bet
			input("You WIN! Play again? Y/N\n >:").upper()
			if "Y":
				Game.main(self)
		else:
			self.money -= self.bet
			input("You LOSE! Play again? Y/N\n >:").upper()
			if "Y":
				Game.main(self)

a = Game()
a.main()


