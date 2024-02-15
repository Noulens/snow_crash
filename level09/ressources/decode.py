if __name__ == '__main__':
	# /home/user/level09/token
	path = "/home/kali/Desktop/token"
	with open(path, 'rb') as file1:
		encoded_token = file1.read()
	for i in range(len(encoded_token) - 1):
		c = encoded_token[i] - i
		print(chr(c), end='')