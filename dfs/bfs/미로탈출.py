n, m = map(int, input().split())
graph = []
visited = [[0]*m for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if (x <= -1 or y <= -1 or x >= n or y >= m):
        return False

    if (graph[x][y] == 0 and visited[x][y] == 0):
        visited[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    else:
        return False


count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count = count + 1

print(count)
