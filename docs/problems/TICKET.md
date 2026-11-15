# TICKET - MUA VÉ

* **Giới hạn thời gian:** $1.0$ giây
* **Giới hạn bộ nhớ:** $256$ MB
* **Tags:** `dp`

Có $n$ người xếp thành một hàng dọc để mua vé, được đánh số từ $1$ đến $n$ theo thứ tự từ đầu hàng đến cuối hàng. Mỗi người cần mua đúng $1$ vé, và quầy bán vé cho phép mỗi người mua tối đa $2$ vé.

Do đó, một số người có thể rời khỏi hàng và nhờ người đứng ngay trước mình mua hộ vé:

* Nếu người thứ $i$ ($1 \le i \le n$) tự mua vé cho riêng mình, thời gian phục vụ tốn $t_i$.
* Nếu người thứ $i + 1$ ($1 \le i < n$) rời khỏi hàng và nhờ người thứ $i$ mua hộ vé, tổng thời gian để người thứ $i$ mua vé cho cả hai người là $r_i$ (lưu ý người thứ $i$ không thể nhờ thêm người khác mua hộ nữa).

**Yêu cầu:** Hãy tìm tổng thời gian phục vụ bán vé nhỏ nhất để tất cả $n$ người đều mua được vé.

## Input

* Dòng đầu tiên chứa số nguyên dương $n$ ($1 \le n \le 10^6$).
* Dòng thứ hai chứa $n$ số nguyên dương $t_1, t_2, \dots, t_n$ ($1 \le t_i \le 10^9$).
* Dòng thứ ba chứa $n - 1$ số nguyên dương $r_1, r_2, \dots, r_{n-1}$ ($1 \le r_i \le 10^9$).

## Output

* In ra một số nguyên duy nhất là tổng thời gian phục vụ nhỏ nhất tìm được.

## Sample Input 1

```text
5
2 5 7 8 4
4 9 10 10

```

## Sample Output 1

```text
18

```

## Sample Input 2

```text
4
5 7 8 4
50 50 50

```

## Sample Output 2

```text
24

```

## Notes

Ở ví dụ 1:

* Có $n = 5$ người xếp hàng với thời gian tự mua $t = [2, 5, 7, 8, 4]$ và thời gian mua ghép hai người $r = [4, 9, 10, 10]$.
* Phương án tối ưu: người thứ $2$ rời hàng nhờ người thứ $1$ mua hộ (tốn $r_1 = 4$), người thứ $4$ rời hàng nhờ người thứ $3$ mua hộ (tốn $r_3 = 10$), và người thứ $5$ tự mua vé (tốn $t_5 = 4$).
* Tổng thời gian phục vụ đạt giá trị nhỏ nhất là: $4 + 10 + 4 = 18$.

Ở ví dụ 2:

* Có $n = 4$ người với thời gian tự mua $t = [5, 7, 8, 4]$ và thời gian mua ghép hai người $r = [50, 50, 50]$.
* Phương án tối ưu là không ai rời hàng, cả $4$ người đều tự mua vé cho riêng mình với tổng thời gian là $5 + 7 + 8 + 4 = 24$.
