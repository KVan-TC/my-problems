---
code: FIBONACCI
title: Số Fibonacci
time_limit: 1.0s
memory_limit: 1024MB
tags:
    - dp
submit_url:
---

Dãy số Fibonacci $f_1, f_2, f_3, \dots$ được định nghĩa như sau:

$$f_1 = 1, \quad f_2 = 1, \quad f_i = f_{i-1} + f_{i-2} \quad (\forall i > 2)$$

**Yêu cầu:** Cho một số nguyên dương $n$, hãy tính giá trị của $f_n$. Do kết quả có thể rất lớn, hãy in ra phần dư của $f_n$ khi chia cho $10^9 + 7$.

## Input

* Dòng duy nhất chứa một số nguyên dương $n$ ($1 \le n \le 10^6$).

## Output

* In ra một số nguyên duy nhất là phần dư của $f_n$ khi chia cho $10^9 + 7$.

## Sample Input 1

```text
3

```

## Sample Output 1

```text
2

```

## Sample Input 2

```text
4

```

## Sample Output 2

```text
3

```

## Notes

Ở ví dụ 1:

* Với $n = 3$, ta có $f_3 = f_2 + f_1 = 1 + 1 = 2$.

Ở ví dụ 2:

* Với $n = 4$, ta có $f_4 = f_3 + f_2 = 2 + 1 = 3$.
