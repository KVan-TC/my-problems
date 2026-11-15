---
code: FROG1
title: Atcoder Educational DP Contest A - Frog 1
time_limit: 1.0s
memory_limit: 1024MB
tags:
    - dp
submit_url: https://oj.vnoi.info/problem/atcoder_dp_a
---

Có $N$ hòn đá được đánh số từ $1$ đến $N$. Với mỗi $i$ ($1 \le i \le N$), độ cao của hòn đá thứ $i$ là $h_i$.

Có một chú ếch ban đầu đứng ở hòn đá $1$. Chú sẽ lặp lại hành động sau đây một số lần để đến được hòn đá $N$:

Nếu chú ếch hiện đang ở hòn đá $i$, chú có thể nhảy đến hòn đá $i + 1$ hoặc hòn đá $i + 2$. Khi đó, chi phí phát sinh sẽ là $\vert{}h_i - h_j\vert{}$, với $j$ là hòn đá mà chú đáp xuống.

**Yêu cầu:** Hãy tìm tổng chi phí tối thiểu có thể phát sinh để chú ếch di chuyển từ hòn đá $1$ đến hòn đá $N$.

## Input

* Dòng đầu tiên chứa một số nguyên $N$ ($2 \le N \le 10^6$).
* Dòng thứ hai chứa $N$ số nguyên $h_1, h_2, \dots, h_N$ ($1 \le h_i \le 10^9$).

## Output

* In ra tổng chi phí tối thiểu có thể phát sinh.

## Sample Input 1

```text
4
10 30 40 20

```

## Sample Output 1

```text
30

```

## Sample Input 2

```text
2
10 10

```

## Sample Output 2

```text
0

```

## Sample Input 3

```text
6
30 10 60 10 60 50

```

## Sample Output 3

```text
40

```

## Notes

Ở ví dụ 1:

* Nếu đi theo lộ trình $1 \to 2 \to 4$, tổng chi phí phát sinh là $\vert{}10 - 30\vert{} + \vert{}30 - 20\vert{} = 30$.

Ở ví dụ 2:

* Nếu đi theo lộ trình $1 \to 2$, tổng chi phí phát sinh là $\vert{}10 - 10\vert{} = 0$.

Ở ví dụ 3:

* Nếu đi theo lộ trình $1 \to 3 \to 5 \to 6$, tổng chi phí phát sinh là $\vert{}30 - 60\vert{} + \vert{}60 - 60\vert{} + \vert{}60 - 50\vert{} = 40$.
