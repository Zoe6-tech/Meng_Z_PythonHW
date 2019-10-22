#look at a temperature and fugure out what state water is in - solid,liquid or gas

#set the temperature first
#and turn our text into a number-int
temp = int(input("enter a temperature :\n"))

if temp <4:
	print("water is frozen - a solid")
elif temp > 4 and temp < 100:
	print("water is a liquid")
elif temp >= 100:
	print("water is  a gas")
