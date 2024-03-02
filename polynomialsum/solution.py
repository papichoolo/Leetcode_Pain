class node:
    def __init__(self, coeff, pwr):
        self.coef = coeff
        self.next = None
        self.power = pwr
        
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, coeff, pwr):
        if self.head == None:
            self.head = node(coeff, pwr)
        else:
            new_node = node(coeff, pwr)
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node

def createList(arr, n):
    lis = Linked_List()
    k=0
    for i in range(n):
        lis.insert(arr[k], arr[k+1])
        k+=2
    return lis.head


class Solution: 
      
    # Method to add two polynomials 
    def addPolynomial(self, p1, p2): 
  
        a = p1 
        b = p2 
        newHead = node(0, 0) 
        c = newHead; 
  
        while (a != None or b != None): 
  
            if (a == None): 
                c.next = b; 
                break
              
            elif (b == None): 
                c.next = a; 
                break; 
              
  
            elif (a.power == b.power): 
                c.next = node(a.coef + b.coef, a.power); 
  
                a = a.next; 
                b = b.next; 
              
  
            elif (a.power > b.power): 
                c.next = node(a.coef, a.power); 
  
                a = a.next; 
              
  
            elif (a.power < b.power): 
                c.next = node(b.coef, b.power); 
  
                b = b.next; 
              
  
            c = c.next; 
  
        return newHead.next; 
      
