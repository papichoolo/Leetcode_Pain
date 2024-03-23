class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class Queue:
    def __init__(self,data):
        new_node=Node(data)
        self.first=new_node
        self.last=new_node
        self.length=1

    def printlist(self):
        temp= self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
    #enqueue operation
    
    def enqueue(self,data):
        new_node=Node(data)
        if self.first is None:
            self.first=new_node
            self.last=new_node
        else:
            self.last.next=new_node
            self.last=new_node
        self.length+=1

q=Queue(4)
q.printlist()
q.enqueue(3)
q.enqueue(78)
q.printlist()