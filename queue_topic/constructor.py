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


q=Queue(4)
q.printlist()