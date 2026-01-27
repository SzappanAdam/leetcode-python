def mergeTwoLists(self, list1, list2):
    """
    Merges two sorted linked lists and returns the head of the new sorted list.
    Uses a dummy node to simplify pointer handling.
    """
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    current.next = list1 or list2
    return dummy.next

# Example linked lists:
# list1: 1 -> 2 -> 4
# list2: 1 -> 3 -> 4

merged = mergeTwoLists(list1, list2)
# Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4