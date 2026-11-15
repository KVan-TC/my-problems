---
code: FROG3
title: Atcoder Educational DP Contest Z - Frog 3
time_limit: 1.0s
memory_limit: 1024MB
tags:
    - dp
submit_url: https://oj.vnoi.info/problem/atcoder_dp_z
---

Có $N$ hòn đá được đánh số từ $1$ đến $N$. Với mỗi $i$ ($1 \le i \le N$), độ cao của hòn đá thứ $i$ là $h_i$, thỏa mãn $h_1 < h_2 < \dots < h_N$.

Có một chú ếch ban đầu đứng ở hòn đá $1$. Chú sẽ lặp lại hành động sau đây một số lần để đến được hòn đá $N$:

* Nếu chú ếch hiện đang ở hòn đá $i$, chú có thể nhảy đến một trong các hòn đá: $i + 1, i + 2, \dots, N$. Khi đó, chi phí phát sinh sẽ là $(h_j - h_i)^2 + C$, với $j$ là hòn đá mà chú đáp xuống.

**Yêu cầu:** Hãy tìm tổng chi phí tối thiểu có thể phát sinh để chú ếch di chuyển từ hòn đá $1$ đến hòn đá $N$.

## Input

* Dòng đầu tiên chứa hai số nguyên $N$ và $C$ ($2 \le N \le 2 \cdot 10^5$; $1 \le C \le 10^{12}$).
* Dòng thứ hai chứa $N$ số nguyên $h_1, h_2, \dots, h_N$ ($1 \le h_1 < h_2 < \dots < h_N \le 10^9$).

## Output

* In ra tổng chi phí tối thiểu có thể phát sinh.

## Sample Input 1

```text
5 6
1 2 3 4 5

```

## Sample Output 1

```text
20

```

## Sample Input 2

```text
2 1000000000000
500000 1000000

```

## Sample Output 2

```text
1250000000000

```

## Sample Input 3

```text
8 5
1 3 4 5 10 11 12 13

```

## Sample Output 3

```text
62

```

## Notes

Ở ví dụ 1:

* Nếu đi theo lộ trình $1 \to 3 \to 5$, tổng chi phí phát sinh là $\big((3 - 1)^2 + 6\big) + \big((5 - 3)^2 + 6\big) = 20$.

Ở ví dụ 2:

* Nếu đi theo lộ trình $1 \to 2$, tổng chi phí phát sinh là $(1000000 - 500000)^2 + 1000000000000 = 1250000000000$.

Ở ví dụ 3:

* Nếu đi theo lộ trình $1 \to 2 \to 4 \to 5 \to 8$, tổng chi phí phát sinh là $\big((3 - 1)^2 + 5\big) + \big((5 - 3)^2 + 5\big) + \big((10 - 5)^2 + 5\big) + \big((13 - 10)^2 + 5\big) = 62$.
