string = list(input())
data = []
num = 0
for i in string:
    if i.isalpha():
        data.append(i)
    else:
        num = num + int(i)

data.sort()

data.append(str(num))
print(''.join(data))
