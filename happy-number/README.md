Happy Number — Python Solution

Problem Description

A happy number is defined by the following process:

\- Starting with any positive integer, replace the number with the sum of the squares of its digits.

\- Repeat the process until:

\- the number becomes 1 (then it is a happy number), or

\- it loops endlessly in a cycle that does not include 1.

Return True if n is a happy number, otherwise return False.

Examples

\- Input: 19

Output: True

Explanation:

1² + 9² = 82

8² + 2² = 68

6² + 8² = 100

1² + 0² + 0² = 1

\- Input: 2

Output: False



Approach

There are two classic ways to detect whether the process enters a cycle:



Approach 1 — Using a Hash Set (Cycle Detection)

This method stores previously seen numbers.

If a number repeats, we are in a cycle → not a happy number.

Complexity

\- Time: O(log n)

\- Space: O(log n) — storing visited numbers

Code

def isHappy(n: int) -> bool:

&nbsp;   seen = set()



&nbsp;   while n != 1:

&nbsp;       if n in seen:

&nbsp;           return False

&nbsp;       seen.add(n)



&nbsp;       n = sum(int(digit)\*\*2 for digit in str(n))



&nbsp;   return True



Approach 2 — Floyd’s Cycle Detection (Optimal)

This method uses two pointers:

\- slow moves one step at a time

\- fast moves two steps at a time

If the sequence enters a cycle, slow and fast will eventually meet.

If fast reaches 1, the number is happy.

Complexity

\- Time: O(log n)

\- Space: O(1) — no extra memory

This is the optimal solution.

Code

def isHappy(n: int) -> bool:

&nbsp;   def get\_next(x):

&nbsp;       return sum(int(d)\*\*2 for d in str(x))



&nbsp;   slow = n

&nbsp;   fast = get\_next(n)



&nbsp;   while fast != 1 and slow != fast:

&nbsp;       slow = get\_next(slow)

&nbsp;       fast = get\_next(get\_next(fast))



&nbsp;   return fast == 1



Example Usage

print(isHappy(19))  # True

print(isHappy(2))   # False

print(isHappy(7))   # True



File Structure

happy-number/

│

├── is\_happy.py   # Python implementations

└── README.md     # Documentation



Notes

\- The hash‑set solution is simple and intuitive.

\- The Floyd slow–fast pointer solution is optimal in space.

\- Both approaches are accepted and commonly used in interviews.

