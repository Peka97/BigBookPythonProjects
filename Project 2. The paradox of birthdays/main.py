import random

print("Birthday Paradox, by Al Sweigart al@inventwithpython.com")


class App_Date:
	months = {"Jan": 32, "Feb": 29, "Mar": 32, "Apr": 31,
	          "May": 32, "Jun": 31, "Jul": 32, "Aug": 32,
	          "Sep": 31, "Oct": 32, "Nov": 31, "Dec": 32}
	generate_number = 0
	temp = []
	result = []
	yes = 0

	def start(self):
		self.generate_number = int(input("How many birthdays shall I generate? (Max 100)\n> "))

	def random_date(self):
		if self.generate_number <= 100:
			for _ in range(self.generate_number):
				random_month = str(self.months.keys()).strip("dict_keys()[]").split(", ")[random.randint(0, 11)].strip("'")
				random_number = random.randint(1, self.months[random_month.strip("'")])
				self.temp.append(f'{random_month} {random_number}')
		self.result = self.temp.copy()
		self.temp.clear()
		return self.result

	def is_match(self, func):
		for item in func:
			if func.count(item) > 1:
				return True

	def сalc_statistics(self):
		for n in range(100000):
			if n == 0:
				print(f"{n} simulations run...")
			elif n % 10000 == 0:
				print(f"{n} simulations run...")
			if a.is_match(a.random_date()) is True:
				self.yes += 1
		print(f"""Out of 100,000 simulations of {a.generate_number} people, there was a
	matching birthday in that group {a.yes} times. This means
	that {a.generate_number} people have a {round(a.yes/1000, 2)}% chance of
	having a matching birthday in their group.
	That's probably more than you would think!""")


a = App_Date()
a.start()
a.сalc_statistics()
