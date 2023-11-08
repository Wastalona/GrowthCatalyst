class BunchOfKeys:
	def __init__(self) -> None:
		self.gens = {"0": "N", "1": "l", "2": "S", "3": "L"}
		self.unipolarity = {"0": "1", "1": "0", "2": "3", "3": "2"}
		self.name = None
		"""
		A - numbers 48-57
		T - letters lw 97 - 122
		C - symbols 32-47 && 58-64 && 91-96 && 123-126 (00100000, 00101111)
		G - letters up 65-90
		"""
		self.encrypt_dict = {
			"0": (48, 57), 
			"1": (97, 122), 
			"2": ((32, 47),  (58, 64), (91, 96)), 
			"3": (65, 90)}


	@staticmethod
	def binary_to_quaternary(binary_num: str) -> str:
		decimal_num = int(binary_num, 2)
		quaternary_num = ""
		while decimal_num > 0:
			remainder = decimal_num % 4
			quaternary_num = str(remainder) + quaternary_num
			decimal_num //= 4
		return quaternary_num

	@staticmethod
	def XOR(a: str, b: str) -> str:
		return (bin(int(a, 2) ^ int(b, 2))[2:]).zfill(8)

	def __species_definition(self, value: str) -> str:
		quaternary_block = self.binary_to_quaternary(value)
		return "".join([i for i in quaternary_block]).zfill(4)

	def __reverse_acid(self, acids: str) -> str:
		return "".join([self.unipolarity[acid] for acid in acids])

	def __inElem(self, addPart, value, class_range_len, l_lim, mode=1):
		value = int(value, 2)
		if mode:
			return ( (addPart + value) // class_range_len + l_lim ), (value % class_range_len) + addPart 
		else:
			return ( (addPart**2 + value) // class_range_len + l_lim ), (value % class_range_len)

	def get_chain(self, word: str, key: int=None) -> str:
		print(f"word: {word}\nkey: {key}")

		key_binary = "".join('{:08b}'.format(ord(i)) for i in word)
		proteins = [key_binary[i:i + 8] for i in range(0, 128, 8)]
		oct_blocks = [self.__species_definition(protein) for protein in proteins[:8]]
		acid_left = "".join([i for i in oct_blocks])
		acid_right = self.__reverse_acid(acid_left)

		left = {"0": proteins[0], "1": proteins[1], "2": proteins[2], "3": proteins[3]}
		right = {"0": proteins[4], "1": proteins[5], "2": proteins[6], "3": proteins[7]}
		left = [left[i] for i in acid_left]
		right = [right[i] for i in acid_right]

		res, a = [], 0
		for x, j in zip(left, acid_left):
			if j == "2":
				l, h = self.encrypt_dict[j][key]
			else:
				l, h = self.encrypt_dict[j]
			n = h - l
			x, a = self.__inElem(a, x, n, l)
			res.append(x)
		first = "".join([chr(i) for i in res])

		res, a = [], 0
		for x, j in zip(right, acid_right):
			if j == "2":
				l, h = self.encrypt_dict[j][key]
			else:
				l, h = self.encrypt_dict[j]
			n = h - l
			x, a = self.__inElem(a, x, n, l)
			res.append(x)
		second = "".join([chr(i) for i in res])

		return first, second

	def get_password(self, text:str):
		return "Soon"