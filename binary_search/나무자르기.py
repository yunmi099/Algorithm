# 키워드(예약어): 변수이름, 함수이름
# if else while for array

N, M = map(int, input().split())
arr = list(map(int, input().split()))


def binary_search(arr, target, start, end):
    mid = (start+end) // 2
    total = 0
    for i in array:
        if i > mid:
            total = total + (i - mid)
    anwser = total - target
    if anwser == 0:
        return mid
    elif anwser < 0:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)


print(binary_search(arr, M, min(arr), max(arr)))
