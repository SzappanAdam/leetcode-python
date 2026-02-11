Intersection of Two Linked Lists — Python Solution

📌 Problem Description

You are given the heads of two singly linked lists headA and headB.

Return the node at which the two lists intersect, or None if they do not intersect.

Two linked lists intersect if they share the same node reference, not just the same value.

Examples

\- Input:

A: 4 → 1 → 8 → 4 → 5

B: 5 → 6 → 1 → 8 → 4 → 5

Output: Node with value 8

\- Input:

A: 1 → 9 → 1 → 2 → 4

B: 3 → 2 → 4

Output: Node with value 2

\- Input:

A: 2 → 6 → 4

B: 1 → 5

Output: None



💡 Approach

This solution uses the elegant two‑pointer switching technique.

Key idea

Let:

\- a traverse list A

\- b traverse list B

When a pointer reaches the end of its list, it switches to the head of the other list.

Because both pointers traverse exactly:

\\mathrm{len(A)}+\\mathrm{len(B)}

…they will either:

\- meet at the intersection node, or

\- both reach None at the same time (no intersection)

This guarantees correctness without extra memory.



🧠 Time \& Space Complexity

\- Time Complexity: O(n + m)

Each pointer traverses both lists once.

\- Space Complexity: O(1)

No additional data structures are used.

This is the optimal solution.



📝 Code Implementation

class ListNode:

&nbsp;   def \_\_init\_\_(self, x):

&nbsp;       self.val = x

&nbsp;       self.next = None



def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:

&nbsp;   if not headA or not headB:

&nbsp;       return None



&nbsp;   a, b = headA, headB



&nbsp;   while a != b:

&nbsp;       a = a.next if a else headB

&nbsp;       b = b.next if b else headA



&nbsp;   return a



🧪 Example Usage

\# Example:

\# A: 4 -> 1 \\

\#             8 -> 4 -> 5

\# B:     5 -> 6 -> 1 /



nodeA1 = ListNode(4)

nodeA2 = ListNode(1)

nodeC1 = ListNode(8)

nodeC2 = ListNode(4)

nodeC3 = ListNode(5)



nodeA1.next = nodeA2

nodeA2.next = nodeC1

nodeC1.next = nodeC2

nodeC2.next = nodeC3



nodeB1 = ListNode(5)

nodeB2 = ListNode(6)

nodeB3 = ListNode(1)



nodeB1.next = nodeB2

nodeB2.next = nodeB3

nodeB3.next = nodeC1  # intersection



print(getIntersectionNode(nodeA1, nodeB1).val)  # 8



📁 File Structure

intersection-of-two-linked-lists/

│

├── get\_intersection\_node.py   # Python implementation

└── README.md                  # Documentation



✔️ Notes

\- This is the optimal O(1)‑space solution.

\- No need for sets or length calculations.

\- A classic pointer‑switching trick often asked in interviews.

