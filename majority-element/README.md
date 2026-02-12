Majority Element — Python Solution

📌 Problem Description

You are given an array nums of size n, where the majority element is the element that appears more than ⌊n/2⌋ times.

The task is to return this majority element.

The problem guarantees that a majority element always exists.

Examples

\- Input: \[3,2,3]

Output: 3

\- Input: \[2,2,1,1,1,2,2]

Output: 2



💡 Approach

This solution uses the Boyer–Moore Majority Vote Algorithm, a clever linear‑time, constant‑space method for finding the majority element.

Key idea

We maintain:

\- a candidate for the majority element

\- a count that increases when we see the candidate and decreases otherwise

Whenever the count drops to zero, we choose a new candidate.

Because the majority element appears more than half the time, it will always survive this elimination process.



🧠 Time \& Space Complexity

\- Time Complexity: O(n)

Single pass through the array.

\- Space Complexity: O(1)

Only two variables are used.

This is the optimal solution.



📝 Code Implementation

def majorityElement(nums):

&nbsp;   count = 0

&nbsp;   candidate = None



&nbsp;   for num in nums:

&nbsp;       if count == 0:

&nbsp;           candidate = num

&nbsp;       count += (1 if num == candidate else -1)



&nbsp;   return candidate



🧪 Example Usage

print(majorityElement(\[3, 2, 3]))              # 3

print(majorityElement(\[2, 2, 1, 1, 1, 2, 2]))  # 2

print(majorityElement(\[1]))                    # 1



📁 File Structure

majority-element/

│

├── majority\_element.py   # Python implementation

└── README.md             # Documentation



✔️ Notes

\- The Boyer–Moore algorithm is the optimal solution for this problem.

\- No need for frequency maps or sorting.

\- The majority element is guaranteed to exist, so no second validation pass is required.

