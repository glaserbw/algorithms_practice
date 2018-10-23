class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def addEnd(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else: 
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node             
        self.size += 1

    def printLl(self):
        result = ''
        temp = self.head
        while temp.next != None: 
            result += str(temp.value)+'->'
            temp = temp.next
        result += str(temp.value)
        print(result)

    def insertAfter(self,prev_node, value):
        if prev_node is None:
            print('Previous node not on linked list')
            return
        new_node=Node(value)
        new_node.next=prev_node.next
        prev_node.next=new_node

    def insertIdx(self, value, idx):
        new_node=Node(value)
        count=0
        if self.head==None:
            self.head=new_node
        else: 
            temp1=self.head
            temp2=self.head
            while temp1.next and temp2.next != None:
                temp1=temp1.next
                temp2=temp2.next
                count+=1 
                if count==idx-1:
                    temp1.next=new_node
                if count==idx+1:
                    new_node=temp2
        self.size+=1

                
                
        
newll = LinkedList()

newll.addend(2)
newll.addend(3)
newll.print_ll()

def insertAfter(self, prev_node, new_data): 
  
        # 1. check if the given prev_node exists 
        if prev_node is None: 
            print "The given previous node must inLinkedList."
            return
  
        #  2. create new node & 
        #      Put in the data 
        new_node = Node(new_data) 
  
        # 4. Make next of new Node as next of prev_node 
        new_node.next = prev_node.next
  
        # 5. make next of prev_node as new_node 
        prev_node.next = new_node
