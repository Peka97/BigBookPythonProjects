import random
import re


class Fallout:
	sign = '!@#$%^&*(){}[]-=_+"№;'
	words = ["REFUGEE", "PENALTY", "CHICKEN", "ADDRESS", "DESPITE", "IMPROVE", "DISPLAY", "FOOTAGE", "FROGMAN",
	         "FORTEAN", "ARCOSIN", "ADAMANT", "ALABAMA", "BALISTA", "BELLBOY", "CHARTER", "CALVARY", "DAWNING",
	         "DECODER", "DEFENCE"]
	result = []
	txt = ''
	attempt = 4
	secret = ''
	player_choose = ''

	def gen_words(self):
		"""Генерирует паттерн кода со словом или без"""
		random.shuffle(self.words)
		signs = ''
		rand = random.randint(0, 1)
		if rand == 0:
			for _ in range(9):
				signs += random.choice(self.sign)
			idx = random.randint(0, 5)
			return f"{signs[:idx]}{self.words.pop()}{signs[idx:]}"
		else:
			for _ in range(16):
				signs += random.choice(self.sign)
			return f"{signs}"

	def gen_code(self):
		"""Выводит код на экран"""
		for i in range(1, 10):
			self.result.append(
				f'0x11{i * 10} {Fallout.gen_words(self)} '
				f'0x12{i * 10} {Fallout.gen_words(self)} '
				f'0x13{i * 10} {Fallout.gen_words(self)}')
		for el in self.result:
			self.txt += f'{el}\n'
		return self.txt

	def attempts(self):
		"""Рисует █ в количестве attempts класса"""
		result = ""
		for _ in range(self.attempt):
			result += ' █'
		return result

	def start_game(self):
		"""Запуск игры. Принимает буквенный пароль из 7 заглавных букв. За каждую попытку ввода отнимает единицу
		из параметра attempts. В случае победы или проигрыша код завершается"""
		r = re.compile('\w{7}')
		try:
			self.secret = r.findall(random.choice(self.result))[0]
		except IndexError:
			self.secret = r.findall(random.choice(self.result))[0]
		print(f'{self.attempt} attempts left:{Fallout.attempts(self)}')
		self.player_choose = input("Enter password:\n >:")
		self.attempt -= 1
		while self.attempt:
			if self.player_choose == self.secret:
				print("Right!")
				break
			elif len(self.player_choose) != 7:
				print(f'{self.attempt} attempts left:{Fallout.attempts(self)}')
				self.player_choose = input("Enter password: (invalid password)\n >:")
				self.attempt -= 1
			else:
				x, y = 0, 0
				for i in self.secret:
					if self.player_choose[y] == i:
						x += 1
					y += 1
				print(f'{self.attempt} attempts left:{Fallout.attempts(self)}')
				self.player_choose = input(f"Enter password: ({x} tries remaining)\n >:")
				self.attempt -= 1
		print("The end")


a = Fallout()
print(a.gen_code())
a.start_game()
