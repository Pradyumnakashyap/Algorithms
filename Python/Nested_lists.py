#Take n number of inputs from user with each containing a string 'name' and float marks in coure
# print the ones with the second lowest marks
#Constraint minimum two inputs provided
 

marksheet = []
for _ in range(0,int(input("Enter number of students "))):
    marksheet.append([input("Enter the name of student "), float(input("Enter the marks for the student "))])
second_lowest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_lowest]))
        

    