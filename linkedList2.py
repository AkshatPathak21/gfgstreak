class Node:
    def __init__(self,data=None,next = None):
        self.data = data
        self.next = next

class LL:
    def __init__(self):
        self.head = None

    def insertLast(self,data):
        nn = Node(data)
        if self.head is None:
            self.head = nn
            return self.head
        else:
            itr = self.head
            while(itr.next):
                itr = itr.next
            itr.next = nn
    def printLL(self):
        curr = self.head
        while(curr):
            print(curr.data)
            curr = curr.next

llob = LL()
llob.insertLast("Akshat")
llob.insertLast("Pathak")
llob.printLL()

