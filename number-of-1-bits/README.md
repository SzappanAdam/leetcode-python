Number of 1 Bits (Hamming Weight) — Python Solution

Problem Description

Given a 32‑bit unsigned integer n, return the number of 1 bits in its binary representation.

This count is known as the Hamming weight.

Examples

\- Input: 00000000000000000000000000001011

Output: 3

\- Input: 00000000000000000000000010000000

Output: 1

\- Input: 11111111111111111111111111111101

Output: 31



Approach

There are two classic approaches to solve this problem efficiently.



Approach 1 — Bit-by-Bit Check

This method repeatedly checks the least significant bit using n \& 1, then right‑shifts the number.

Logic

\- Extract the lowest bit

\- Add it to the count

\- Shift the number right

\- Repeat until n becomes zero

Complexity

\- Time: O(32) — fixed number of iterations

\- Space: O(1)

Code

def hammingWeight(n: int) -> int:

&nbsp;   count = 0

&nbsp;   while n:

&nbsp;       count += n \& 1

&nbsp;       n >>= 1

&nbsp;   return count



Approach 2 — Brian Kernighan’s Algorithm (Optimal)

This algorithm removes the lowest set bit (1) in each iteration using:

n \&= (n - 1)



Each iteration eliminates exactly one 1 bit.

Logic

\- Subtracting 1 flips all bits after the lowest set bit

\- AND-ing with the original number clears that lowest set bit

\- Repeat until n becomes zero

\- Count how many times this happens

Complexity

\- Time: O(k), where k = number of set bits

\- Space: O(1)

This is the optimal solution.

Code

def hammingWeight(n: int) -> int:

&nbsp;   count = 0

&nbsp;   while n:

&nbsp;       n \&= (n - 1)

&nbsp;       count += 1

&nbsp;   return count



Example Usage

print(hammingWeight(0b1011))        # 3

print(hammingWeight(0b10000000))    # 1

print(hammingWeight(0b11111101))    # 7



File Structure

number-of-1-bits/

│

├── hamming\_weight.py   # Python implementations

└── README.md           # Documentation



Notes

\- The bit‑by‑bit method is simple and reliable.

\- Brian Kernighan’s algorithm is more efficient when the number has few set bits.

\- Both solutions run in constant space.

