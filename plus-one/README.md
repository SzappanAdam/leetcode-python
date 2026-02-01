Plus One — Python Solution

📌 Problem Description

You are given a large integer represented as an array of digits, where each element digits\[i] is a single digit of the number.

The digits are stored such that the most significant digit is at the front of the list.

Your task is to add one to the integer and return the resulting list of digits.

Examples

\- Input: \[1,2,3] → Output: \[1,2,4]

\- Input: \[4,3,2,1] → Output: \[4,3,2,2]

\- Input: \[9,9,9] → Output: \[1,0,0,0]



💡 Approach

The solution processes the digits from right to left, simulating the addition of 1:

\- Start from the last digit

\- If the digit is less than 9 → increment it and return

\- If the digit is 9 → set it to 0 and continue carrying

\- If all digits were 9 → prepend 1 to the list

This approach avoids converting the digits to an integer, which is important for very large numbers.



🧠 Time \& Space Complexity

\- Time Complexity: O(n)

Each digit is processed at most once.

\- Space Complexity: O(1)

Except for the special case where a new digit is added (e.g., \[9,9,9] → \[1,0,0,0]).



📝 Code Implementation

def plusOne(digits: list\[int]) -> list\[int]:

&nbsp;   """

&nbsp;   Adds one to the integer represented by the list of digits.

&nbsp;   Handles carry propagation from right to left.

&nbsp;   """

&nbsp;   n = len(digits)



&nbsp;   for i in range(n - 1, -1, -1):

&nbsp;       if digits\[i] < 9:

&nbsp;           digits\[i] += 1

&nbsp;           return digits

&nbsp;       digits\[i] = 0



&nbsp;   return \[1] + digits



🧪 Example Usage

print(plusOne(\[1,2,3]))      # \[1,2,4]

print(plusOne(\[9,9,9]))      # \[1,0,0,0]

print(plusOne(\[4,3,2,1]))    # \[4,3,2,2]



📁 File Structure

plus-one/

│

├── plus\_one.py   # Python implementation

└── README.md     # Documentation



✔️ Notes

\- This is the optimal solution for this problem.

\- It avoids integer overflow issues by working directly with the digit list.

\- Perfect for algorithm practice and LeetCode collections.

