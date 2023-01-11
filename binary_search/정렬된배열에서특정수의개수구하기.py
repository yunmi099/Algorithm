from bisect import bisect_left, bisect_right
N, M = map(int, input().split())
array = list(map(int, input().split()))
answer = bisect_right(array, M)-bisect_left(array, M)
if answer == 0:
    answer = -1
print(answer)
