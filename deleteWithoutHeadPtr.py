def deleteNode(self,del_node):
        if not del_node.next:
            del_node=None
        del_node.data=del_node.next.data
        del_node.next=del_node.next.next