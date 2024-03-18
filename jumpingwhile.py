# Function to print x in increasing order
def printIncreasingPower(x):
    i = 1
    # Loop to jump in powers of 2
    while(i**2 <= x):
        print ( i**2, end = " ")
        i+=1