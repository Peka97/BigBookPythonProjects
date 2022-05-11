def main():
	start_num = int(input("Введите число:\n >:"))
	result = [start_num]
	num = result[-1]
	while num != 1:
		if num % 2 == 0:
			num = num / 2
		elif num % 2 != 0:
			num = num * 3 + 1
		result.append(int(num))
	print(result)


main()
