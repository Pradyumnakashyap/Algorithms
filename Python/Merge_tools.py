#The first line contains a single string denoting s.
# The second line contains an integer,k, denoting the length of each subsegment.
# Print n/k lines where each line i contains string ui (No gaurentee n is divisible by k) make sure to take our all duplicates in each line
import textwrap
def merge_the_tools(string, k):
    # your code goes here
    final=''
    for i in range(0,len(string)):
        if string[i] not in final:
            final=final+string[i]  
        if (i+1)%k==0:
            print(final)
            final=''

    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)