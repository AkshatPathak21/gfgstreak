class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#Advanced Linked list
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

#Basic Linked List
#creating Node
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

#Linking the Nodes
n1.next = n2
n2.next = n3
n3.next = n4

#Printing the Linked List
curr = n1
while(curr):
    print(curr.data,end="->")
    curr = curr.next