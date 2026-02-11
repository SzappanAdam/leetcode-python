Linked List Cycle — Python Solution

Problem Description

Given the head of a singly linked list, determine whether the list contains a cycle.

A cycle exists if a node’s next pointer points to a previously visited node, causing the list to loop infinitely.

Examples

\- Input: 3 → 2 → 0 → -4 ↘

↑\_\_\_\_\_\_\_\_\_\_\_

Output: True

\- Input: 1 → 2 → None

Output: False

\- Input: 1 → None

Output: False



Approach

There are two standard approaches to detect a cycle in a linked list:



Approach 1 — Floyd’s Tortoise and Hare (Optimal)

This algorithm uses two pointers:

\- slow moves one step at a time

\- fast moves two steps at a time

If the list contains a cycle, the two pointers will eventually meet.

Why it works

\- If there is no cycle, fast reaches None

\- If there is a cycle, fast will “lap” slow and they will meet

Complexity

\- Time: O(n)

\- Space: O(1) — constant extra memory

This is the optimal and most commonly expected interview solution.

Code

class ListNode:

&nbsp;   def \_\_init\_\_(self, x):

&nbsp;       self.val = x

&nbsp;       self.next = None



def hasCycle(head: ListNode) -> bool:

&nbsp;   slow = fast = head



&nbsp;   while fast and fast.next:

&nbsp;       slow = slow.next

&nbsp;       fast = fast.next.next



&nbsp;       if slow == fast:

&nbsp;           return True



&nbsp;   return False



Approach 2 — Hash Set Tracking

This method stores visited nodes in a set:

\- If a node is seen again → cycle detected

\- Otherwise, continue traversing

Complexity

\- Time: O(n)

\- Space: O(n) — storing visited nodes

This solution is intuitive and easy to understand, though not optimal in memory.

Code

def hasCycle(head: ListNode) -> bool:

&nbsp;   seen = set()

&nbsp;   current = head



&nbsp;   while current:

&nbsp;       if current in seen:

&nbsp;           return True

&nbsp;       seen.add(current)

&nbsp;       current = current.next



&nbsp;   return False



Example Usage

\# Example linked list with a cycle:

\# 3 -> 2 -> 0 -> -4

\#       ^         |

\#       |\_\_\_\_\_\_\_\_\_|



node1 = ListNode(3)

node2 = ListNode(2)

node3 = ListNode(0)

node4 = ListNode(-4)



node1.next = node2

node2.next = node3

node3.next = node4

node4.next = node2  # cycle here



print(hasCycle(node1))  # True



File Structure

linked-list-cycle/

│

├── has\_cycle.py   # Python implementations

└── README.md      # Documentation



Notes

\- Floyd’s algorithm is the optimal solution and widely used in interviews.

\- The set‑based solution is excellent for clarity and debugging.

\- This problem is foundational for understanding pointer techniques in linked lists.

