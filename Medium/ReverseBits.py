# get an integer, convert it to binary, reverse its binary digits and print the decimal form of that reversed binary number for "t" values

t = int(input())

for i in range(t):
  p = int(input())
  binary = str(int(str(bin(p))[2:][::-1]))    # the first str is for getting the binary value, reading only the characters from the 2nd index (as binary values start with a "0b")
                                              # the int is to remove any 0s that were intially at the end of the binary value, but came to the beginning after reversal
                                              # the final str is to make it a suitable binary value for the following operations
  binary = "0b" + binary            
  
  print(int(binary, 2))
