class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def sort(self, head):
        if not head or not head.next:
            return head
        
        st = head
        temp = st.next
        
        while temp:
            if temp.data >= st.data:
                st = temp
                temp = temp.next
            else:
                st.next = temp.next
                prev = None
                curr = head
                while curr != st and curr.data <= temp.data:
                    prev = curr
                    curr = curr.next
                if prev is None:
                    temp.next = head
                    head = temp
                else:
                    temp.next = curr
                    prev.next = temp
            temp = st.next
        
        return head