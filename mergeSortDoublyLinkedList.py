class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class Solution():
    def sortDoubly(self,head):
        def mergesort(sta=head):
            if not sta.next:
                return sta
            slow,fast=sta,sta
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            mid=slow
            mid.prev.next=None
            mid.prev=None
            left=mergesort(sta)
            right=mergesort(mid)
            dummy= Node(None)
            cur=dummy
            while left or right:
                if left and right:
                    if left.data<=right.data:
                        cur.next=left
                        left.prev=cur
                        left=left.next
                    else:
                        cur.next=right
                        right.prev=cur
                        right=right.next
                elif left:
                    cur.next=left
                    left.prev=cur
                    left=None
                elif right:
                    cur.next=right
                    right.prev=cur
                    right=None
                cur=cur.next
            dummy.next.prev=None
            return dummy.next
        return mergesort()