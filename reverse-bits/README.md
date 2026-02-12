Reverse Bits — Python Solution

📌 Problem Description

Given a 32‑bit unsigned integer n, return the integer that results from reversing its bits.

Example:

Input:  n = 00000010100101000001111010011100

Output:    00111001011110000010100101000000



The output must also be interpreted as a 32‑bit unsigned integer.



💡 Approach

The algorithm processes the number bit‑by‑bit:

\- Initialize result = 0

\- Loop exactly 32 times (because the input is a 32‑bit integer)

\- In each iteration:

\- Extract the lowest bit of n using n \& 1

\- Shift result left by 1 to make room for the new bit

\- Add the extracted bit to result

\- Shift n right by 1 to process the next bit

This effectively builds the reversed bit sequence from left to right.



🧠 Time \& Space Complexity

\- Time Complexity: O(1)

Always exactly 32 iterations.

\- Space Complexity: O(1)

Only two integers are used.

This is the optimal solution.



📝 Code Implementation

def reverseBits(n: int) -> int:

&nbsp;   result = 0

&nbsp;   for \_ in range(32):

&nbsp;       result = (result << 1) | (n \& 1)

&nbsp;       n >>= 1

&nbsp;   return result



🧪 Example Usage

print(reverseBits(43261596))

\# Expected: 964176192



print(reverseBits(4294967293))

\# Expected: 3221225471



📁 File Structure

reverse-bits/

│

├── reverse\_bits.py   # Python implementation

└── README.md         # Documentation



✔️ Notes

\- The solution strictly follows the 32‑bit requirement.

\- Bitwise operations make this approach extremely fast.

\- No Python‑specific tricks are needed; this is a clean, low‑level solution

