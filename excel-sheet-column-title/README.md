Excel Sheet Column Title — Python Solution

📌 Problem Description

Given an integer columnNumber, return its corresponding Excel column title.

Excel columns follow this pattern:

1  -> A

2  -> B

...

26 -> Z

27 -> AA

28 -> AB

...



This is essentially converting a number into a base‑26 alphabet system, except it is 1‑indexed, not 0‑indexed — which is the main trick of the problem.



💡 Approach

Excel column titles behave like a modified base‑26 system:

\- There is no zero digit

\- Instead of 0–25, the digits are A–Z (1–26)

\- Therefore, before taking the modulo, we must subtract 1

Algorithm steps:

\- Subtract 1 from columnNumber

\- Compute the remainder modulo 26 → this gives the current letter

\- Convert remainder to a character (0 → A, 25 → Z)

\- Prepend the character to the result

\- Divide columnNumber by 26 and repeat until it becomes 0

This ensures correct handling of transitions like:

\- 26 → Z

\- 27 → AA

\- 52 → AZ

\- 53 → BA



🧠 Time \& Space Complexity

\- Time Complexity: O(log₍₂₆₎ n)

Each iteration processes one “digit” of the base‑26 representation.

\- Space Complexity: O(1) extra

Only a few variables are used.

This is the optimal solution.



📝 Code Implementation

def convertToTitle(columnNumber: int) -> str:

&nbsp;   result = ""

&nbsp;   while columnNumber > 0:

&nbsp;       columnNumber -= 1

&nbsp;       remainder = columnNumber % 26

&nbsp;       result = chr(65 + remainder) + result

&nbsp;       columnNumber //= 26

&nbsp;   return result



🧪 Example Usage

print(convertToTitle(1))    # A

print(convertToTitle(26))   # Z

print(convertToTitle(27))   # AA

print(convertToTitle(52))   # AZ

print(convertToTitle(701))  # ZY

print(convertToTitle(702))  # ZZ

print(convertToTitle(703))  # AAA



📁 File Structure

excel-sheet-column-title/

│

├── convert\_to\_title.py   # Python implementation

└── README.md             # Documentation



✔️ Notes

\- The key insight is subtracting 1 before modulo.

\- This is a classic number‑to‑string conversion problem with a twist.

\- The solution is optimal and matches the official editorial

