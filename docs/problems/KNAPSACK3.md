# KNAPSACK3 - Cái túi 3

* **Giới hạn thời gian:** $1.0$ giây
* **Giới hạn bộ nhớ:** $1024$ MB
* **Tags:** `dp`

Cho $N$ loại đồ vật và một chiếc túi có sức chứa tối đa là $W$. Mỗi đồ vật thuộc loại thứ $i$ ($1 \le i \le N$) có trọng lượng $w_i$, giá trị $v_i$, và có sẵn đúng $c_i$ chiếc.

**Yêu cầu:** Hãy chọn một số đồ vật (trong số các đồ vật hiện có) để xếp vào túi sao cho tổng trọng lượng không vượt quá $W$ và tổng giá trị thu được là lớn nhất.

## Input

* Dòng đầu tiên chứa hai số nguyên dương $N$ và $W$ ($1 \le N \le 1000$; $1 \le W \le 10^5$).
* $N$ dòng tiếp theo, dòng thứ $i$ chứa ba số nguyên dương $w_i$, $v_i$ và $c_i$ ($1 \le w_i \le W$; $1 \le v_i \le 10^9$; $1 \le c_i \le 1000$), các số cách nhau bởi một khoảng trắng.

## Output

* In ra một số nguyên duy nhất là tổng giá trị lớn nhất tìm được.

## Sample Input 1

```text
3 8
3 30 1
4 50 1
5 60 1

```

## Sample Output 1

```text
90

```

## Sample Input 2

```text
3 8
3 30 2
4 50 2
5 60 2

```

## Sample Output 2

```text
100

```

## Notes

Ở ví dụ 1:

* Có $N = 3$ loại đồ vật và chiếc túi có sức chứa $W = 8$, mỗi loại chỉ có $1$ chiếc.
* Chọn $1$ đồ vật loại $1$ (trọng lượng $3$, giá trị $30$) và $1$ đồ vật loại $3$ (trọng lượng $5$, giá trị $60$).
* Tổng trọng lượng là $3 + 5 = 8 \le 8$ và tổng giá trị là $30 + 60 = 90$.

Ở ví dụ 2:

* Có $N = 3$ loại đồ vật và chiếc túi có sức chứa $W = 8$, mỗi loại có $2$ chiếc.
* Chọn $2$ đồ vật loại $2$ (mỗi chiếc có trọng lượng $4$, giá trị $50$).
* Tổng trọng lượng là $2 \times 4 = 8 \le 8$ và tổng giá trị là $2 \times 50 = 100$.
