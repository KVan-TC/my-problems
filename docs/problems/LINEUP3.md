---
code: LINEUP3
title: Giao lưu 3
time_limit: 1.0s
memory_limit: 1024MB
tags:
    - dp
submit_url:
---

Có $n$ học sinh (gồm cả nam và nữ) được xếp thành một hàng dọc và đánh số từ $1$ đến $n$. Cho một số nguyên không âm $k$, một cách xếp hàng được gọi là *hợp lệ* nếu giữa hai bạn nam bất kỳ trong hàng có ít nhất $k$ bạn nữ đứng ngăn cách giữa họ. Hai cách xếp hàng được coi là khác nhau nếu tồn tại ít nhất một vị trí có giới tính của học sinh đứng ở vị trí đó khác nhau.

**Yêu cầu:** Hãy đếm số cách xếp hàng hợp lệ. Vì kết quả có thể rất lớn, hãy in ra phần dư của kết quả khi chia cho $10^9 + 7$.

## Input

* Dòng duy nhất chứa hai số nguyên $n$ và $k$ ($1 \le n \le 10^6$; $0 \le k \le n$).

## Output

* In ra một số nguyên duy nhất là số cách xếp hàng hợp lệ sau khi chia dư cho $10^9 + 7$.

## Sample Input 1

```text
4 2

```

## Sample Output 1

```text
6

```

## Notes

Ở ví dụ 1:

* Với $n = 4$ và $k = 2$, ký hiệu $0$ là bạn nữ và $1$ là bạn nam, giữa hai bạn nam bất kỳ phải có ít nhất $2$ bạn nữ đứng ngăn cách.
* Có $6$ cách xếp hàng hợp lệ gồm: $(0, 0, 0, 0)$, $(1, 0, 0, 0)$, $(0, 1, 0, 0)$, $(0, 0, 1, 0)$, $(0, 0, 0, 1)$, $(1, 0, 0, 1)$.
