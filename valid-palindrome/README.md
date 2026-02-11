Valid Palindrome — Python Solution

Problem Description

Given a string s, determine whether it is a palindrome, considering only alphanumeric characters and ignoring case.

A palindrome reads the same forward and backward after filtering out non‑alphanumeric characters.

Examples

\- Input: "A man, a plan, a canal: Panama"

Output: True

\- Input: "race a car"

Output: False

\- Input: " "

Output: True



Approach

There are two standard approaches to solve this problem efficiently:

Approach 1 — Filter and Reverse (Simple and Clean)

\- Remove all non‑alphanumeric characters

\- Convert everything to lowercase

\- Check if the string equals its reverse

This is the most readable solution and leverages Python’s strengths.

Approach 2 — Two‑Pointer Technique (Optimized)

\- Use two pointers (left and right)

\- Skip non‑alphanumeric characters

\- Compare characters while moving inward

This avoids creating a new string and uses O(1) extra memory.

Both solutions run in O(n) time.



Time \& Space Complexity

|  |  |  |  | 

|  |  |  |  | 

|  |  |  |  | 



Code Implementation

Solution 1 — Filter and Reverse

def isPalindrome(s: str) -> bool:

&nbsp;   filtered = ''.join(ch.lower() for ch in s if ch.isalnum())

&nbsp;   return filtered == filtered\[::-1]



Solution 2 — Two‑Pointer Technique (Optimized)

def isPalindrome(s: str) -> bool:

&nbsp;   left, right = 0, len(s) - 1



&nbsp;   while left < right:

&nbsp;       while left < right and not s\[left].isalnum():

&nbsp;           left += 1

&nbsp;       while left < right and not s\[right].isalnum():

&nbsp;           right -= 1



&nbsp;       if s\[left].lower() != s\[right].lower():

&nbsp;           return False



&nbsp;       left += 1

&nbsp;       right -= 1



&nbsp;   return True



Example Usage

print(isPalindrome("A man, a plan, a canal: Panama"))  # True

print(isPalindrome("race a car"))                      # False

print(isPalindrome(" "))                               # True



File Structure

valid-palindrome/

│

├── is\_palindrome.py   # Python implementations

└── README.md          # Documentation



Notes

\- Both solutions are correct and accepted.

\- The two‑pointer version is optimal in terms of memory usage.

\- This problem is a classic introduction to string sanitization and pointer techniques.

