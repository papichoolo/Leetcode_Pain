class Solution:
    # Function to remove a loop in the linked list.
    def removeLoop(self, head):
        def detectAndRemoveLoop(head):
            slow = head
            fast = head

            # Detect loop
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    break

            # If no loop found, return
            if not fast or not fast.next:
                return

            # Find the length of the loop
            length = 1
            while fast.next != slow:
                fast = fast.next
                length += 1

            # Reset slow pointer to head and move fast pointer ahead by length nodes
            slow = head
            fast = head
            for _ in range(length):
                fast = fast.next

            # Move both pointers until they meet, this will be the starting point of the loop
            while slow != fast:
                slow = slow.next
                fast = fast.next

            # Move the fast pointer to the last node of the loop
            while fast.next != slow:
                fast = fast.next

            # Remove the loop by setting the next of the last node to None
            fast.next = None

        detectAndRemoveLoop(head)
        return head