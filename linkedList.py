class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class linkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return self.head
        else:
            itr = self.head
            while(itr.next):
                itr = itr.next
            itr.next = new_node

    def printLL(self):
        curr = self.head
        while(curr):
            print(curr.data)
            curr = curr.next

ob = linkedList()

ob.insert(0)
ob.insert(1)
ob.insert("Akshat")
ob.printLL()