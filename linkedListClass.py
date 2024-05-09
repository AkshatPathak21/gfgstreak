class Node:
    def __init__(self,data=None,next = None):
        self.data = data
        self.next = next

#Class declaration of linked list
class linkedList():
    #Creating Head
    def __init__(self):
        self.head = None
    # Inserting items at the end 
    def insert(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return self.head
        else:
            itr = self.head
            while(itr.next):
                itr = itr.next
            itr.next = newNode
    # Inserting items at the beginning
    def insertBegin(self,data):
        newNode = Node(data)
        ptr = self.head
        self.head = newNode
        self.head.next = ptr

    #printing linked list
    def printLinkedList(self):
        curr = self.head
        while(curr):
            print(curr.data,end = " -> ")
            curr = curr.next
        print(None)

ob = linkedList()
ob.insert(10)
ob.insert(20)
ob.insertBegin(0)
ob.insert(30)
ob.insertBegin(-10)
ob.printLinkedList()