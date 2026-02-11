Single Number — Python Solution

Problem Description

You are given a non‑empty array of integers nums, where every element appears twice except for one.

Your task is to find the element that appears exactly once.

You must implement a solution with:

\- O(n) time complexity

\- O(1) extra space

Examples

\- Input: \[2,2,1]

Output: 1

\- Input: \[4,1,2,1,2]

Output: 4

\- Input: \[1]

Output: 1



Approach

There are two common approaches to solve this problem:

Approach 1 — XOR Trick (Optimal)

This solution uses the properties of the XOR operator:

\- a ^ a = 0

\- a ^ 0 = a

\- XOR is commutative and associative

Thus, all duplicate numbers cancel out, and only the unique number remains.

This is the optimal solution with O(1) extra memory.



Approach 2 — Set Toggle Method

This approach uses a set to track numbers:

\- If a number appears for the first time → add it

\- If it appears again → remove it

At the end, the set contains only the unique number.

This is intuitive and easy to understand, but uses O(n) extra memory.



Time \& Space Complexity

|  |  |  |  | 

|  |  |  |  | 

|  |  |  |  | 



Code Implementation

Solution 1 — XOR Trick (Optimal)

def singleNumber(nums: list\[int]) -> int:

&nbsp;   result = 0

&nbsp;   for n in nums:

&nbsp;       result ^= n

&nbsp;   return result



Solution 2 — Set Toggle Method

def singleNumber(nums: list\[int]) -> int:

&nbsp;   seen = set()

&nbsp;   for n in nums:

&nbsp;       if n in seen:

&nbsp;           seen.remove(n)

&nbsp;       else:

&nbsp;           seen.add(n)

&nbsp;   return seen.pop()



Example Usage

print(singleNumber(\[2, 2, 1]))        # 1

print(singleNumber(\[4, 1, 2, 1, 2]))  # 4

print(singleNumber(\[1]))              # 1



File Structure

single-number/

│

├── single\_number.py   # Python implementations

└── README.md          # Documentation



Notes

\- The XOR solution is the preferred one in interviews due to its optimal space usage.

\- The set‑based solution is great for clarity and debugging.

\- This problem is a classic introduction to bit manipulation.

