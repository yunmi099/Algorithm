str = input()
num = list(str)
new_list = list(map(int, num))
result = new_list[0]
for i in range(len(new_list)-1):
    if (new_list[i] == 0 | | new_list[i] == 1):
        result = result + new_list[i+1]
    else:
        result = result * new_list[i+1]
print(result)
