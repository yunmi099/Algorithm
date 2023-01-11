location = list(str(input()))
print(location)
x = ord(location[0])-ord('a')+1
y = int(location[1])

count = 0

if (0 < x+2 < 9):
    if (0 < y+1 < 9):
        count += 1

    if (0 < y-1 < 9):
        count += 1

if (0 < x-2 < 9):
    if (0 < y+1 < 9):
        count += 1
    if (0 < y-1 < 9):
        count += 1

if (0 < y+2 < 9):
    if (0 < x+1 < 9):
        count += 1
    if (0 < x-1 < 9):
        count += 1

if (0 < y-2 < 9):
    if (0 < x+1 < 9):
        count += 1
    if (0 < x-1 < 9):
        count += 1

print(count)

# 모법답안
# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0]))- int(ord('a'))+1

# steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

# result = 0

# for step in steps :

# 	next_row = row + step[0]
# 	next_column = column + step[1]

# 	if next_row >= 1 and next_row <=8 and next_colum >=1 and next_column <= 8:
# 	result += 1

# print(result)
