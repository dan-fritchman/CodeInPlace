
def moon():
    """ Convert your weight on earth to your weight on the moon """ 
    earth_weight_str = input("Your weight on earth: ")
    earth_weight = float(earth_weight_str)
    moon_weight = earth_weight * 0.165
    print("Your moon weight: " + str(moon_weight))


if __name__ == '__main__':
    moon()

