# Sales simulator application

This is a simple sales simulator application written in Python. This logic of this application is basically one way to implement one discount calculator. doesn't have a database, so the data is stored in memory and is cleaned when the app stop to run.

## Base for discount calculation

The discount is calculated based on the following table:

| Units   | Discount |
| ------- | -------- |
| 4       | 0%       |
| 5 - 19  | 3%       |
| 20 - 99 | 6%       |
| 100...  | 10%      |

The discount is applied to the total price of the order.
