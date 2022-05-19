import random

from pics import HANGMAN_PICS as pic


class Gallows:
	WORDS = ["Котенок", "Самолет", "Тракторист", "Супруга", "Компьютер", "Локомотив"]
	idx_pic = 0
	mask = []
	secret = ''
	player_letter = ''
	gallows = ''

	def gen_secret_word(self):
		self.secret = random.choice(self.WORDS).upper()

	def next_print(self):
		self.gallows = pic[self.idx_pic]
		print(self.gallows)
		print(*self.mask)
		self.idx_pic += 1

	def create_mask(self):
		for _ in range(len(self.secret)):
			self.mask.append("_")
		return self.mask

	def update_mask(self):
		for idx, letter in enumerate(self.secret):
			if letter == self.player_letter:
				self.mask[idx] = self.player_letter
		print(*self.mask)

	def valid_letter(self):
		for letter in self.secret:
			if self.player_letter == letter:
				print(self.gallows)
				return True
		Gallows.next_print(self)
		return False

	def start_game(self):
		Gallows.gen_secret_word(self)
		Gallows.create_mask(self)
		Gallows.next_print(self)
		print(*self.secret)
		self.player_letter = input("Enter your letter:\n >:")
		while True:
			print(self.mask.count('_'))
			if self.mask.count('_') == 0:
				print("Rigth")
				break
			elif self.idx_pic == 6:
				Gallows.next_print(self)
				print("You dead!")
				break
			else:
				if Gallows.valid_letter(self):
					Gallows.update_mask(self)
				self.player_letter = input("Enter your letter:\n >:")


a = Gallows()
a.start_game()
