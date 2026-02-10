Best Time to Buy and Sell Stock — Python Solution

📌 Problem Description

You are given an array prices where prices\[i] is the price of a stock on day i.

Your task is to maximize profit by choosing a single day to buy and a different day in the future to sell.

If no profit can be made, return 0.

Examples

\- Input: \[7,1,5,3,6,4]

Output: 5

Explanation: Buy at 1, sell at 6.

\- Input: \[7,6,4,3,1]

Output: 0

Explanation: No profitable transaction possible.



💡 Approach

This is a classic one‑pass problem.

We track:

\- the minimum price so far (best day to buy)

\- the maximum profit so far (best sell after that buy)

For each price:

\- Update the minimum price if the current price is lower

\- Otherwise, compute the profit if sold today

\- Update the maximum profit if this profit is higher

This ensures optimal performance in a single linear scan.



🧠 Time \& Space Complexity

\- Time Complexity: O(n)

Only one pass through the list.

\- Space Complexity: O(1)

Only two variables are used.

This is the optimal solution.



📝 Code Implementation

def max\_profit(prices: list\[int]) -> int:

&nbsp;   """

&nbsp;   Returns the maximum profit achievable from a single buy-sell transaction.

&nbsp;   Uses a one-pass approach tracking the minimum price and maximum profit.

&nbsp;   """

&nbsp;   min\_price = float('inf')

&nbsp;   max\_profit = 0



&nbsp;   for price in prices:

&nbsp;       if price < min\_price:

&nbsp;           min\_price = price

&nbsp;       elif price - min\_price > max\_profit:

&nbsp;           max\_profit = price - min\_price



&nbsp;   return max\_profit



🧪 Example Usage

print(max\_profit(\[7, 1, 5, 3, 6, 4]))  # 5

print(max\_profit(\[7, 6, 4, 3, 1]))      # 0

print(max\_profit(\[2, 4, 1]))            # 2



📁 File Structure

best-time-to-buy-and-sell-stock/

│

├── max\_profit.py   # Python implementation

└── README.md       # Documentation



✔️ Notes

\- This is the optimal O(n) solution.

\- Avoids the naive O(n²) approach of checking all buy/sell pairs.

\- A foundational problem for understanding sliding windows and greedy strategies.

