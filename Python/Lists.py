#Simulate the functionality of lists 
#List fucntions :
#insert i e: Insert integer e at position i.
#print: Print the list.
#remove e: Delete the first occurrence of integer e.
#append e: Insert integer e at the end of the list.
#sort: Sort the list.
#pop: Pop the last element from the list.
#reverse: Reverse the list.


N = int(input("Enter the number of commands: "))
userList = []
for _ in range(N):
    s = input("Enter <command> <position> <value> ").split()
    usr_command = s[0]
    args = s[1:]
    if usr_command !="print":
        usr_command += "("+ ",".join(args) +")"
        eval("userList."+usr_command)
    else:
        print(userList)