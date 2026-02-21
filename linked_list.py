class Node :
    def __init__(self ,data):
        self.data = data 
        self.next = None
class linked_list:
    def __init__(self):
        self.head = None
        self.length = 0 

    def append(self, value):
        node: Node = Node(value)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1


    


   