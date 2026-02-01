Climbing Stairs — Python Solution

📌 Problem Description

You are climbing a staircase with n steps.

Each time you can climb 1 or 2 steps.

Your task is to return the number of distinct ways you can reach the top.

This is a classic dynamic programming problem that reduces to computing the Fibonacci sequence.

Examples

\- Input: n = 2 → Output: 2

(1+1, 2)

\- Input: n = 3 → Output: 3

(1+1+1, 1+2, 2+1)

\- Input: n = 5 → Output: 8



💡 Approach

The number of ways to reach step n is:

f(n)=f(n-1)+f(n-2)

Because:

\- To reach step n, you either came from step n-1 (1 step)

\- Or from step n-2 (2 steps)

This is exactly the Fibonacci sequence.

To optimize space, the solution keeps only the last two computed values instead of storing the whole DP array.



🧠 Time \& Space Complexity

\- Time Complexity: O(n)

A single loop computes the result.

\- Space Complexity: O(1)

Only two variables are maintained.



📝 Code Implementation

def climbStairs(n: int) -> int:

&nbsp;   """

&nbsp;   Returns the number of distinct ways to climb to the top.

&nbsp;   Uses Fibonacci logic with O(1) space.

&nbsp;   """

&nbsp;   if n <= 2:

&nbsp;       return n



&nbsp;   first, second = 1, 2



&nbsp;   for \_ in range(3, n + 1):

&nbsp;       first, second = second, first + second



&nbsp;   return second



🧪 Example Usage

print(climbStairs(2))  # 2

print(climbStairs(3))  # 3

print(climbStairs(5))  # 8



📁 File Structure

climbing-stairs/

│

├── climb\_stairs.py   # Python implementation

└── README.md         # Documentation



✔️ Notes

\- This is the optimal solution for this problem.

\- The Fibonacci pattern appears frequently in dynamic programming.

\- Perfect for algorithm practice and LeetCode collections.

