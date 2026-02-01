Sqrt(x) — Python Solution

📌 Problem Description

Given a non‑negative integer x, compute and return the integer square root of x.

The integer square root is defined as:

\- the floor of the real square root

\- i.e., the largest integer r such that r \* r ≤ x

You must not use built‑in exponent functions like pow(x, 0.5).

Examples

\- Input: x = 4 → Output: 2

\- Input: x = 8 → Output: 2 (since √8 ≈ 2.828, floor = 2)

\- Input: x = 0 → Output: 0



💡 Approach

The solution uses binary search to efficiently find the integer square root.

Steps:

\- Handle small cases (0 and 1) immediately

\- Set search boundaries:

\- left = 1

\- right = x // 2

\- Compute mid and compare mid \* mid with x

\- Narrow the search space accordingly

\- If no exact square root is found, return right, which will be the floor value

This approach ensures optimal performance even for very large integers.



🧠 Time \& Space Complexity

\- Time Complexity: O(log n)

Binary search reduces the range exponentially.

\- Space Complexity: O(1)

Only a few variables are used.



📝 Code Implementation

def mySqrt(x: int) -> int:

&nbsp;   """

&nbsp;   Computes the integer square root of x using binary search.

&nbsp;   Returns the floor of the real square root.

&nbsp;   """

&nbsp;   if x < 2:

&nbsp;       return x



&nbsp;   left, right = 1, x // 2



&nbsp;   while left <= right:

&nbsp;       mid = (left + right) // 2

&nbsp;       if mid \* mid == x:

&nbsp;           return mid

&nbsp;       elif mid \* mid < x:

&nbsp;           left = mid + 1

&nbsp;       else:

&nbsp;           right = mid - 1



&nbsp;   return right



🧪 Example Usage

print(mySqrt(4))   # 2

print(mySqrt(8))   # 2

print(mySqrt(1))   # 1

print(mySqrt(0))   # 0



📁 File Structure

sqrt-x/

│

├── my\_sqrt.py   # Python implementation

└── README.md    # Documentation



✔️ Notes

\- This is the optimal solution for this problem.

\- Binary search is the standard technique for computing integer square roots efficiently.

\- Perfect for algorithm practice and LeetCode collections.

