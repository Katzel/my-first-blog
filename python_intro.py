def hi():
	print("Hi there!")
	print("How are you?")

def hi(name):
	if name=="Hola":
		print("Hi Hola!")
	elif name=="Sonja":
		print("Hi Sonja!")
	else:
		print("Hi anonymous!")
hi("Sonja")

def hi(name):
	print("Hola "+name+"!")
hi("Lucy")

girls=["Rachel","Mónica","Phoebe","Hola","Tú"]
def hi(name):
		print("Hi"+name+"!")
girls=["Rachel","Mónica","Phoebe","Hola","Tú"]
for name in girls:
	hi(name)
	print("Next girl")