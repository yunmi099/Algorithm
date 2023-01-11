N, M = map(int, input().split())
rice_cake = list(map(int, input().split()))
rice_cake.sort()


def binary_search(array, target, start, end):
    anwser = 0
    if start > end:
        return start-1  # 가장 마지막 mid 값을 return
    mid = (start+end)//2
    for i in range(N):
        if array[i] > mid:
            anwser = anwser + array[i]-mid
    if anwser == target:
        return mid
    elif anwser < target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


print(binary_search(rice_cake, M, 0, rice_cake[N-1]))
