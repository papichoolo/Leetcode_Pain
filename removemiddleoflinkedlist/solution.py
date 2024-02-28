
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def deleteMid(self,head):
        slow = head
        fast = head
        prev=None

            # Detect loop
        while fast and fast.next:
            prev=slow
            slow = slow.next
            fast = fast.next.next
                
        prev.next=slow.next
        slow.next=None
        return head
        
        '''
        head:  head of given linkedList
        return: head of resultant llist
        '''
        
        #code here
    