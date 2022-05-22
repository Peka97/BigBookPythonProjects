class Net:
	element_1 = "\\_/"
	element_2 = "/ \\"
	result = ""

	def print_net(self):
		for i in range(20):
			if i % 2 != 0:
				self.result += f"{self.element_1 * 10}\n"
			else:
				self.result += f"{self.element_2 * 10}\n"
		return self.result


a = Net()
print(a.print_net())
