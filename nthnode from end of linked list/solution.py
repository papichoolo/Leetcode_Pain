def getNthFromLast(head, n):
    if not head:
        return -1

    # Initialize two pointers, first and second
    first = head
    second = head

    # Move the first pointer n steps ahead
    for _ in range(n):
        if not first:
            return -1
        first = first.next

    # Move both pointers together until the first pointer reaches the end
    while first:
        first = first.next
        second = second.next

    # At this point, the second pointer is pointing to the Nth node from the end
    return second.data
