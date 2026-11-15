# MAXSUM - Tổng đoạn con lớn nhất

* **Giới hạn thời gian:** $1.0$ giây
* **Giới hạn bộ nhớ:** $512$ MB
* **Tags:** `dp`, `prefix-sums`

Cho một dãy số nguyên $x_1, x_2, \dots, x_n$ gồm $n$ phần tử. Một đoạn con liên tiếp khác rỗng của dãy là một dãy gồm các phần tử liên tiếp $x_l, x_{l+1}, \dots, x_r$ với $1 \le l \le r \le n$.

**Yêu cầu:** Hãy tìm tổng lớn nhất của các giá trị trong một đoạn con liên tiếp khác rỗng của dãy đã cho.

## Input

* Dòng đầu tiên chứa một số nguyên dương $n$ ($1 \le n \le 2 \cdot 10^5$) — số lượng phần tử của dãy.
* Dòng thứ hai chứa $n$ số nguyên $x_1, x_2, \dots, x_n$ ($-10^9 \le x_i \le 10^9$), các số cách nhau bởi một khoảng trắng.

## Output

* In ra một số nguyên duy nhất là tổng lớn nhất của một đoạn con liên tiếp khác rỗng tìm được.

## Sample Input 1

```text
8
-1 3 -2 5 3 -5 2 2

```

## Sample Output 1

```text
9

```

## Notes

Ở ví dụ 1:

* Đoạn con liên tiếp có tổng lớn nhất là $(3, -2, 5, 3)$ (từ vị trí $2$ đến vị trí $5$) với tổng giá trị là $3 + (-2) + 5 + 3 = 9$.
