Roman to Integer — Python Solution

📌 Problem Description

Given a Roman numeral string s, convert it into an integer.

Roman numerals are based on seven symbols:

| Symbol | Value | 

| I      | 1     | 

| V      | 5     | 

| X      | 10    | 

| L      | 50    | 

| C      | 100   | 

| D      | 500   | 

| M      | 1000  | 



In most cases, numerals are added together.

However, in subtractive notation, a smaller numeral placed before a larger one is subtracted:

\- IV = 4

\- IX = 9

\- XL = 40

\- XC = 90

\- CD = 400

\- CM = 900

The goal is to correctly interpret these rules and compute the integer value.



💡 Approach

The solution processes the Roman numeral from right to left.

For each character:

\- Convert it to its numeric value.

\- Compare it with the previously processed value.

\- If the current value is smaller, subtract it (subtractive case).

\- Otherwise, add it.

This method naturally handles all subtractive pairs without needing special cases.



🧠 Time \& Space Complexity

\- Time Complexity: O(n)

We traverse the string once.

\- Space Complexity: O(1)

Only a few variables are used.



📝 Code Implementation

def romanToInt(s: str) -> int:

&nbsp;   """

&nbsp;   Converts a Roman numeral string into an integer.

&nbsp;   Uses reverse traversal to handle subtractive notation efficiently.

&nbsp;   """

&nbsp;   values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

&nbsp;   total = 0

&nbsp;   prev\_value = 0



&nbsp;   for char in reversed(s):

&nbsp;       value = values\[char]

&nbsp;       if value < prev\_value:

&nbsp;           total -= value

&nbsp;       else:

&nbsp;           total += value

&nbsp;       prev\_value = value



&nbsp;   return total







🧪 Example Usage

print(romanToInt("III"))      # 3

print(romanToInt("LVIII"))    # 58

print(romanToInt("MCMXCIV"))  # 1994



📁 File Structure

roman-to-integer/

│

├── roman\_to\_int.py   # Python implementation

└── README.md          # Documentation



✔️ Notes

\- This is one of the most efficient and clean solutions for this problem.

\- Reverse traversal avoids complex conditional logic.

\- Ideal for algorithm practice and LeetCode collections.



