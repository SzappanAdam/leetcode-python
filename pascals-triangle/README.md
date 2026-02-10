Pascal's Triangle — Python Solution

📌 Problem Description

Given an integer numRows, generate the first numRows of Pascal’s Triangle.

In Pascal’s Triangle:

\- Each row starts and ends with 1

\- Every inner element is the sum of the two elements directly above it

Examples

\- Input: numRows = 5

Output:

\[

&nbsp; \[1],

&nbsp; \[1,1],

&nbsp; \[1,2,1],

&nbsp; \[1,3,3,1],

&nbsp; \[1,4,6,4,1]

]

\- Input: numRows = 1

Output: \[\[1]]



💡 Approach

The triangle is built row by row.

For each row:

\- Initialize it with all 1s

\- For each inner position j (from 1 to i-1):

\\mathrm{row}\[j]=\\mathrm{previous\\\_ row}\[j-1]+\\mathrm{previous\\\_ row}\[j]- Append the completed row to the triangle

This approach directly follows the mathematical definition of Pascal’s Triangle.



🧠 Time \& Space Complexity

\- Time Complexity: O(n²)

Each row has up to n elements, and you compute all rows.

\- Space Complexity: O(n²)

Required to store the entire triangle.



📝 Code Implementation

def generate(numRows: int):

&nbsp;   """

&nbsp;   Generates the first numRows of Pascal's Triangle.

&nbsp;   Each row is constructed based on the previous row.

&nbsp;   """

&nbsp;   triangle = \[]



&nbsp;   for i in range(numRows):

&nbsp;       row = \[1] \* (i + 1)



&nbsp;       for j in range(1, i):

&nbsp;           row\[j] = triangle\[i - 1]\[j - 1] + triangle\[i - 1]\[j]



&nbsp;       triangle.append(row)



&nbsp;   return triangle



🧪 Example Usage

print(generate(5))

\# Output:

\# \[

\#   \[1],

\#   \[1,1],

\#   \[1,2,1],

\#   \[1,3,3,1],

\#   \[1,4,6,4,1]

\# ]



📁 File Structure

pascals-triangle/

│

├── generate.py   # Python implementation

└── README.md     # Documentation



✔️ Notes

\- This is the standard dynamic programming solution.

\- Each row depends only on the previous one.

\- Perfect for practicing 2D list construction and combinatorial patterns.

