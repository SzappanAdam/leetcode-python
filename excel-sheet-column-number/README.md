Excel Sheet Column Number — Python Solution

📌 Problem Description

Given a string columnTitle representing an Excel column title (e.g., "A", "AB", "ZY"), return its corresponding column number.

Excel columns follow this pattern:

A  -> 1

B  -> 2

...

Z  -> 26

AA -> 27

AB -> 28

...



This is essentially converting a base‑26 alphabetic representation into an integer.



💡 Approach

Excel column titles behave like a base‑26 number system, but with a twist:

\- Instead of digits 0–25, we have letters A–Z representing 1–26.

\- Therefore, each character contributes its value as:

\\mathrm{value}=\\mathrm{ord(ch)}-\\mathrm{ord('A')}+1

The algorithm processes characters from left to right:

\- Multiply the current result by 26

\- Add the numeric value of the current character

This is identical to converting a number from base‑26 to base‑10.



🧠 Time \& Space Complexity

\- Time Complexity: O(n)

Each character is processed once.

\- Space Complexity: O(1)

Only a single integer accumulator is used.

This is the optimal solution.



📝 Code Implementation

def titleToNumber(columnTitle: str) -> int:

&nbsp;   result = 0

&nbsp;   for ch in columnTitle:

&nbsp;       result = result \* 26 + (ord(ch) - ord('A') + 1)

&nbsp;   return result



🧪 Example Usage

print(titleToNumber("A"))    # 1

print(titleToNumber("Z"))    # 26

print(titleToNumber("AA"))   # 27

print(titleToNumber("AB"))   # 28

print(titleToNumber("ZY"))   # 701

print(titleToNumber("AAA"))  # 703



📁 File Structure

excel-sheet-column-number/

│

├── title\_to\_number.py   # Python implementation

└── README.md            # Documentation



✔️ Notes

\- This is the canonical solution to the problem.

\- No need for reversing the string or using extra data structures.

\- The logic mirrors base‑conversion algorithms used in number systems.

