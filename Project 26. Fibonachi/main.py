amount = int(input("Enter amount Fibonachi:\n >: "))


class Fib:
	result = [0, 1]
	temp = 0
	start = 0

	def func(self, num):
		if num == 1:
			return 0
		elif num == 2:
			return self.result
		else:
			while self.start <= num:
				self.temp = self.result[-1] + self.result[-2]
				self.result.append(self.temp)
				self.start += 1
			return self.result


a = Fib()

print(a.func(amount))
