# TILING1 - LÁT GẠCH 1

* **Giới hạn thời gian:** $1.0$ giây
* **Giới hạn bộ nhớ:** $256$ MB
* **Tags:** `dp`

Cho $q$ truy vấn, mỗi truy vấn cung cấp một số nguyên dương $n$ tương ứng với một bảng lưới chữ nhật kích thước $2 \times n$ gồm $2$ hàng và $n$ cột. Ta có vô số các viên gạch hình chữ nhật thuộc hai loại kích thước: $1 \times 2$ (đặt ngang) và $2 \times 1$ (đặt dọc).

Cần lát kín toàn bộ bảng lưới $2 \times n$ bằng các viên gạch đã cho sao cho các viên gạch không chồng đè lên nhau, không có phần nào của viên gạch thừa ra ngoài phạm vi bảng lưới và không còn ô trống nào chưa được lát. Hai cách lát được coi là khác nhau nếu tồn tại ít nhất một viên gạch có vị trí hoặc hướng đặt khác nhau giữa hai cách lát.

**Yêu cầu:** Với mỗi truy vấn, hãy đếm số lượng cách lát gạch hợp lệ trên bảng lưới $2 \times n$. Vì kết quả có thể rất lớn, hãy in ra phần dư của kết quả khi chia cho $10^9 + 7$.

## Input

* Dòng đầu tiên chứa số nguyên dương $q$ ($1 \le q \le 10^6$) là số lượng truy vấn.
* $q$ dòng tiếp theo, mỗi dòng chứa một số nguyên dương $n$ ($1 \le n \le 10^6$).

## Output

* Gồm $q$ dòng, dòng thứ $i$ in ra một số nguyên duy nhất là số lượng cách lát gạch hợp lệ của truy vấn thứ $i$ sau khi chia dư cho $10^9 + 7$.

## Sample Input 1

```text
3
1
2
3

```

## Sample Output 1

```text
1
2
3

```

## Notes

Ở ví dụ 1:

* Với $n = 1$, bảng lưới kích thước $2 \times 1$ có duy nhất $1$ cách lát hợp lệ là đặt $1$ viên gạch $2 \times 1$ theo chiều dọc.
* Với $n = 2$, bảng lưới kích thước $2 \times 2$ có $2$ cách lát hợp lệ: đặt $2$ viên gạch $2 \times 1$ dọc song song nhau, hoặc đặt $2$ viên gạch $1 \times 2$ ngang chồng lên nhau.
* Với $n = 3$, bảng lưới kích thước $2 \times 3$ có $3$ cách lát hợp lệ: dùng $3$ viên gạch dọc; dùng $1$ viên dọc ở cột trái và $2$ viên ngang ở hai cột phải; hoặc dùng $2$ viên ngang ở hai cột trái và $1$ viên dọc ở cột phải.
