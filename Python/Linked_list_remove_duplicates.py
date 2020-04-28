#Use list Data structures to develop a linked list and write a function remove duplicates to remove duplicates 
#in the linked list to return the head of the updated list.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        cur = head
        if (cur == None):  
            return 
        if (cur.next != None):  
          
        # Compare current node with next node  
            if (cur.data == cur.next.data):    
            # to_free pointer stores the next of current  
            # pointer which is to be deleted.  
                to_free = cur.next
                cur.next = cur.next.next
              
            # free(to_free)  
                self.removeDuplicates(cur)  
          
        # Important: only advance if no deletion 
            else:  
                self.removeDuplicates(cur.next)  
          
        return head 
        

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 