Add Binary — Python Solution

📌 Problem Description

Given two binary strings a and b, return their sum as a binary string.

The input strings may be very long, so converting them to integers directly is not recommended.

Instead, the addition must be performed manually, bit by bit.

Examples

\- Input: a = "11", b = "1" → Output: "100"

\- Input: a = "1010", b = "1011" → Output: "10101"



💡 Approach

The solution performs binary addition from right to left, similar to how you would add numbers by hand.

Steps:

\- Initialize two pointers at the end of each string

\- Add corresponding bits plus any carry

\- Compute:

\- the new bit: total % 2

\- the new carry: total // 2

\- Append the bit to the result list

\- Reverse the result at the end

This approach avoids integer overflow and handles arbitrarily large binary strings.



🧠 Time \& Space Complexity

\- Time Complexity: O(n)

Each bit is processed once.

\- Space Complexity: O(n)

The result string requires additional space.



📝 Code Implementation

def addBinary(a: str, b: str) -> str:

&nbsp;   """

&nbsp;   Adds two binary strings and returns the result as a binary string.

&nbsp;   Processes digits from right to left and handles carry propagation.

&nbsp;   """

&nbsp;   result = \[]

&nbsp;   i, j = len(a) - 1, len(b) - 1

&nbsp;   carry = 0



&nbsp;   while i >= 0 or j >= 0 or carry:

&nbsp;       total = carry

&nbsp;       if i >= 0:

&nbsp;           total += int(a\[i])

&nbsp;           i -= 1

&nbsp;       if j >= 0:

&nbsp;           total += int(b\[j])

&nbsp;           j -= 1



&nbsp;       result.append(str(total % 2))

&nbsp;       carry = total // 2



&nbsp;   return ''.join(reversed(result))



🧪 Example Usage

print(addBinary("11", "1"))        # "100"

print(addBinary("1010", "1011"))   # "10101"

print(addBinary("0", "0"))         # "0"



📁 File Structure

add-binary/

│

├── add\_binary.py   # Python implementation

└── README.md       # Documentation



✔️ Notes

\- This is the optimal and most commonly accepted solution.

\- It avoids converting binary strings to integers, which is important for very large inputs.

\- Perfect for algorithm practice and LeetCode collections.

