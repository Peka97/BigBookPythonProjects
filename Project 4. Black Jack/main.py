import copy
import random
import time


class Game:
	dealer_score = 0
	player_score = 0
	game = True
	player_first_card = ['backside']
	player_second_card = ['backside']
	dealer_first_card = ['backside']
	dealer_second_card = ['backside']
	symbol = ["♠", "♣", "♣", "♦"]
	money = 5000
	bet = 0

	def get_deck(self):
		num = random.randint(2, 14)
		if num < 11:
			pass
		else:
			if 11 < num < 15:
				num = 10
			elif num == 11:
				if self.player_score + 11 > 21:
					num = 1
				else:
					num = 11
		self.player_score += num
		Game.show_card(self, num, "player")

	def dealer_game(self):
		num = random.randint(2, 14)
		if num < 11:
			pass
		else:
			if 11 < num < 15:
				num = 10
			elif num == 11:
				if self.player_score + 11 > 21:
					num = 1
				else:
					num = 11
		self.dealer_score += num
		Game.show_card(self, num, "dealer")

	def start(self):
		self.player_score = 0
		self.dealer_score = 0
		self.bet = int(input("Укажите ставку\n >:"))
		Game.dealer_game(self)
		for _ in range(2):
			Game.get_deck(self)
		print(f"DEALER: {self.dealer_score}")
		print(f"PLAYER: {self.player_score}")
		Game.action(self)

	def again(self):
		if self.money < 100:
			print("Ты нищий! У тебя совсем мало денег")
		var = input(f"Конец игры.\n Сумма ваших денег: {self.money}.\nМожет ещё партию? Y/N\n >:")
		if var == "N":
			print("===================")
			print("Окей, возвращайся снова!")
			print("===================")
		elif var == "Y":
			print("===================")
			print("Отлично!")
			print("===================")
			self.game = True
			Game.start(self)

	def action(self):
		while self.game:
			if self.player_score == 21:
				print("PLAYER is Win!")
				self.money += self.bet
				self.game = False
				break
			text = input("Ваше действие: D - взять ещё карту, P - спасовать\n > :")
			if text == "D":
				print("===================")
				print("Окей, держи карту")
				print("===================")
				time.sleep(2)
				Game.get_deck(self)
				print("===================")
				print(f"DEALER: {self.dealer_score}")
				print(f"PLAYER: {self.player_score}")
				print("===================")
				if self.player_score > 21:
					print(f"{self.player_score} || Перебор || DEALER is Win!")
					self.money -= self.bet
					self.game = False
			elif text == "P":
				while True:
					if self.player_score == self.dealer_score:
						print("===================")
						print("Ничья!")
						print("===================")
						self.game = False
						break
					elif self.dealer_score > 21:
						print(f"{self.dealer_score} || Перебор || PLAYER is Win!")
						self.money += self.bet
						self.game = False
						break
					elif self.dealer_score > self.player_score:
						print(f"Ха-ха, я выиграл!")
						print("DEALER is Win!")
						self.money -= self.bet
						self.game = False
						break
					print("===================")
					print("Окей. Тяну карту")
					print("===================")
					time.sleep(2)
					Game.dealer_game(self)
					print("===================")
					print(f"DEALER: {self.dealer_score}")
					print(f"PLAYER: {self.player_score}")
					print("===================")
		print("THE END")
		self.player_score = 0
		self.dealer_score = 0
		self.player_second_card = ['backside']
		self.player_first_card = ['backside']
		self.dealer_first_card = ['backside']
		self.dealer_second_card = ['backside']
		Game.again(self)

	def show_card(self, num, name):
		if name == "dealer":
			sample = ['', '', '', '']
			sample[0] += " ___ "
			sample[1] += "|## |"
			sample[2] += "|###|"
			sample[3] += "|_##|"
			self.dealer_second_card = copy.copy(sample)
			sample = ['', '', '', '']
			idx_sym = random.randint(0, 3)
			sym = self.symbol[idx_sym]
			sample[0] += " ___"
			if num == 10:
				nums = ['J', 'Q', 'K']
				idx = random.randint(0, 2)
				num = nums[idx]
			elif num == 1 or num == 11:
				num = "A"
			if len(str(num)) > 1:
				sample[1] += f"|{num} |"
				sample[2] += f"| {sym} |"
				sample[3] += f"|_{num}|"
			else:
				sample[1] += f"|{num}  |"
				sample[2] += f"| {sym} |"
				sample[3] += f"|__{num}|"
			self.dealer_first_card = copy.copy(sample)
			print("DEALER CARDS:")
			for row_1, row_2 in zip(self.dealer_second_card, self.dealer_first_card):
				print(row_1, row_2)
		elif name == "player":

			sample = ['', '', '', '']

			idx_sym = random.randint(0, 3)
			sym = self.symbol[idx_sym]
			sample[0] += " ___ "
			if num == 10:
				nums = ['J', 'Q', 'K']
				idx = random.randint(0, 2)
				num = nums[idx]
			elif num == 1 or num == 11:
				num = "A"
			if len(str(num)) > 1:
				sample[1] += f"|{num} |"
				sample[2] += f"| {sym} |"
				sample[3] += f"|_{num}|"
			else:
				sample[1] += f"|{num}  |"
				sample[2] += f"| {sym} |"
				sample[3] += f"|__{num}|"
			self.player_second_card = copy.copy(self.player_first_card)
			self.player_first_card = copy.copy(sample)
			if 'backside' not in self.player_second_card:
				print("PLAYER CARDS:")
				for row_1, row_2 in zip(self.player_second_card, self.player_first_card):
					print(row_1, row_2)


a = Game()
a.start()


