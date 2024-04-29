class Solution:
    def deleteMid(self,head):
        c = 0
        ptr = head
        while ptr!= None:
            ptr = ptr.next
            c = c+1
        temp = head
        if c ==1:
            head = head.next
            return head
        else:
            for i in range(c//2):
                prev = temp
                temp = temp.next
                if i ==c//2-1:
                    prev.next = temp.next
            return head