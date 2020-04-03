#Take n number of inputs from user with each containing a string 'name' and float marks in coure
# print the ones with the second lowest marks

# To take Custom Input 

#marksheet = []
    #for _ in range(0,int(input())):
        #marksheet.append([input(), float(input())])
    



n = 5
marksheet = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
second_lowest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_lowest]))
        

    