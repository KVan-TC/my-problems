---
code: PATHMED
title: Trung vị chênh lệch trên đường đi cây
time_limit: 2.0s
memory_limit: 256MB
tags:
    - trees
    - data-structures
    - segment-tree
    - binary-search
submit_url:
---

Cho một cây gồm $n$ đỉnh được đánh số từ $1$ đến $n$ và $n - 1$ cạnh vô hướng. Đỉnh thứ $i$ ($1 \le i \le n$) có trọng số nguyên dương $a_i$.

Cần xử lý lần lượt $q$ truy vấn trực tuyến. Ở mỗi truy vấn, bạn được cho hai số nguyên $u'$ và $v'$. Gọi $last\_ans$ là kết quả của truy vấn liền trước đó (với truy vấn đầu tiên, khởi tạo $last\_ans = 0$). Hai đỉnh thực tế của truy vấn được giải mã theo công thức:

$$u = ((u' \oplus last\_ans) \bmod n) + 1$$

$$v = ((v' \oplus last\_ans) \bmod n) + 1$$

trong đó $\oplus$ là phép toán XOR theo từng bit.

Xét đường đi đơn duy nhất nối từ đỉnh $u$ đến đỉnh $v$ trên cây, giả sử đường đi này đi qua $m$ đỉnh và danh sách trọng số của các đỉnh đó sau khi sắp xếp theo thứ tự không giảm là $w_1 \le w_2 \le \dots \le w_m$.

Ta định nghĩa độ lệch trung vị của đường đi $(u, v)$ là giá trị nhỏ nhất của biểu thức:

$$\sum_{i=1}^{m} \vert{}w_i - x\vert{}$$

khi chọn $x$ là trọng số của một đỉnh bất kỳ nằm trên đường đi đơn từ $u$ đến $v$ (tức là $x \in \{w_1, w_2, \dots, w_m\}$).

**Yêu cầu:** Với mỗi truy vấn, hãy tính độ lệch trung vị của đường đi đơn từ $u$ đến $v$ và cập nhật $last\_ans$ bằng kết quả vừa tìm được.

## Input

* Dòng đầu tiên chứa hai số nguyên dương $n$ và $q$ ($1 \le n, q \le 2 \cdot 10^5$).
* Dòng thứ hai chứa $n$ số nguyên dương $a_1, a_2, \dots, a_n$ ($1 \le a_i \le 10^9$) — trọng số của các đỉnh.
* Trong $n - 1$ dòng tiếp theo, mỗi dòng chứa hai số nguyên dương $x_i$ và $y_i$ ($1 \le x_i, y_i \le n$, $x_i \ne y_i$) mô tả một cạnh của cây.
* Trong $q$ dòng cuối cùng, dòng thứ $j$ chứa hai số nguyên không âm $u'_j$ và $v'_j$ ($0 \le u'_j, v'_j \le 2 \cdot 10^9$) mô tả truy vấn thứ $j$ đã bị mã hóa.

## Output

* In ra $q$ dòng, dòng thứ $j$ chứa một số nguyên duy nhất là đáp án của truy vấn thứ $j$.

## Sample Input 1

```text
5 3
4 1 7 2 9
1 2
1 3
2 4
2 5
2 4
8 11
15 12

```

## Sample Output 1

```text
9
6
8

```

## Notes

Ở ví dụ 1:

* Truy vấn $1$: $last\_ans = 0$, $u'_1 = 2$, $v'_1 = 4$:
* Giải mã: $u = ((2 \oplus 0) \bmod 5) + 1 = 3$, $v = ((4 \oplus 0) \bmod 5) + 1 = 5$.
* Đường đi đơn từ $3$ đến $5$ gồm $4$ đỉnh: $3 \to 1 \to 2 \to 5$ với các trọng số tương ứng là $[7, 4, 1, 9]$.
* Sắp xếp tăng dần: $w = [1, 4, 7, 9]$. Chọn $x = 4$ (hoặc $x = 7$), tổng khoảng cách là $\vert{}1 - 4\vert{} + \vert{}4 - 4\vert{} + \vert{}7 - 4\vert{} + \vert{}9 - 4\vert{} = 3 + 0 + 3 + 5 = 9$. Cập nhật $last\_ans = 9$.


* Truy vấn $2$: $last\_ans = 9$, $u'_2 = 8$, $v'_2 = 11$:
* Giải mã: $u = ((8 \oplus 9) \bmod 5) + 1 = 2$, $v = ((11 \oplus 9) \bmod 5) + 1 = 3$.
* Đường đi đơn từ $2$ đến $3$ gồm $3$ đỉnh: $2 \to 1 \to 3$ với trọng số đã sắp xếp $w = [1, 4, 7]$.
* Chọn $x = 4$, tổng khoảng cách là $\vert{}1 - 4\vert{} + \vert{}4 - 4\vert{} + \vert{}7 - 4\vert{} = 3 + 0 + 3 = 6$. Cập nhật $last\_ans = 6$.


* Truy vấn $3$: $last\_ans = 6$, $u'_3 = 15$, $v'_3 = 12$:
* Giải mã: $u = ((15 \oplus 6) \bmod 5) + 1 = (9 \bmod 5) + 1 = 5$, $v = ((12 \oplus 6) \bmod 5) + 1 = (10 \bmod 5) + 1 = 1$.
* Đường đi đơn từ $5$ đến $1$ gồm $3$ đỉnh: $5 \to 2 \to 1$ với trọng số đã sắp xếp $w = [1, 4, 9]$.
* Chọn $x = 4$, tổng khoảng cách là $\vert{}1 - 4\vert{} + \vert{}4 - 4\vert{} + \vert{}9 - 4\vert{} = 3 + 0 + 5 = 8$. Cập nhật $last\_ans = 8$.