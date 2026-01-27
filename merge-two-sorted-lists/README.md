Merge Two Sorted Lists — Python Solution

📌 Problem Description

You are given the heads of two sorted linked lists, list1 and list2.

Your task is to merge the two lists into a single sorted linked list, and return its head.

The merged list must be built by splicing together the nodes of the original lists — no new nodes should be created.

Examples

\- Input: list1 = \[1,2,4], list2 = \[1,3,4]

Output: \[1,1,2,3,4,4]

\- Input: list1 = \[], list2 = \[]

Output: \[]

\- Input: list1 = \[], list2 = \[0]

Output: \[0]



💡 Approach

The solution uses a dummy node and a pointer (current) to build the merged list.

Steps:

\- Create a dummy node to simplify edge cases

\- Compare the current nodes of both lists

\- Append the smaller node to the merged list

\- Move the pointer forward in the chosen list

\- When one list ends, append the remaining nodes of the other list

\- Return dummy.next as the head of the merged list

This is the most common and efficient approach for this problem.



🧠 Time \& Space Complexity

\- Time Complexity: O(n + m)

Each list is traversed once.

\- Space Complexity: O(1)

The merge is done in‑place using existing nodes.



📝 Code Implementation

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



🧪 Example Usage

\# Example linked lists:

\# list1: 1 -> 2 -> 4

\# list2: 1 -> 3 -> 4



merged = mergeTwoLists(list1, list2)

\# Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4



📁 File Structure

merge-two-sorted-lists/

│

├── merge\_two\_lists.py   # Python implementation

└── README.md            # Documentation



✔️ Notes

\- This is the most widely accepted and optimal solution for this problem.

\- The dummy node pattern is a common technique in linked list problems.

\- Perfect for algorithm practice and LeetCode collections.

