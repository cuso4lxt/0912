def is_valid_state(state):
    if(state[1] == state[2] and state[0] != state[1]) or (state[2] == state[3] and state[0] != state[2]):
        return False  # 狼羊/羊菜 单独在一起
    return True

def dfs(state, path, visited):
    if state == (0, 0, 0, 0):
        # 找到了解决方案
        print("找到解决方案：", path)
        return

    for move in moves:
        new_state = tuple(state[i] + move[i] for i in range(4))
        if all(0 <= new_state[i] <= 1 for i in range(4)) and is_valid_state(new_state) and new_state not in visited:
            visited.add(new_state)
            dfs(new_state, path + [new_state], visited)
            visited.remove(new_state)



# 初始状态：（1，1，1，1）表示人、狼、羊、菜都在起始岸
initial_state = (1,1,1,1)
# 所有的移动方式
moves = [
    (-1,0,0,0),
    (-1,-1,0,0),
    (-1,0,-1,0),
    (-1,0,0,-1),
    (1,0,0,0),
    (1,1,0,0),
    (1,0,1,0),
    (1,0,0,1)
]

visited = set()  # 创建一个空集合，用于储存已经访问过的状态
visited.add(initial_state)  # 将初始状态加入访问过的集合中

dfs(initial_state, [initial_state], visited)