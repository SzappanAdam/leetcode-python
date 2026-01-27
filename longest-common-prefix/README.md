Longest Common Prefix — Python Solution

📌 Problem Description

Given an array of strings strs, return the longest common prefix shared among all strings in the list.

If no common prefix exists, return an empty string.

Examples

\- \["flower", "flow", "flight"] → "fl"

\- \["dog", "racecar", "car"] → "" (no common prefix)

This is a classic string‑processing problem on LeetCode.



💡 Approach

The solution starts by assuming the first string is the prefix.

Then, for each subsequent string:

\- While the current string does not start with the prefix

\- Shorten the prefix by removing the last character

\- If the prefix becomes empty, return ""

This method ensures we always maintain the longest valid prefix seen so far.



🧠 Time \& Space Complexity

\- Time Complexity: O(n · m)

where n = number of strings, m = length of the shortest string

\- Space Complexity: O(1)

only the prefix variable is used



📝 Code Implementation

def longest\_common\_prefix(strs: list\[str]) -> str:

&nbsp;   """

&nbsp;   Returns the longest common prefix among a list of strings.

&nbsp;   If no common prefix exists, returns an empty string.

&nbsp;   """

&nbsp;   if not strs:

&nbsp;       return ""



&nbsp;   prefix = strs\[0]



&nbsp;   for s in strs\[1:]:

&nbsp;       while not s.startswith(prefix):

&nbsp;           prefix = prefix\[:-1]

&nbsp;           if prefix == "":

&nbsp;               return ""

&nbsp;   return prefix



🧪 Example Usage

print(longest\_common\_prefix(\["flower", "flow", "flight"]))  # "fl"

print(longest\_common\_prefix(\["dog", "racecar", "car"]))     # ""

print(longest\_common\_prefix(\["interspecies", "interstellar", "interstate"]))  # "inters"



📁 File Structure

longest-common-prefix/

│

├── longest\_common\_prefix.py   # Python implementation

└── README.md                  # Documentation



✔️ Notes

\- This is a clean and widely accepted solution for this problem.

\- The startswith() method keeps the logic simple and readable.

\- Ideal for algorithm practice and LeetCode collections.



