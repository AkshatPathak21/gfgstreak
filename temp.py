class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linked():
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return self.head
        else:
            ptr = self.head
            while(ptr.next):
                ptr = ptr.next
            ptr.next = new_node
    
    def insertBegin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return self.head
        else:
            ptr = self.head
            self.head = new_node
            self.head.next = ptr

    def printll(self):
        curr = self.head
        while(curr):
            print(curr.data)
            curr = curr.next

ob = linked()

ob.insertBegin(10)

ob.printll()