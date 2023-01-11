
N, M, K = map(int, input().split())
value = input().split()
max = 0
sum = 0
for i in range(N):
    if int(value[i]) > max:
        max_2 = max
        max = int(value[i])
while (M > 0):
    if (M > K):
        for i in range(K):
            sum = sum + max
        sum = sum + max_2
        M = M-K-1
    else:
        for i in range(M):
            sum = sum + max

print(sum)
