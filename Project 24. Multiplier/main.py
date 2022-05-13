import math

digit = int(input('Enter your digit:\n >:'))


def main(dig):
	result = []
	for i in range(1, int(math.sqrt(dig)+1)):
		if dig % i == 0:
			x = dig // i
			result.append((i, x))
	result = set(result)
	print(result)


main(digit)
