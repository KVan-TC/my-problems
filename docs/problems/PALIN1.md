---
code: PALIN1
title: Xâu đối xứng 1
time_limit: 1.0s
memory_limit: 1024MB
tags:
    - dp
    - strings
submit_url:
---

Cho một xâu ký tự $s$ chỉ gồm các chữ cái tiếng Anh in thường. Ở mỗi thao tác, bạn được phép chèn một ký tự tiếng Anh in thường bất kỳ vào một vị trí tùy ý trong xâu $s$ (ở đầu, ở cuối hoặc xen giữa hai ký tự liên tiếp).

Một xâu được gọi là đối xứng (palindrome) nếu khi đọc xâu từ trái sang phải cũng thu được kết quả giống như khi đọc từ phải sang trái.

**Yêu cầu:** Tìm số thao tác chèn ký tự ít nhất để biến đổi xâu $s$ ban đầu thành một xâu đối xứng.

## Input

* Dòng duy nhất chứa xâu ký tự $s$ chỉ gồm các chữ cái tiếng Anh in thường ($1 \le \vert{}s\vert{} \le 5000$).

## Output

* In ra một số nguyên duy nhất là số thao tác ít nhất cần thực hiện.

## Sample Input 1

```text
abc

```

## Sample Output 1

```text
2

```

## Sample Input 2

```text
aabbc

```

## Sample Output 2

```text
3

```

## Notes

Ở ví dụ 1:

* Xâu ban đầu là $s = \texttt{"abc"}$.
* Ta có thể chèn thêm $2$ ký tự $\texttt{'b'}$ và $\texttt{'a'}$ vào cuối xâu để thu được xâu đối xứng $\texttt{"abcba"}$ (hoặc chèn $\texttt{'c'}$ và $\texttt{'b'}$ vào đầu xâu để thu được $\texttt{"cbabc"}$).

Ở ví dụ 2:

* Xâu ban đầu là $s = \texttt{"aabbc"}$.
* Cần tối thiểu $3$ thao tác chèn ký tự để biến đổi $s$ thành một xâu đối xứng độ dài $8$, chẳng hạn như $\texttt{"cbabbabc"}$.
