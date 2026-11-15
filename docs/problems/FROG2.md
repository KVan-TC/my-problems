---
code: FROG2
title: Atcoder Educational DP Contest B - Frog 2
time_limit: 1.0s
memory_limit: 1024MB
tags:
    - dp
submit_url: https://oj.vnoi.info/problem/atcoder_dp_b
---

Có $N$ hòn đá được đánh số từ $1$ đến $N$. Với mỗi $i$ ($1 \le i \le N$), độ cao của hòn đá thứ $i$ là $h_i$.

Có một chú ếch ban đầu đứng ở hòn đá $1$. Chú sẽ lặp lại hành động sau đây một số lần để đến được hòn đá $N$:

* Nếu chú ếch hiện đang ở hòn đá $i$, chú có thể nhảy đến một trong các hòn đá: $i + 1, i + 2, \dots, i + K$. Khi đó, chi phí phát sinh sẽ là $\vert{}h_i - h_j\vert{}$, với $j$ là hòn đá mà chú đáp xuống.

**Yêu cầu:** Hãy tìm tổng chi phí tối thiểu có thể phát sinh để chú ếch di chuyển từ hòn đá $1$ đến hòn đá $N$.

## Input

* Dòng đầu tiên chứa hai số nguyên $N$ và $K$ ($2 \le N \le 10^5$; $1 \le K \le 100$).
* Dòng thứ hai chứa $N$ số nguyên $h_1, h_2, \dots, h_N$ ($1 \le h_i \le 10^4$).

## Output

* In ra tổng chi phí tối thiểu có thể phát sinh.

## Sample Input 1

```text
5 3
10 30 40 50 20

```

## Sample Output 1

```text
30

```

## Sample Input 2

```text
3 1
10 20 10

```

## Sample Output 2

```text
20

```

## Sample Input 3

```text
2 100
10 10

```

## Sample Output 3

```text
0

```

## Sample Input 4

```text
10 4
40 10 20 70 80 10 20 70 80 60

```

## Sample Output 4

```text
40

```

## Notes

Ở ví dụ 1:

* Nếu đi theo lộ trình $1 \to 2 \to 5$, tổng chi phí phát sinh là $\vert{}10 - 30\vert{} + \vert{}30 - 20\vert{} = 30$.

Ở ví dụ 2:

* Nếu đi theo lộ trình $1 \to 2 \to 3$, tổng chi phí phát sinh là $\vert{}10 - 20\vert{} + \vert{}20 - 10\vert{} = 20$.

Ở ví dụ 3:

* Nếu đi theo lộ trình $1 \to 2$, tổng chi phí phát sinh là $\vert{}10 - 10\vert{} = 0$.

Ở ví dụ 4:

* Nếu đi theo lộ trình $1 \to 4 \to 8 \to 10$, tổng chi phí phát sinh là $\vert{}40 - 70\vert{} + \vert{}70 - 70\vert{} + \vert{}70 - 60\vert{} = 40$.
