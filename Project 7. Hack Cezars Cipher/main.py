def main():
	message = input('Enter message\n >: ').upper()
	key = 0
	while True:
		result = ""
		key += 1
		for a in message:
			result += chr(ord(f'{a}') - key)
		print(result)
		choice = input('Похоже на правду? Y/N\n >:').upper()
		if choice == "Y":
			break

main()
