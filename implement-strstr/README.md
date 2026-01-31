📄 README.md — Implement strStr()

📌 Problem Description

Implement the function strStr(haystack, needle).

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

If needle is an empty string, return 0.

Examples

\- Input: "sadbutsad", "sad" → Output: 0

\- Input: "leetcode", "leeto" → Output: -1

\- Input: "hello", "ll" → Output: 2



💡 Approach (Primary Solution — Sliding Window)

The algorithm checks each possible starting position in haystack and compares the substring with needle.

Steps:

\- If needle is empty → return 0

\- Slide a window of size len(needle) across haystack

\- Compare each substring with needle

\- If a match is found → return the index

\- If no match exists → return -1

This is the standard O(n·m) solution expected in interviews.



🧠 Time \& Space Complexity

\- Time Complexity: O(n · m)

where n = length of haystack, m = length of needle

\- Space Complexity: O(1)



📝 Code Implementation (Primary Solution)

def strStr(haystack: str, needle: str) -> int:

&nbsp;   """

&nbsp;   Returns the index of the first occurrence of `needle` in `haystack`,

&nbsp;   or -1 if `needle` is not found.

&nbsp;   """

&nbsp;   m, n = len(needle), len(haystack)



&nbsp;   if m == 0:

&nbsp;       return 0



&nbsp;   for i in range(n - m + 1):

&nbsp;       if haystack\[i:i + m] == needle:

&nbsp;           return i



&nbsp;   return -1



🧪 Example Usage

print(strStr("sadbutsad", "sad"))   # 0

print(strStr("leetcode", "leeto"))  # -1

print(strStr("hello", "ll"))        # 2



🔄 Alternative Pythonic Solution (Using str.find())

Python provides a built‑in method that solves the problem directly.

def strStr(haystack: str, needle: str) -> int:

&nbsp;   return haystack.find(needle)



This is concise and valid on LeetCode, but the primary solution above is preferred for interviews and algorithm practice.



📁 File Structure

implement-strstr/

│

├── strstr.py     # Python implementation (both solutions included)

└── README.md     # Documentation



✔️ Notes

\- The sliding‑window solution is the recommended one for interviews.

\- The find() method is a clean Python shortcut but not algorithmic.

\- Both solutions pass all LeetCode test cases.



