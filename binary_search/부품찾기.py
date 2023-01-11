N = int(input())
store = list(map(int, input().split()))
M = int(input())
buy = list(map(int, input().split()))
anwser = ['no' for i in range(M)]

for i in range(M):
    for _ in store:
        if (buy[i] == _):
            anwser[i] = 'yes'
            print(anwser[i])
            continue

print(anwser)
