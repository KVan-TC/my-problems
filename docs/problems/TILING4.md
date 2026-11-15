# TILING4 - LÁT GẠCH 4

* **Giới hạn thời gian:** $1.0$ giây
* **Giới hạn bộ nhớ:** $256$ MB
* **Tags:** `dp`

Cho một bảng lưới chữ nhật kích thước $2 \times n$ gồm $2$ hàng và $n$ cột. Ta có thể đặt một số lượng tùy ý (có thể bằng $0$) các viên gạch hình chữ L (mỗi viên gạch chiếm đúng $3$ ô trong một vùng vuông $2 \times 2$ liền kề) lên bảng lưới sao cho không có hai viên gạch nào đè lên nhau. Lưu ý rằng một cách đặt hợp lệ không nhất thiết phải phủ kín toàn bộ bảng lưới.

Với mỗi cách đặt gạch hợp lệ, **độ bao phủ** của cách đặt đó được định nghĩa là tổng số lượng ô trên bảng lưới bị đè bởi một viên gạch chữ L bất kỳ (tức bằng $3$ lần số viên gạch chữ L được sử dụng).

**Yêu cầu:** Hãy tính tổng độ bao phủ của tất cả các cách đặt gạch hợp lệ trên bảng lưới $2 \times n$. Vì kết quả có thể rất lớn, hãy in ra phần dư của kết quả khi chia cho $998244353$.

## Input

* Dòng duy nhất chứa một số nguyên dương $n$ ($1 \le n \le 10^6$).

## Output

* In ra một số nguyên duy nhất là tổng độ bao phủ tìm được sau khi chia dư cho $998244353$.

## Sample Input 1

```text
2

```

## Sample Output 1

```text
12

```

## Sample Input 2

```text
3

```

## Sample Output 2

```text
36

```

## Sample Input 3

```text
4

```

## Sample Output 3

```text
156

```

## Notes

Ở ví dụ 1:

* Với $n = 2$, bảng lưới có kích thước $2 \times 2$ và có tất cả $5$ cách đặt gạch hợp lệ:
* $1$ cách không đặt viên gạch nào, có độ bao phủ bằng $0$.
* $4$ cách đặt đúng $1$ viên gạch chữ L (tương ứng với $4$ hướng xoay của chữ L trong vùng $2 \times 2$), mỗi cách có độ bao phủ bằng $3$.

* Tổng độ bao phủ của tất cả các cách đặt là: $0 + 4 \times 3 = 12$.

Ở ví dụ 2:

* Với $n = 3$, bảng lưới có kích thước $2 \times 3$ và có tất cả $11$ cách đặt gạch hợp lệ:
* $1$ cách không đặt viên gạch nào, có độ bao phủ bằng $0$.
* $8$ cách đặt đúng $1$ viên gạch chữ L ($4$ cách đặt trong vùng cột $1 \dots 2$ và $4$ cách đặt trong vùng cột $2 \dots 3$), mỗi cách có độ bao phủ bằng $3$.
* $2$ cách đặt đồng thời $2$ viên gạch chữ L không giao nhau (một viên ở cột $1 \dots 2$ và một viên ở cột $2 \dots 3$), mỗi cách có độ bao phủ bằng $6$.

* Tổng độ bao phủ của tất cả các cách đặt là: $0 + 8 \times 3 + 2 \times 6 = 36$.
