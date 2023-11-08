# import re


# def count_of_different_elements(from_) -> list:
# 	patterns = [
# 		'\\W+', '[0-9+]',
# 		'[A-Z+]', '[a-z+]']


# 	# count of different symbols (symbols, number, U letters, L latters)
# 	startList = [len(re.findall(pattern, from_)) for pattern in patterns]
# 	lastList = startList.copy()


# 	# distribution
# 	for i in startList:
# 		maxNumber = 0
# 		positionOfMaxNumber = startList.index(max(startList))
# 		positionOfNumber = startList.index(i)
# 		startList.remove(i)

# 		while i < 3:
# 			i += 1
# 			maxNumber -= 1

# 		startList.insert(positionOfNumber,i)
# 		maxNumber += max(startList)
# 		startList.remove(max(startList))
# 		startList.insert(positionOfMaxNumber, maxNumber)

# 	#end
# 	answer = [startList[i]-lastList[i] for i in range(0,4)]

# 	#output
# 	return answer



# if __name__ == '__main__':
# 	print(count_of_different_elements("asdsadasdaEWAed0"))


from datetime import datetime

class KeyWrapper:
	# Values on the unit circle
	loops = (
		(
			{0: "+", 30: "b", 45: ";", 60: "w",
			90: "Z", 120: "r", 135: "x", 150: "o", 
			180: "A", 210: "^", 225: ")", 240: "H",
			270: "3", 300: "y", 315: "n", 330: "i",
			360: "+"}), # Loop 1
		(
			{0: "o", 30: "<", 45: "7", 60: "@",
			90: "q", 120: "L", 135: "1", 150: "e", 
			180: "z", 210: "q", 225: "h", 240: "#",
			270: "8", 300: "4", 315: "s", 330: "$",
			360: "o"}),
		(
			{0: "t", 30: "0", 45: "c", 60: "e",
			90: "*", 120: "a", 135: "i", 150: "j", 
			180: "b", 210: "2", 225: "[", 240: "6",
			270: "2", 300: "P", 315: "-", 330: "g",
			360: "t"}),
		(
			{0: "k", 30: "K", 45: "5", 60: "m",
			90: "u", 120: "!", 135: "=", 150: "1", 
			180: "Q", 210: "n", 225: "U", 240: "T",
			270: "y", 300: "k", 315: "d", 330: "6",
			360: "k"}),
		(
			{0: "{", 30: "j", 45: "\\", 60: "'",
			90: "(", 120: "f", 135: "|", 150: "Y", 
			180: "N", 210: ">", 225: ",", 240: "D",
			270: "9", 300: "0", 315: "d", 330: "l",
			360: "{"}),
		(
			{0: "~", 30: "S", 45: "F", 60: "u",
			90: "v", 120: "_", 135: "p", 150: "v", 
			180: "l", 210: "t", 225: "w", 240: "W",
			270: "E", 300: "g", 315: "G", 330: "M",
			360: "~"}),
		(
			{0: "J", 30: "x", 45: "h", 60: ":",
			90: "O", 120: "z", 135: "B", 150: "I", 
			180: "V", 210: "}", 225: "C", 240: "a",
			270: "f", 300: "]", 315: "8", 330: "X",
			360: "J"}),
		(
			{0: "9", 30: "s", 45: "r", 60: "`",
			90: ".", 120: "7", 135: "m", 150: '"', 
			180: "c", 210: "/", 225: "&", 240: "p",
			270: "R", 300: "?", 315: "%", 330: "4",
			360: "9"})
	)


	def __init__(self, phrase):
		self.phrase = phrase
		self.unique = len(set(phrase))


	@staticmethod
	def __f(x):
		"""Return the numbers of degrees"""
		return x - (x // 360) * 360 

	@staticmethod
	def __get_n():
		data = datetime.now()
		return abs((data.hour + data.minute) * data.isoweekday())


	def __get_aiv(self) -> tuple:
		"""
		Return all independent variables
		unique, length, missing(-)/overage(+), n, hour, minute, weekday
		"""
		length = len(self.phrase)
		misover = length - 16
		return self.unique, misover, self.__get_n(), 

	def __get_vfl(self, degree, loop):
		"""Get value from loop"""
		nearest_degree = min(self.loops[loop].keys(), key=lambda x: abs(x - degree))
		return self.loops[loop][nearest_degree]


	def encode(self):
		# 	return set([self.__get_vfl(self.__f(x * n), n % 8) for x in map(ord, self.phrase)])
		n = self.__get_n()

		if n > 8: n %= 8 
		vfl_values = set()

		for x in map(ord, self.phrase):
			vfl_values.add(self.__get_vfl(self.__f(x * n), n))

		return vfl_values


	def decode(self):
		...


	def __del__(self):
		pass


def main():
	phrase = input("keywrapper> ")
	wrapper = KeyWrapper(phrase)
	print(wrapper.encode())


if __name__ == "__main__":
	main()