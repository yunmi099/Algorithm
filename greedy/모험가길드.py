n = int(input())
person = list(map(int, input().split()))
count = 0
person.sort()
while (n > 0):
    n = n-person[n-1]
    count += 1
print(count)
