# Author: zzk


maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
dirs = [
    lambda x, y: (x + 1, y),
    lambda x, y: (x - 1, y),
    lambda x, y: (x, y - 1),
    lambda x, y: (x, y + 1),
]


def mpath(x1, y1, x2, y2):
    stack = []
    stack.append((x1, y1))
    while len(stack) > 0:
        curNode = stack[-1]
        if curNode[0] == x2 and curNode[1] == y2:
            # 到达终点
            for p in stack:
                print(p)
            break
        for dir in dirs:
            nextNode = dir(*curNode)
            if maze[nextNode[0]][nextNode[1]] == 0:
                # 找到下一个
                stack.append(nextNode)
                # 标记已走过
                maze[nextNode[0]][nextNode[1]] = -1
                break
        else:  # 标记为死路
            maze[curNode[0]][curNode[1]] = -1
            stack.pop()
    return False

mpath(1, 1, 8, 8)

