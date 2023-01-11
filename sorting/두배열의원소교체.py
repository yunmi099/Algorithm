N, K = map(int, input().split())
list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))
list_A.sort()
list_B.sort()
for i in range(K):

    if list_A[0] >= list_B[N-1]:
        break
    list_A[0], list_B[N-1] = list_B[N-1], list_A[0]
    list_A.sort()
    list_B.sort()

print(sum(list_A))