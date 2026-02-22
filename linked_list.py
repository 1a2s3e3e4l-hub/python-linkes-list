class Node :
    def __init__(self ,data):
        self.data = data 
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0 
    
    def length(self):
        return self.length

    def prepend(self, data):
        node: Node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
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
    

    def remove_at(self , index):
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")
        
        if index == 0 :
            removed_data = self.head.data
            self.head = self.head.next 
            self.length -= 1 
            return removed_data
    
        current = self.head
        for _ in range(index - 1):
            current = current.next

        node_to_remove = current.next
        removed_data = node_to_remove.data
        current.next = node_to_remove.next 
        
        self.length -= 1
        return removed_data

    def clear (self):
        self.head = None 
        self.length = 0 

           
# ---------------------------
# Element Queries
# ---------------------------
    def contains(self , value):
        current = self.head
        while current :
            if current.data == value:
                return True
            current= current.next
        return False
    
    def index_of(self,value):
        current = self.head
        index = 0
        while current :
            if current.data == value :
                return index
            current =current.next
            index += 1

        return -1

    def for_each(self, action):
        current = self.head
        while current:
            action(current.data)
            current = current.next


  


   
