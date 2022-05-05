def main():
	method = input('(E)ncode or (D)ecode?\n >: ').upper()
	key = int(input('Enter key\n >: '))
	message = input('Enter message\n >: ').upper()
	result = ""
	if method == "E":
		for a in message:
			result += chr(ord(f'{a}') + key)
		print(result)
		del result
	elif method == "D":
		for a in message:
			result += chr(ord(f'{a}') - key)
		print(result)
		del result

main()
