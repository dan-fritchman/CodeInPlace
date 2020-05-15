# Data comes from Johns Hopkins Univeristy. Thanks to them for making this public!
# https://github.com/CSSEGISandData/COVID-19
# You can find data beyond cumulative cases there!

'''
Test your code by analysing total confirmed cases over time
Each line in the file represents one day. The first value is confirmed cases on Jan 22nd.
The number of confirmed cases is "cumulative" meaning that it is the total number
of cases up until the current day. It will never go down! 
'''

ITALY_PATH = 'italy.txt'

# This directory has files for all countries if you want to explore further
DATA_DIR = 'confirmed'

import matplotlib.pyplot as plt

def main():
    my_list = []
    for line in open('italy.txt'):
        # str: num + \n => int
        l = int(line.strip())
        my_list.append(l)
    plt.plot(my_list)
    plt.show()
    

if __name__ == '__main__':
    main()
