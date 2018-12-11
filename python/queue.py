class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue: 
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0 

    def enqueue(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        self.size += 1
        
