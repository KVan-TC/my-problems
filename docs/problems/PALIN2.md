---
code: PALIN2
title: Xâu đối xứng 2
time_limit: 1.0s
memory_limit: 1024MB
tags:
    - dp
    - strings
submit_url:
---

Cho một số nguyên dương $k$ và một xâu ký tự $s$ chỉ gồm các chữ cái tiếng Anh in thường. Ở mỗi thao tác, bạn được phép chọn một vị trí bất kỳ trong xâu $s$ và thay đổi ký tự tại vị trí đó thành một chữ cái tiếng Anh in thường khác.

Một xâu được gọi là đối xứng (palindrome) nếu khi đọc xâu từ trái sang phải cũng thu được kết quả giống như khi đọc từ phải sang trái.

**Yêu cầu:** Tìm số thao tác thay đổi ký tự ít nhất cần thực hiện để sau khi biến đổi, có thể phân chia xâu $s$ thành đúng $k$ xâu con liên tiếp không rỗng sao cho cả $k$ xâu con đó đều là xâu đối xứng.

## Input

* Dòng đầu tiên chứa số nguyên dương $k$ ($1 \le k \le \vert{}s\vert{}$).
* Dòng thứ hai chứa xâu ký tự $s$ chỉ gồm các chữ cái tiếng Anh in thường ($1 \le \vert{}s\vert{} \le 5000$).

## Output

* In ra một số nguyên duy nhất là số thao tác ít nhất cần thực hiện.

## Sample Input 1

```text
2
abc

```

## Sample Output 1

```text
1

```

## Sample Input 2

```text
3
aabbc

```

## Sample Output 2

```text
0

```

## Notes

Ở ví dụ 1:

* Xâu ban đầu là $s = \texttt{"abc"}$ và $k = 2$.
* Ta thực hiện $1$ thao tác đổi ký tự thứ hai thành $\texttt{'a'}$ để thu được xâu $\texttt{"aac"}$, sau đó chia thành $k = 2$ xâu con liên tiếp đối xứng là $\texttt{"aa"}$ và $\texttt{"c"}$ (hoặc đổi ký tự thứ hai thành $\texttt{'c'}$ để chia thành $\texttt{"a"}$ và $\texttt{"cc"}$).

Ở ví dụ 2:

* Xâu ban đầu là $s = \texttt{"aabbc"}$ và $k = 3$.
* Không cần thực hiện thao tác nào ($0$ thao tác), ta có thể chia ngay xâu ban đầu thành $k = 3$ xâu con liên tiếp đều đối xứng là $\texttt{"aa"}$, $\texttt{"bb"}$ và $\texttt{"c"}$.
