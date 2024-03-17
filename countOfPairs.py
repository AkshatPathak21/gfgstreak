'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def countPair(self, head1, head2, n1, n2, x):
        '''
        head1:  head of linkedList 1
        head2:  head of linkedList 2
        n1:  len of  linkedList 1
        n2:  len of linkedList 1
        x:   given sum
        '''
        first=set()
        while head1:
            first.add(head1.data)
            head1=head1.next
        result=0
        while head2:
            if x-head2.data in first:
                result+=1
            head2=head2.next
        return result