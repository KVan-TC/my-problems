---
code: MAXSUM2
title: Tổng đoạn con lớn nhất 2
time_limit: 1.0s
memory_limit: 512MB
tags:
    - dp
    - prefix-sums
submit_url: https://cses.fi/problemset/task/1644
---

Cho một dãy số nguyên $x_1, x_2, \dots, x_n$ gồm $n$ phần tử và hai số nguyên dương $a, b$. Một đoạn con liên tiếp hợp lệ của dãy là một dãy các phần tử liên tiếp $x_l, x_{l+1}, \dots, x_r$ ($1 \le l \le r \le n$) có độ dài nằm trong đoạn $[a, b]$, tức là thỏa mãn $a \le r - l + 1 \le b$.

**Yêu cầu:** Hãy tìm tổng lớn nhất của các giá trị trong một đoạn con liên tiếp hợp lệ của dãy đã cho.

## Input

* Dòng đầu tiên chứa ba số nguyên dương $n$, $a$ và $b$ ($1 \le a \le b \le n \le 2 \cdot 10^5$) — kích thước của dãy số và giới hạn độ dài tối thiểu, tối đa của đoạn con.
* Dòng thứ hai chứa $n$ số nguyên $x_1, x_2, \dots, x_n$ ($-10^9 \le x_i \le 10^9$), các số cách nhau bởi một khoảng trắng.

## Output

* In ra một số nguyên duy nhất là tổng lớn nhất tìm được.

## Sample Input 1

```text
8 1 2
-1 3 -2 5 3 -5 2 2

```

## Sample Output 1

```text
8

```

## Notes

Ở ví dụ 1:

* Dãy ban đầu là $x = [-1, 3, -2, 5, 3, -5, 2, 2]$ gồm $n = 8$ phần tử, yêu cầu đoạn con có độ dài từ $a = 1$ đến $b = 2$.
* Đoạn con liên tiếp hợp lệ có tổng lớn nhất là $(5, 3)$ (từ vị trí $4$ đến vị trí $5$, có độ dài $2 \in [1, 2]$) với tổng giá trị là $5 + 3 = 8$.
