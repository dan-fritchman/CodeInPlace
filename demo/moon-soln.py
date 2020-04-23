

def moon():
	earth_weight_str = input("Enter your weigh on earth: ")
	earth_weight = float(earth_weight_str)
	MOON_MULTIPLE = 0.165
	moon_weight = earth_weight * MOON_MULTIPLE
	print("Your weight on the moon ==> " + str(moon_weight))

if __name__ == '__main__':
	moon()

