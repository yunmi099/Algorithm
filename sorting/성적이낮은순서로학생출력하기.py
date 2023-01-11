N = int(input())

array = []
for i in range(N):
    array.append(int(input()))

array.sort()
array.reverse()

for i in array:
    print(i, end='')
