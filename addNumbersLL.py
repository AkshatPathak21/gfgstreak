class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Solution:
    #Function to add two numbers represented by linked list.
    
    def reverselist(self, num):
        
        prev = None
        
        cur = num
        
        nxt = None
        
        while cur:
            
            nxt = cur.next
            
            cur.next = prev
            
            prev = cur
            
            cur = nxt
            
        return prev
            
            
        
        
    
    def addTwoLists(self, num1, num2):
        # code here
        # return head of sum list
        
        
        revnum1 = self.reverselist(num1)
        
        revnum2 = self.reverselist(num2)
        
        
        cur_sm = 0
        
        currier = 0
        
        stupid_head = Node(-1)
        
        temp = stupid_head
        
        temp1 = revnum1
        
        temp2 = revnum2
        
        while temp1 or temp2 or currier:
            
            cur_sm = 0
            
            if temp1:
                
                cur_sm += temp1.data
                
                temp1 = temp1.next
                
            if temp2:
                
                cur_sm += temp2.data
                
                temp2 = temp2.next
                
            cur_sm+= currier
            
            
                
            new_node = Node(cur_sm%10)
            currier = cur_sm//10
            temp.next = new_node
            temp = temp.next
            
        
            
        ans = self.reverselist(stupid_head.next)
        
        while ans and ans.data == 0:
            
            ans = ans.next
            
            
        return ans if ans else Node(0)