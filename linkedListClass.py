from DSA.temp import LinkedList


class Node:
    def __init__(self,data=None,next = None):
        self.data = data
        self.next = next

#Class declaration of linked list
class linkdeList:
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

    #printing linked list
    def printLinkedList(self):
        curr = self.head
        while(curr):
            print(curr.data)
            curr = curr.next


ob = LinkedList()
ob.insert(10)
ob.insert(20)
ob.printLinkedList()

