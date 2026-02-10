Pascal's Triangle II — Python Solution

📌 Problem Description

Given an integer rowIndex, return the rowIndex‑th (0‑indexed) row of Pascal’s Triangle.

In Pascal’s Triangle:

\- Each row starts and ends with 1

\- Every inner element is the sum of the two elements directly above it

Examples

\- Input: rowIndex = 3

Output: \[1, 3, 3, 1]

\- Input: rowIndex = 0

Output: \[1]

\- Input: rowIndex = 1

Output: \[1, 1]



💡 Approach

There are two common ways to compute the rowIndex‑th row:

Approach 1 — Build Rows Iteratively (Classic DP)

You generate each row from the previous one until reaching rowIndex.

\- Easy to understand

\- Uses O(n) extra space

\- Time complexity: O(n²)

Approach 2 — In‑Place Update (Optimized DP)

You maintain a single list and update it from right to left, ensuring values are not overwritten prematurely.

\- Optimal space usage

\- Still O(n²) time

\- This is the preferred solution in interviews

Both solutions are correct and accepted.



🧠 Time \& Space Complexity

|  |  |  |  | 

|  |  |  |  | 

|  |  |  |  | 



📝 Code Implementation

✔️ Solution 1 — Build Rows Iteratively

def getRow(rowIndex: int):

&nbsp;   row = \[1]

&nbsp;   for i in range(rowIndex):

&nbsp;       new\_row = \[1]

&nbsp;       for j in range(1, len(row)):

&nbsp;           new\_row.append(row\[j - 1] + row\[j])

&nbsp;       new\_row.append(1)

&nbsp;       row = new\_row

&nbsp;   return row



✔️ Solution 2 — In‑Place Update (Optimized)

def getRow(rowIndex: int):

&nbsp;   row = \[1] \* (rowIndex + 1)

&nbsp;   for i in range(2, rowIndex + 1):

&nbsp;       for j in range(i - 1, 0, -1):

&nbsp;           row\[j] += row\[j - 1]

&nbsp;   return row



🧪 Example Usage

print(getRow(3))  # \[1, 3, 3, 1]

print(getRow(0))  # \[1]

print(getRow(5))  # \[1, 5, 10, 10, 5, 1]



📁 File Structure

pascals-triangle-ii/

│

├── get\_row.py     # Python implementations

└── README.md      # Documentation



✔️ Notes

\- Both solutions are correct; the second is more space‑efficient.

\- The in‑place update technique is a classic DP trick and often appears in interviews.

\- This problem is a natural extension of LeetCode 118 (Pascal’s Triangle).

