Length of Last Word — Python Solution

📌 Problem Description

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is defined as a maximal substring consisting of non‑space characters only.

Examples

\- Input: "Hello World" → Output: 5

\- Input: "   fly me   to   the moon  " → Output: 4

\- Input: "luffy is still joyboy" → Output: 6



💡 Approach (Primary Solution — Manual Scan)

The optimal solution scans the string from the end, skipping trailing spaces, then counting characters until the next space.

Steps:

\- Start from the last character

\- Skip all spaces

\- Count characters until a space or the beginning of the string

This approach uses O(1) extra memory and runs in O(n) time.



🧠 Time \& Space Complexity

\- Time Complexity: O(n)

\- Space Complexity: O(1)



📝 Code Implementation (Primary Solution)

def lengthOfLastWord(s: str) -> int:

&nbsp;   """

&nbsp;   Returns the length of the last word in the string.

&nbsp;   Scans from the end for optimal O(1) space usage.

&nbsp;   """

&nbsp;   i = len(s) - 1

&nbsp;   length = 0



&nbsp;   # Skip trailing spaces

&nbsp;   while i >= 0 and s\[i] == ' ':

&nbsp;       i -= 1



&nbsp;   # Count characters of the last word

&nbsp;   while i >= 0 and s\[i] != ' ':

&nbsp;       length += 1

&nbsp;       i -= 1



&nbsp;   return length



🔄 Alternative Pythonic Solution

def lengthOfLastWord(s: str) -> int:

&nbsp;   s = s.rstrip()

&nbsp;   return len(s.split()\[-1])





This version is concise and readable, but uses extra memory due to split().



🧪 Example Usage

print(lengthOfLastWord("   fly me   to   the moon  "))  # 4

print(lengthOfLastWord("Hello World"))                  # 5

print(lengthOfLastWord("luffy is still joyboy"))        # 6



📁 File Structure

length-of-last-word/

│

├── length\_of\_last\_word.py   # Python implementation

└── README.md                # Documentation



✔️ Notes

\- The manual scan solution is optimal and interview‑friendly.

\- The Pythonic version is elegant but uses extra memory.

\- Both pass all LeetCode test cases.



