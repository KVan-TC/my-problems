---
code: TILING2
title: Lát gạch 2
time_limit: 1.0s
memory_limit: 256MB
tags:
    - dp
submit_url:
---

Cho một bảng lưới chữ nhật kích thước $2 \times n$ gồm $2$ hàng và $n$ cột. Ta có vô số các viên gạch thuộc ba loại kích thước: $1 \times 1$, $2 \times 1$ và $1 \times 2$.

Cần lát kín toàn bộ bảng lưới bằng các viên gạch đã cho sao cho các viên gạch không chồng đè lên nhau, không có phần nào của viên gạch thừa ra ngoài phạm vi bảng lưới và không còn ô trống nào chưa được lát. Hai cách lát được coi là khác nhau nếu tồn tại ít nhất một viên gạch có vị trí hoặc kích thước khác nhau giữa hai cách lát.

**Yêu cầu:** Hãy đếm số lượng cách lát gạch hợp lệ trên bảng lưới $2 \times n$. Vì kết quả có thể rất lớn, hãy in ra phần dư của kết quả khi chia cho $10^9 + 7$.

## Input

* Dòng duy nhất chứa một số nguyên dương $n$ ($1 \le n \le 10^6$).

## Output

* In ra một số nguyên duy nhất là số lượng cách lát gạch hợp lệ tìm được sau khi chia dư cho $10^9 + 7$.

## Sample Input 1

```text
1

```

## Sample Output 1

```text
2

```

## Sample Input 2

```text
2

```

## Sample Output 2

```text
7

```

## Sample Input 3

```text
3

```

## Sample Output 3

```text
22

```

## Sample Input 4

```text
4

```

## Sample Output 4

```text
71

```

## Notes

Ở ví dụ 1:

* Với $n = 1$, bảng lưới có kích thước $2 \times 1$ và có tất cả $2$ cách lát hợp lệ:
1. Dùng $2$ viên gạch kích thước $1 \times 1$.
2. Dùng $1$ viên gạch kích thước $2 \times 1$ đặt dọc.

Ở ví dụ 2:

* Với $n = 2$, bảng lưới có kích thước $2 \times 2$ và có tất cả $7$ cách lát hợp lệ như minh họa trong hình:
1. Dùng $4$ viên gạch kích thước $1 \times 1$ ($1$ cách).
2. Dùng $1$ viên gạch $2 \times 1$ đặt dọc và $2$ viên gạch $1 \times 1$ ($2$ cách: viên $2 \times 1$ ở cột trái hoặc cột phải).
3. Dùng $1$ viên gạch $1 \times 2$ đặt ngang và $2$ viên gạch $1 \times 1$ ($2$ cách: viên $1 \times 2$ ở hàng trên hoặc hàng dưới).
4. Dùng $2$ viên gạch $2 \times 1$ đặt dọc song song ($1$ cách).
5. Dùng $2$ viên gạch $1 \times 2$ đặt ngang chồng lên nhau ($1$ cách).
