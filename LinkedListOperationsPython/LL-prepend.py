class Node(self,value):
    self.value = value
    self.next = None

class LinkedList(self):
    self.head = None
    self.tail = None
    self.length = 0

    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    