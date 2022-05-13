import random
import time


def main():
	print("Ready...")
	time.sleep(random.randint(1, 10))
	start = time.time()
	input('DRAW!!!')
	result = time.time() - start
	print(result)
	if result < 0.1:
		print("You drew before \"DRAW\" appeared! You lose.")
	elif 0.1 < result < 0.7:
		print("WOW! Nice shoot!")
	else:
		print("To slow... Try again")


main()
