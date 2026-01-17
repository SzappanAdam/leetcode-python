Palindrome Number — Python Solution

📌 Problem Description

Given an integer x, determine whether it is a palindrome.

A palindrome number reads the same forward and backward.

Examples:

\- 121 → palindrome

\- -121 → not a palindrome (negative sign breaks symmetry)

\- 10 → not a palindrome

This is a classic LeetCode problem that tests basic logic and string manipulation.



💡 Approach

The simplest and most readable solution is to:

\- Immediately return False for negative numbers

\- Convert the number to a string

\- Compare the string with its reversed version using slicing (\[::-1])

This approach is clean, intuitive, and efficient for typical input sizes.



🧠 Time \& Space Complexity

\- Time Complexity: O(n)

where n is the number of digits in the integer

\- Space Complexity: O(n)

due to converting the number to a string



🧪 Example Usage

from is\_palindrome import is\_palindrome



print(is\_palindrome(121))        # True

print(is\_palindrome(-121))       # False

print(is\_palindrome(10))         # False

print(is\_palindrome(123454321))  # True



📝 Code Implementation

def is\_palindrome(x: int) -> bool:

    """

    Returns True if x is a palindrome number.

    Negative numbers are not considered palindromes.

    """

    if x < 0:

        return False

    return str(x) == str(x)\[::-1]



📁 File Structure

palindrome-number/

│

├── is\_palindrome.py   # Python implementation

└── README.md           # Documentation



✔️ Notes

\- This is the simplest and most readable solution.

\- A non-string mathematical solution also exists, but this version is perfectly acceptable for interviews and practice.

\- Ideal for algorithm collections and LeetCode repositories.

