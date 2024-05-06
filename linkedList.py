class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#Basic Declaration of Linked List

#Creating Nodes
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

#Linking the Nodes
n1.next = n2
n2.next = n3
n3.next = n4

#Printing the Linked List (List Traversal)
curr = n1
while(curr):
    if curr.next is not None:
        print(curr.data,end=" -> ")
    else:
        print("None")
    curr = curr.next