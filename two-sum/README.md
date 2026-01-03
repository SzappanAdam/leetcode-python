Two Sum — Python Solution



📌 Problem Description



Given an array of integers nums and an integer target, the task is to return the indices of the two numbers such that they add up to the target.

You may assume:

\- Each input has exactly one valid solution.

\- You may not use the same element twice.

\- The order of the returned indices does not matter.

This is one of the most common introductory algorithm problems on LeetCode.



💡 Approach



The solution uses a hash map (dictionary) to store previously seen numbers and their indices.

For each number:

\- Compute its complement: target - num

\- Check if the complement is already in the dictionary

\- If yes → return the pair of indices

\- If not → store the current number and its index

This allows us to solve the problem in O(n) time.



🧠 Time \& Space Complexity



\- Time Complexity: O(n)

We traverse the list once, and dictionary lookups are O(1) on average.

\- Space Complexity: O(n)

In the worst case, we store every number in the dictionary.



🧪 Example Usage



from two\_sum import two\_sum

print(two\_sum(\[2, 7, 11, 15], 9))   # Output: \[0, 1]

print(two\_sum(\[3, 2, 4], 6))        # Output: \[1, 2]

print(two\_sum(\[3, 3], 6))           # Output: \[0, 1]



📁 File Structure



two-sum/

│

├── two\_sum.py      # Python implementation

└── README.md        # Documentation



📝 Code Implementation



def two\_sum(nums: list\[int], target: int) -> list\[int]:

&nbsp;   """

&nbsp;   Returns the indices of two numbers in `nums` that add up to `target`.

&nbsp;   Uses a hash map for O(n) time complexity.

&nbsp;   """

&nbsp;   seen = {}



&nbsp;   for index, num in enumerate(nums):

&nbsp;       complement = target - num

&nbsp;       if complement in seen:

&nbsp;           return \[seen\[complement], index]

&nbsp;       seen\[num] = index



✔️ Notes

\- This solution is optimal for the Two Sum problem.

\- The code follows clean, readable Python conventions.

\- Suitable for interview preparation and algorithm practice.

