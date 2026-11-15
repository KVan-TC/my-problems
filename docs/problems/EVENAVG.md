---
code: EVENAVG
title: Trung bình cộng chẵn
tags: Toán học, Số học
limits: 1.0s / 256MB
---

Một cửa hàng tạp hóa ghi sổ thu chi từng ngày và khai với bên thuế rằng mức lãi trung bình mỗi ngày của cửa hàng là $K$. Bên thuế cử hai cán bộ đến kiểm kê. Mỗi đợt kiểm kê, hai người lấy một số chẵn ngày liên tiếp trong sổ, mỗi người xem một nửa số ngày đó, và đợt nào có trung bình cộng đúng bằng mức khai thì coi là khớp sổ.

Sổ ghi $n$ ngày, ngày thứ $i$ có số tiền $a_i$: $a_i > 0$ là lãi, $a_i < 0$ là lỗ, $a_i = 0$ là hòa vốn. Một đợt kiểm kê là một đoạn các ngày liên tiếp từ ngày $l$ đến ngày $r$ với $1 \le l < r \le n$, sao cho số ngày $r - l + 1$ là số chẵn. Đợt kiểm kê khớp sổ nếu trung bình cộng của $a_l, a_{l+1}, \dots, a_r$ đúng bằng $K$, tức là


$$a_l + a_{l+1} + \dots + a_r = K \cdot (r - l + 1).$$

Hai đợt kiểm kê là khác nhau nếu khác $l$ hoặc khác $r$.

**Yêu cầu:** Hãy đếm số đợt kiểm kê khớp sổ và cho biết đợt khớp sổ dài nhất gồm bao nhiêu ngày.

## Input

* Dòng đầu chứa hai số nguyên $n$ và $K$ ($1 \le n \le 2 \cdot 10^5$, $|K| \le 10^9$).
* Dòng thứ hai chứa $n$ số nguyên $a_1, a_2, \dots, a_n$ ($|a_i| \le 10^9$).

Mỗi file dữ liệu vào gồm đúng một bộ test.

## Output

* Một dòng gồm hai số nguyên cách nhau một dấu cách: số đợt kiểm kê khớp sổ, rồi số ngày của đợt khớp sổ dài nhất. Nếu không có đợt nào khớp sổ thì in `0 0`.

## Scoring

| Subtask | Điểm | Ràng buộc |
| --- | --- | --- |
| 1 | 20% | $n \le 300$ |
| 2 | 25% | $n \le 5000$ |
| 3 | 20% | $K = 0$ |
| 4 | 35% | Không có ràng buộc gì thêm |

## Sample Input 1

```text
5 1
1 2 0 3 -1

```

## Sample Output 1

```text
3 4

```

## Sample Input 2

```text
3 4
4 5 3

```

## Sample Output 2

```text
1 2

```
