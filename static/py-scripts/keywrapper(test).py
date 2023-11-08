from datetime import datetime
from time import sleep

def radioactive_decay_method(t:str, l:int) -> str:
	if 32 <= int(t, 2) <= 126:
		return chr(int(t, 2))
	# elif int(t, 2) < 32:
	# 	return f"{int(t, 2)} < 32"
	# elif len(t) <= 0:
	# 	return f"{t} <= 0"

	# try:
	t = str(max(int(t[:l+1]), int(t[l+1:])))
	# print(f"t: {t}, l: {l}")
	# except ValueError:
	# 	t = str(int(t[:l]))

	return radioactive_decay_method(t, int(l // 1.4))



def get_data():
	phrase = input(">")
	l = len(phrase)
	lis = []

	if l < 16:
		while len(phrase) < 16:
			unique = len(set(phrase))
			nt = l + 1

			date = datetime.now()
			t = int(f"{date.hour}{date.minute}") * date.second
			bin_t = str(bin(t))[2:]
			print(f"unique: {unique}\nl: {l}\nnt: {nt}\nt: {t}\nbin t: {bin_t}")

			bin_l = len(bin_t)

			if bin_l < len(bin_t):
				l -= len(bin_t) - bin_l

			new_letter = radioactive_decay_method(bin_t, l-1)
			phrase += new_letter
			lis.append(new_letter)
			sleep(1)

	elif l > 16:
		pass

	print(lis, phrase)

if __name__ == "__main__":
	get_data()
