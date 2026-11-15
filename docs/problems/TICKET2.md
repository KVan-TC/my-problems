---
code: TICKET2
title: Mua vé 2
time_limit: 1.0s
memory_limit: 256MB
tags:
    - dp
submit_url:
---

Bạn đã lên kế hoạch đi tàu trước cho $n$ ngày. Danh sách đó được thể hiện dưới mảng $d$, trong đó nếu $d_i = 1$ thì bạn cần đi tàu vào ngày thứ $i$, còn $d_i = 0$ nếu không cần. Vé tàu được bán theo ba cách khác nhau:

* Vé $1$ ngày được bán với giá $a$.
* Thẻ $7$ ngày được bán với giá $b$.
* Thẻ $30$ ngày được bán với giá $c$.

Thẻ cho phép đi lại nhiều ngày liên tục.

Ví dụ: nếu chúng ta nhận được thẻ $7$ ngày vào ngày thứ $2$ thì chúng ta có thể đi tàu trong $7$ ngày: $2, 3, 4, 5, 6, 7$ và $8$.

**Yêu cầu:** Hãy tính số tiền tối thiểu bạn cần để thực hiện đúng kế hoạch đi tàu mà bạn đã đề ra trong $n$ ngày.

## Input

* Dòng đầu tiên gồm bốn số nguyên $n, a, b, c$ ($1 \le n \le 10^6$, $1 \le a < b < c \le 10^6$).
* Dòng tiếp theo gồm $n$ số nguyên, số thứ $i$ là giá trị $d_i$ thể hiện có cần đi tàu vào ngày thứ $i$ không ($0 \le d_i \le 1$).

## Output

* Gồm một dòng duy nhất là đáp án cần tìm.

## Sample Input 1

```text
8 2 7 15
1 0 0 1 0 1 1 1

```

## Sample Output 1

```text
9

```

## Sample Input 2

```text
8 2 7 8
1 0 0 1 0 1 1 1

```

## Sample Output 2

```text
8

```

## Notes

Ở ví dụ 1:

* Ta có thể mua vé $1$ ngày vào ngày thứ nhất, mua thẻ $7$ ngày vào ngày thứ tư.

Ở ví dụ 2:

* Ta có thể mua thẻ $30$ ngày vào ngày thứ nhất.
