#Today, we're learning about Key-Value pair mappings using a Map or Dictionary data structure. 
#Given  names and phone numbers, 
#assemble a phone book that maps friends' names to their respective phone numbers.
#You will then be given an unknown number of names to query your phone book for. 
#For each  queried, print the associated entry from your phone book on a new line in the form name=phoneNumber;
# if an entry for  is not found, print Not found instead.

phone_book = dict([ map(str,input().split()) for x in range(int(input()))])
while True:
    try:
        name = input()
        if name in phone_book:
            print(name, "=", phone_book[name], sep="")
        else : print("Not found")   
    except: break
