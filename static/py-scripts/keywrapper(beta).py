from datetime import datetime

class KeyWrapper:
	# Values on the unit circle
	loops = (
		(
			{0: "a", 30: "", 45: "", 60: "",
			90: "", 120: "", 135: "", 150: "", 
			180: "", 210: "", 225: "", 240: "",
			270: "", 300: "", 315: "", 330: "",
			360: ""}), # Loop 1
		(
			{0: "a", 30: "", 45: "", 60: "",
			90: "", 120: "", 135: "", 150: "", 
			180: "", 210: "", 225: "", 240: "",
			270: "", 300: "", 315: "", 330: "",
			360: ""}),
		(
			{0: "a", 30: "", 45: "", 60: "",
			90: "", 120: "", 135: "", 150: "", 
			180: "", 210: "", 225: "", 240: "",
			270: "", 300: "", 315: "", 330: "",
			360: ""}),
		(
			{0: "a", 30: "", 45: "", 60: "",
			90: "", 120: "", 135: "", 150: "", 
			180: "", 210: "", 225: "", 240: "",
			270: "", 300: "", 315: "", 330: "",
			360: ""}), # ...
		(
			{0: "a", 30: "", 45: "", 60: "",
			90: "", 120: "", 135: "", 150: "", 
			180: "", 210: "", 225: "", 240: "",
			270: "", 300: "", 315: "", 330: "",
			360: ""}),
		(
			{0: "a", 30: "", 45: "", 60: "",
			90: "", 120: "", 135: "", 150: "", 
			180: "", 210: "", 225: "", 240: "",
			270: "", 300: "", 315: "", 330: "",
			360: ""}),
		(
			{0: "a", 30: "", 45: "", 60: "",
			90: "", 120: "", 135: "", 150: "", 
			180: "", 210: "", 225: "", 240: "",
			270: "", 300: "", 315: "", 330: "",
			360: ""}),
		(
			{0: "a", 30: "", 45: "", 60: "",
			90: "", 120: "", 135: "", 150: "", 
			180: "", 210: "", 225: "", 240: "",
			270: "", 300: "", 315: "", 330: "",
			360: ""})) # Loop 8


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

	def __get_vfl(self, degree, loop):
		"""Get value from loop"""
		loop = self.loops[loop]
		if (0 <= degree and degree < 90):
			return loop
		elif (90 <= degree and degree < 180):
			return loop
		elif (180 <= degree and degree < 270):
			return loop
		elif (270 <= degree and degree < 360):
			return loop


	def encode(self):
		n = self.__get_n()

		if n > 8:
			return [self.__get_vfl(self.__f(x * n), n % 8) for x in map(ord, self.phrase)]

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