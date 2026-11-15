# VSTEPS - Bậc thang

* **Giới hạn thời gian:** $1.0$ giây
* **Giới hạn bộ nhớ:** $256$ MB
* **Tags:** `dp`

Bờm chơi trò chơi điện tử Lucky Luke đến màn phải điều khiển Lucky leo lên một cầu thang gồm $n$ bậc.

Các bậc thang được đánh số từ $1$ đến $n$ từ dưới lên trên. Lucky có thể đi lên một bậc thang, hoặc nhảy một bước lên hai bậc thang. Tuy nhiên một số bậc thang đã bị thủng do cũ kỹ và Lucky không thể bước chân lên được. Biết ban đầu, Lucky đứng ở bậc thang số $1$ (bậc thang số $1$ không bao giờ bị thủng).

**Yêu cầu:** Chơi đến đây, Bờm chợt nảy ra câu hỏi: có bao nhiêu cách để Lucky leo hết được cầu thang? (nghĩa là leo đến bậc thang thứ $n$). Bờm muốn nhờ bạn trả lời câu hỏi này.

## Input

* Dòng đầu tiên gồm $2$ số nguyên $n$ và $k$, là số bậc của cầu thang và số bậc thang bị hỏng ($0 \le k < n \le 10^5$).
* Dòng thứ hai gồm $k$ số nguyên cho biết chỉ số của các bậc thang bị hỏng theo thứ tự tăng dần.

## Output

* In ra phần dư của số cách Lucky leo hết cầu thang khi chia cho $14062008$.

## Sample Input 1

```text
4 2
2 3

```

## Sample Output 1

```text
0

```

## Sample Input 2

```text
90000 1
49000

```

## Sample Output 2

```text
4108266

```
