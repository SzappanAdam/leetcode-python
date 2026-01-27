Valid Parentheses — Python Solution

📌 Problem Description

Given a string s containing only the characters:

\- (, )

\- \[, ]

\- {, }

determine whether the input string is valid.

A string is valid if:

\- Every opening bracket has a corresponding closing bracket of the same type

\- Brackets close in the correct order

\- No unmatched or extra brackets remain

Examples

\- "()" → valid

\- "()\[]{}" → valid

\- "(]" → invalid

\- "(\[)]" → invalid

\- "{\[]}" → valid



💡 Approach

The solution uses a stack to track expected closing brackets.

For each character:

\- If it is an opening bracket, push the corresponding closing bracket onto the stack

\- If it is a closing bracket:

\- If the stack is empty → invalid

\- If it does not match the top of the stack → invalid

\- At the end, the string is valid only if the stack is empty

This method ensures correct ordering and matching of brackets.



🧠 Time \& Space Complexity

\- Time Complexity: O(n)

Each character is processed once.

\- Space Complexity: O(n)

In the worst case, all opening brackets are stored in the stack.



📝 Code Implementation

def is\_valid\_parentheses(s: str) -> bool:

&nbsp;   """

&nbsp;   Returns True if the input string contains valid parentheses.

&nbsp;   Uses a stack to match opening and closing brackets.

&nbsp;   """

&nbsp;   stack = \[]



&nbsp;   for ch in s:

&nbsp;       if ch == '(':

&nbsp;           stack.append(')')

&nbsp;       elif ch == '\[':

&nbsp;           stack.append(']')

&nbsp;       elif ch == '{':

&nbsp;           stack.append('}')

&nbsp;       elif not stack or ch != stack.pop():

&nbsp;           return False



&nbsp;   return not stack



🧪 Example Usage

print(is\_valid\_parentheses("()"))        # True

print(is\_valid\_parentheses("()\[]{}"))    # True

print(is\_valid\_parentheses("(]"))        # False

print(is\_valid\_parentheses("(\[)]"))      # False

print(is\_valid\_parentheses("{\[]}"))      # True



📁 File Structure

valid-parentheses/

│

├── is\_valid\_parentheses.py   # Python implementation

└── README.md                 # Documentation



✔️ Notes

\- This is one of the most efficient and elegant solutions for this problem.

\- Using expected closing brackets simplifies the logic.

\- Ideal for algorithm practice and LeetCode collections.



