Remove Duplicates from Sorted List — Python Solution

📌 Problem Description

Given the head of a sorted linked list, delete all duplicates so that each element appears only once.

Return the head of the modified list.

Because the list is sorted, duplicate values will always appear consecutively, which allows a simple linear scan.

Examples

\- Input: 1 → 1 → 2

Output: 1 → 2

\- Input: 1 → 1 → 2 → 3 → 3

Output: 1 → 2 → 3



💡 Approach

The algorithm iterates through the linked list using a pointer current.

For each node:

\- If current.val == current.next.val, skip the next node by updating the pointer

\- Otherwise, move forward normally

Since the list is sorted, duplicates will always be adjacent, making this approach efficient and straightforward.



🧠 Time \& Space Complexity

\- Time Complexity: O(n)

Each node is visited once.

\- Space Complexity: O(1)

No additional data structures are used.



📝 Code Implementation

class ListNode:

&nbsp;   def \_\_init\_\_(self, val=0, next=None):

&nbsp;       self.val = val

&nbsp;       self.next = next



def deleteDuplicates(head: ListNode) -> ListNode:

&nbsp;   """

&nbsp;   Removes duplicates from a sorted linked list.

&nbsp;   Returns the head of the modified list.

&nbsp;   """

&nbsp;   current = head



&nbsp;   while current and current.next:

&nbsp;       if current.val == current.next.val:

&nbsp;           current.next = current.next.next

&nbsp;       else:

&nbsp;           current = current.next



&nbsp;   return head



🧪 Example Usage

Because LeetCode uses linked lists, here is a helper setup for local testing:

def build\_list(values):

&nbsp;   if not values:

&nbsp;       return None

&nbsp;   head = ListNode(values\[0])

&nbsp;   current = head

&nbsp;   for v in values\[1:]:

&nbsp;       current.next = ListNode(v)

&nbsp;       current = current.next

&nbsp;   return head



def print\_list(head):

&nbsp;   values = \[]

&nbsp;   current = head

&nbsp;   while current:

&nbsp;       values.append(current.val)

&nbsp;       current = current.next

&nbsp;   print(values)



head = build\_list(\[1, 1, 2, 3, 3])

result = deleteDuplicates(head)

print\_list(result)  # \[1, 2, 3]



📁 File Structure

remove-duplicates-from-sorted-list/

│

├── delete\_duplicates.py   # Python implementation

└── README.md              # Documentation



✔️ Notes

\- This is the optimal solution for this problem.

\- Works only because the list is sorted — otherwise, duplicates would not be adjacent.

\- Perfect for practicing linked list manipulation.

