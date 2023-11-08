from re import findall
import random
from datetime import datetime
from string import punctuation, ascii_letters, digits
from math import floor

from sympy import *
from perlin_noise import PerlinNoise
import numpy as np
# import matplotlib.pyplot as plt

import tables


class Gen:
	def __init__(self, name=None):
		self.name = name
		self.strucures = {
			"adenin": self.__adenin(),
			"thymine": self.__thymine(),
			"cytosine":self.__cytosine(),
			"guanine": self.__guanine()
		}
		self.strucure = self.strucures[name]

	def __code_NH(self, rev=False, coef=(1,1)):
		pass


	def __code_HC(self, rev=False, coef=(1,1)):
		pass

	# Generating strucures
	def __adenin(self):
		pass

	def __thymine(self):
		pass

	def __cytosine(self):
		pass

	def __guanine(self):
		pass


	def __del__(self):
		pass


class DNK:
	def __init__(self):
		"""
		Bonds: A-T, C-G
		"""
		self.name = None
		# H*1, O*8, N*7, C*6
		self.blocks = (None, None, None, None)

	def __branch(self):
		pass


	def hydrogen_bond(self):
		pass


	def get_chain(self, word:str):
		key_binary = "".join('{:08b}'.format(ord(i)) for i in word)
		nucleotids = [key_binary[i:i + 8] for i in range(0, 128, 8)]
		print(key_binary)
		print(nucleotids)


	def __del__(self):
		pass


class ImproveKey:
	seed = int(str(datetime.today())[11:13])
	octaves = int(datetime.isoweekday(datetime.today()))
	days = {1:'Mo', 2:'Tu', 3:'We', 4:'Th', 5:'Fr', 6:'St', 7:'Sn',}

	def __init__(self, imperfect:str):
		self.imperfect = imperfect
		self.needAmount = []


	def equalization(self) -> list:
		"""
		This function receives an imperfect key 
		from which it makes a list with the number of characters
		"""

		patterns = [
			'\\W+', '[0-9+]',
			'[A-Z+]', '[a-z+]']


		# count of different symbols (symbols, number, U letters, L latters)
		startList = [len(findall(pattern, self.imperfect)) for pattern in patterns]
		lastList = startList.copy()


		# distribution
		for i in startList:
			maxNumber = 0
			positionOfMaxNumber = startList.index(max(startList))
			positionOfNumber = startList.index(i)
			startList.remove(i)

			while i < 3:
				i += 1
				maxNumber -= 1

			startList.insert(positionOfNumber,i)
			maxNumber += max(startList)
			startList.remove(max(startList))
			startList.insert(positionOfMaxNumber, maxNumber)

		# get equalization
		answer = [startList[i]-lastList[i] for i in range(0,4)]

		return answer


	def getRepElem(self, table:str, line:str, column:str) -> tuple:
		line, column = floor(line),floor(column)
		if table == 'symbols': return tables.symbolsTable[line][column]
		elif table == 'numbers': return tables.numbersTable[line][column]
		elif table == 'letterU' : return tables.lettersUTable[line][column]
		else: return tables.lettersLTable[line][column]


	def searchWithPerlin(self, needElementCount:int, point:str) -> list:
		"""
		function generates perlin noise on base seed (current time) and octaves (current date)

		"""

		if needElementCount < 0: return {point:needElementCount} # if replaceable elements
		
		#Perlin Noise
		positionPattern = {
			'symbols':[8, 4],
			'numbers':[5, 2],
			'letterU':[4, 6],
			'letterL':[4, 6]}


		perlinNoise = PerlinNoise(octaves=self.octaves, seed=self.seed) 
		xpix, ypix = positionPattern[point][0], positionPattern[point][1] # size
		noise = [[perlinNoise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)] # create noice 
		strPositions = [[f"{noise.index(i)}.{i.index(j)}" for j in i] for i in noise] # string representations of element positions in the noise matrix 
		# for i in noise:
		# 	for j in i:
		# 		if j < -0.01:tree.append(f"{noise.index(i)}.{i.index(j)}")
		# plt.imshow(noise, cmap='gray')
		# plt.show()

		# if not empty
		listOfPosition, newCharactersList = strPositions[:needElementCount], []
		if len(listOfPosition) > 0:
			newCharactersList = [self.getRepElem(point, i[0], i[2]) for i in listOfPosition]
			for i in listOfPosition:
				newCharactersList.append(self.getRepElem(point, i[0], i[2])) # getting new characters through the "getRepElem" function

		# overflow check 
		while len(newCharactersList) > needElementCount:
			newCharactersList.pop()

		return newCharactersList


	def findNecessaryElem(self) -> list:
		needAmount = self.equalization() 
		print(needAmount, self.imperfect)
		passwordConsistOf = {
			'symbols': [needAmount[0], []],
			'numbers': [needAmount[1], []],
			'letterU': [needAmount[2], []],
			'letterL': [needAmount[3], []]
		}
			
		# fills list "passwordConsistOf" values from imperfect key 
		for count, char in enumerate(self.imperfect):
			if char.isdigit():
				passwordConsistOf['numbers'][1].append({char: count})
			elif char.islower():
				passwordConsistOf['letterL'][1].append({char: count})
			elif char.isupper():
				passwordConsistOf['letterU'][1].append({char: count})
			else:
				passwordConsistOf['symbols'][1].append({char: count})

		tableNames = passwordConsistOf.keys()
		result = [self.searchWithPerlin(passwordConsistOf[_][0], _) for _ in tableNames]

		return result


	def findThisElem(self, listOfData:list, passwordNF:str) -> list:
		word = [i for i in listOfData]
		count = listOfData[word[0]]
		print("findThisElem", word, count)
		print(word[0] == 'letterU')

		if word[0] == 'letterL': 
			result = [i for i in passwordNF if i.islower()]
		elif word[0] == 'numbers': 
			result = [i for i in passwordNF if i.isdigit()]
		elif word[0] == 'letterU': 
			result = [i for i in passwordNF if i.isupper()]
		else: 
			result = [i for i in passwordNF if i in punctuation]

		return result[:abs(count)]#caesarCipher(abs(count), word)
		# return result


	def REPLACE_(self, firstRep, secondRep, phrase) -> str:
		# end, firstRepLis = {}, []
		end, firstRepLis = [[], []], []
		
		# firstRepLis = [[j for j in i] for i in firstRep]
		for i in firstRep:
			for j in i:
				firstRepLis.append(j)

		# for i in range(len(firstRepLis)):
		# 	end[secondRep[i]] = firstRepLis[i]

		for i in range(len(firstRepLis)):
			end[0].append(secondRep[i])
			end[1].append(firstRepLis[i])


		# [self.imperfect.replace(str(i), str(j), 1) for i, j in end.items()]
		for _ in range(len(firstRepLis)):
			print(str(end[0][_]), str(end[1][_]))
			self.imperfect = self.imperfect.replace(str(end[0][_]), str(end[1][_]), 1)


		return f'{phrase}:{self.seed}{self.days[self.octaves]}\n{self.imperfect}'


	def improve_key(self, text):
		replaceableList = self.findNecessaryElem()
		replacingList = []

		for i in replaceableList:
			if type(i) == dict:
				replacingList = self.findThisElem(
					replaceableList[replaceableList.index(i)],
					self.imperfect)
				replaceableList.remove(i)

		print("r", replaceableList)
		print(replacingList)
				
		return self.REPLACE_(firstRep=replaceableList, secondRep=replacingList, phrase=text)


class BunchOfKeys:
	def __init__(self, text:str = "", additional_part:str = "Empty"):
		self.text = text
		self.apart = additional_part


	def __Key(self, asco:int, uk:int) -> str:
		"""
		First step of password generation
		"""

		if isprime(asco): asco += uk
		else: asco -= uk            

		if asco > 126: asco -= (uk*2) - (asco - 126)
		elif asco < 32: asco += (uk*2) + (asco + 32)

		return chr(asco)


	def __create_password(self):
		unique = len(set(self.text)) # Unique Key
		acsiiCode = [ord(str(_)) for _ in self.text] #convert into acsii
		key = ''.join([self.__Key(i, unique) for i in acsiiCode]) # create imperfect key
		decrypt_password = 0#ImproveKey(self.__key).decode_word(self.text)

		password = ImproveKey(key).improve_key(self.text)	
		return password	



	def __decrypt_password(self):
		return "soon"
		# raise NotImplementedError("Тело функции не реализовано")


	def get_password(self, word):
		print("crypt")
		self.text = word
		return self.__create_password()
		# raise NotImplementedError("Тело функции не реализовано")


	def show_password(self, word):
		print("decrypt")
		self.text, self.apart = word[:16], word[17:]
		
		return self.__decrypt_password()


	def start_action(self, word):
		lenght = len(word)

		if lenght < 16: return "Not enough characters"
		elif self.method == "crypt" and lenght == 16: return self.get_password()
		else: return self.show_password()


	def __del__(self): pass


# default list of imports
__all__ = ["BunchOfKeys"]	