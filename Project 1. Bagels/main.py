import random
import re


class Game:
	secret_num = 0
	my_num = ""
	difficult = 0
	sample = re.compile(r'\d{3}')

	def start(self):
		print("""Bagels, a deductive logic game.
		By Al Sweigart al@inventwithpython.com
		I am thinking of a 3-digit number. Try to guess what it is.
		Here are some clues:
		When I say:         That means:
		 Pico                One digit is correct but in the wrong position.
		 Fermi               One digit is correct and in the right position.
		 Bagels              No digit is correct.
		""")

	def set_num(self):
		self.secret_num = random.randint(100, 999)
		print("I have thought up a number.\nYou have 10 guesses to get it.")
		# print(f"Secret num: {self.secret_num}")

	def set_difficult(self):
		difficult = int(input("\nChoose difficult: 0 - Easy, 1 - Medium, 2 - Hard\nEnter digit: "))
		if difficult == 0:
			self.difficult = 20
		elif difficult == 1:
			self.difficult = 10
		elif difficult == 2:
			self.difficult = 5
		print(difficult)

	def is_valid(self):
		return True if self.sample.match(self.my_num) else False

	def game(self):
		attempt = 0
		print(self.difficult)
		while True and attempt < self.difficult:
			attempt += 1
			self.my_num = input(f"Guess #{attempt}:\n")
			if Game.is_valid(self) is not True:
				print(f"Wrong num {self.my_num}. Try again")
			elif int(self.my_num) == int(self.secret_num):
				print("You got it!")
				break
			else:
				str_input_num = str(self.my_num)
				str_secret_num = str(self.secret_num)
				reply = []
				for idx, el in enumerate(str_input_num):
					if el == str_secret_num[idx]:
						reply.append("Fermi")
					elif el in str_secret_num:
						reply.append("Pico")
					elif idx == 2 and reply == []:
						reply.append("Bagels")
				print(*reply)
				del reply



a = Game()
a.start()
a.set_num()
a.set_difficult()
a.game()


matrix = [
	[0, 0]
	[0, 0]
]
