# from bk import BunchOfKeys
# from mbs import Manager


# class InBunch:
# 	def __init__(self, word, method="crypt"):
# 		self.word = word
# 		self.method = method


# 	def get_password(self):
# 		bunch = BunchOfKeys(self.word)

# 		return bunch.create_password()


# 	def show_password(self):
# 		bunch = BunchOfKeys(self.word[:16], self.word[17:])
		
# 		return bunch.decrypt_password()


# 	def start_action(self):
# 		lenght = len(self.word)

# 		if lenght < 16: return "Not enough characters"
# 		elif self.method == "crypt" and lenght == 16: return self.get_password()
# 		else: return self.show_password()


# 	def __del__(self): pass


# class PrivateBank:
# 	def __init__(self):pass

# 	def get_vizualization(self):
# 		# df = pd.DataFrame({
# 		# 	"Date": ["22-01-22", "22-01-23", "22-01-24", "22-01-25", "22-01-26"],
# 		# 	"Amount": [530, 590, 1230, 1250, 1180],
# 		# 	"Neccessary":[100, 130, 400, 410, 340],
# 		# 	"Uneccessary":[30, 42, 190, 194, 194],
# 		# 	"Storage":[400, 418, 640, 646, 194],
# 		# })

# 		# fig = plt.figure()
# 		# sns.pie(data=df)
# 		# sns.set_style("darkgrid")
# 		# plt.show()
# 		fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# 		recipe = ["225 g flour",
# 				  "90 g sugar",
# 				  "1 egg",
# 				  "60 g butter",
# 				  "100 ml milk",
# 				  "1/2 package of yeast"]

# 		data = [225, 90, 50, 60, 100, 5]

# 		wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

# 		bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
# 		kw = dict(arrowprops=dict(arrowstyle="-"),
# 				  bbox=bbox_props, zorder=0, va="center")

# 		for i, p in enumerate(wedges):
# 			ang = (p.theta2 - p.theta1)/2. + p.theta1
# 			y = np.sin(np.deg2rad(ang))
# 			x = np.cos(np.deg2rad(ang))
# 			horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
# 			connectionstyle = f"angle,angleA=0,angleB={ang}"
# 			kw["arrowprops"].update({"connectionstyle": connectionstyle})
# 			ax.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
# 						horizontalalignment=horizontalalignment, **kw)

# 		ax.set_title("Matplotlib bakery: A donut")
# 		plt.savefig('saved_figure.png')
# 		plt.show()

# 	def __del__(self): pass


# # default list of imports
# __all__ = ["InBunch", "PrivateBank"]