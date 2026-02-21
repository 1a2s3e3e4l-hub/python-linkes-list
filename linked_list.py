class Node :
    def __init__(self ,data):
        self.data = data 
        self.next = None
class linked_list:
    def __init__(self):
        self.head = None
        self.length = 0 

    def append(self, data):
        node: Node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1



    def insert(self, index, data):
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")

        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.length += 1 
            return 
    
        current = self.head
        for _ in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        
        self.length += 1



   