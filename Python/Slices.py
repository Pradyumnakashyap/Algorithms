
#Take N number of strings and print the strings with even and odd characters of the string separately
# input : 2 good bad 
# output : go od
#          bd a
for N in range(int(input())):
    S = input()
    print(S[::2], S[1::2])