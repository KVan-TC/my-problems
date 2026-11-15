# TILING3 - LÁT GẠCH 3

* **Giới hạn thời gian:** $1.0$ giây
* **Giới hạn bộ nhớ:** $256$ MB
* **Tags:** `dp`

Cho một bảng lưới chữ nhật kích thước $2 \times n$ gồm $2$ hàng và $n$ cột. Ta có thể đặt một số lượng tùy ý (có thể bằng $0$) các viên gạch hình chữ L (mỗi viên gạch chiếm đúng $3$ ô trong một vùng vuông $2 \times 2$ liền kề, theo một trong $4$ hướng xoay) lên bảng lưới sao cho không có hai viên gạch nào đè lên nhau và không có phần nào của viên gạch vượt ra ngoài phạm vi bảng lưới.

Lưu ý rằng một cách đặt hợp lệ không nhất thiết phải phủ kín toàn bộ bảng lưới (các ô trống không bị gạch đè lên vẫn được chấp nhận). Hai cách đặt được coi là khác nhau nếu tồn tại ít nhất một ô vuông đơn vị bị phủ bởi một viên gạch ở cách đặt này nhưng không bị phủ ở cách đặt kia, hoặc thuộc hai viên gạch khác nhau giữa hai cách đặt.

**Yêu cầu:** Hãy đếm tổng số cách đặt gạch hợp lệ trên bảng lưới $2 \times n$. Vì kết quả có thể rất lớn, hãy in ra phần dư của kết quả khi chia cho $998244353$.

## Input

* Dòng duy nhất chứa một số nguyên dương $n$ ($1 \le n \le 10^6$).

## Output

* In ra một số nguyên duy nhất là số lượng cách đặt gạch hợp lệ tìm được sau khi chia dư cho $998244353$.

## Sample Input 1

```text
1

```

## Sample Output 1

```text
1

```

## Sample Input 2

```text
2

```

## Sample Output 2

```text
5

```

## Sample Input 3

```text
3

```

## Sample Output 3

```text
11

```

## Sample Input 4

```text
4

```

## Sample Output 4

```text
33

```

## Notes

Ở ví dụ 1:

* Với $n = 1$, bảng lưới kích thước $2 \times 1$ không đủ chiều rộng để đặt bất kỳ viên gạch chữ L nào, do đó chỉ có duy nhất $1$ cách đặt hợp lệ là không đặt viên gạch nào.

Ở ví dụ 2:

* Với $n = 2$, bảng lưới có kích thước $2 \times 2$ và có tất cả $5$ cách đặt gạch hợp lệ:
* $1$ cách không đặt viên gạch nào (để trống toàn bộ $4$ ô).
* $4$ cách đặt đúng $1$ viên gạch hình chữ L (tương ứng với $4$ hướng xoay khác nhau của viên gạch chữ L trong vùng vuông $2 \times 2$).

Ở ví dụ 3:

* Với $n = 3$, bảng lưới có kích thước $2 \times 3$ và có tất cả $11$ cách đặt gạch hợp lệ:
* $1$ cách không đặt viên gạch nào.
* $8$ cách đặt đúng $1$ viên gạch hình chữ L ($4$ cách đặt trong vùng cột $1 \dots 2$ và $4$ cách đặt trong vùng cột $2 \dots 3$).
* $2$ cách đặt đồng thời $2$ viên gạch hình chữ L không giao nhau (một viên ở cột $1 \dots 2$ và một viên ở cột $2 \dots 3$ khớp vào nhau).
