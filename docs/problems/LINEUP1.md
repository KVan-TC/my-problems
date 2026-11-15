# LINEUP1 - Giao lưu 1

* **Giới hạn thời gian:** $1.0$ giây
* **Giới hạn bộ nhớ:** $256$ MB
* **Tags:** `dp`

Có $n$ học sinh (gồm cả nam và nữ) được xếp thành một hàng dọc và đánh số từ $1$ đến $n$. Một cách xếp hàng được gọi là *hợp lệ* nếu không có $3$ bạn nam nào đứng liền kề nhau. Hai cách xếp hàng được coi là khác nhau nếu tồn tại ít nhất một vị trí có giới tính của học sinh đứng ở vị trí đó khác nhau.

**Yêu cầu:** Hãy đếm số cách xếp hàng hợp lệ. Vì kết quả có thể rất lớn, hãy in ra phần dư của kết quả khi chia cho $10^9 + 7$.

## Input

* Dòng duy nhất chứa một số nguyên dương $n$ ($1 \le n \le 10^6$).

## Output

* In ra một số nguyên duy nhất là số cách xếp hàng hợp lệ sau khi chia dư cho $10^9 + 7$.

## Sample Input 1

```text
3

```

## Sample Output 1

```text
7

```

## Notes

Ở ví dụ 1:

* Với $n = 3$, ký hiệu $0$ là bạn nữ và $1$ là bạn nam, có $7$ cách xếp hàng hợp lệ gồm: $(0, 0, 0)$, $(0, 0, 1)$, $(0, 1, 0)$, $(0, 1, 1)$, $(1, 0, 0)$, $(1, 0, 1)$, $(1, 1, 0)$.
