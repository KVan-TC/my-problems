---
code: KNAPSACK1
title: Atcoder Educational DP Contest D - Knapsack 1
time_limit: 1.0s
memory_limit: 1024MB
tags:
    - dp
submit_url: https://oj.vnoi.info/problem/atcoder_dp_d
---

Có $N$ đồ vật được đánh số từ $1$ đến $N$. Với mỗi $i$ ($1 \le i \le N$), đồ vật thứ $i$ có trọng lượng là $w_i$ và giá trị là $v_i$.

Taro quyết định chọn một số đồ vật trong $N$ đồ vật đã cho để mang về nhà trong một chiếc túi. Sức chứa tối đa của chiếc túi là $W$, nghĩa là tổng trọng lượng của các đồ vật được chọn không được vượt quá $W$.

**Yêu cầu:** Hãy tìm tổng giá trị lớn nhất có thể đạt được của các đồ vật mà Taro mang về nhà.

## Input

* Dòng đầu tiên chứa hai số nguyên $N$ và $W$ ($1 \le N \le 1000$; $1 \le W \le 10^5$).
* Trong $N$ dòng tiếp theo, dòng thứ $i$ chứa hai số nguyên $w_i$ và $v_i$ ($1 \le w_i \le W$; $1 \le v_i \le 10^9$).

## Output

* In ra tổng giá trị lớn nhất có thể đạt được của các đồ vật mà Taro mang về nhà.

## Sample Input 1

```text
3 8
3 30
4 50
5 60

```

## Sample Output 1

```text
90

```

## Sample Input 2

```text
5 5
1 1000000000
1 1000000000
1 1000000000
1 1000000000
1 1000000000

```

## Sample Output 2

```text
5000000000

```

## Sample Input 3

```text
6 15
6 5
5 6
6 4
6 6
3 5
7 2

```

## Sample Output 3

```text
17

```

## Notes

Ở ví dụ 1:

* Nên chọn đồ vật $1$ và $3$. Khi đó, tổng trọng lượng là $3 + 5 = 8$, và tổng giá trị là $30 + 60 = 90$.

Ở ví dụ 2:

* Đáp án có thể không vừa với kiểu số nguyên $32$-bit.

Ở ví dụ 3:

* Nên chọn đồ vật $2, 4$ và $5$. Khi đó, tổng trọng lượng là $5 + 6 + 3 = 14$, và tổng giá trị là $6 + 6 + 5 = 17$.
