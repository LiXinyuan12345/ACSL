'''
有向图：
1. 求length=3的path数?
    构造邻接矩阵,将矩阵自乘3次,将矩阵的所有数相加即为path数

2.求从A点出发length=3的path数? 
    构造邻接矩阵,将矩阵自乘3次,将行A所有数相加即为path数

3 求从A点到C length=3的path数?
    构造邻接矩阵,将矩阵自乘3次,A行C列数即为path数

4.从哪一个顶点出发,有最多的length=3的path数?
    构造邻接矩阵,将矩阵自乘3次,按行求和,和最大的那行就是顶点

5.哪些顶点对,没有length=3的path?
    构造邻接矩阵,将矩阵自乘3次,矩阵中值为0的行列就是顶点对

6.从a出发有多少环?
   构造邻接矩阵,将矩阵自乘【2,顶点数-1】次,将每次自乘的【a,a】数相加

7.有多少唯一的顶点对在两个方向上都没有length=2的path?可以包括(X,X)。
   构造邻接矩阵,将矩阵自乘2次,【a,b】和【b , a】=0 或者【a,a】=0都是结果对,需去重
'''

# 去重找有向图中环个数
def find_unique_cycles(adj_matrix):
    n = len(adj_matrix)
    visited = [False] * n
    path = []
    cycles = []
    
    def dfs(v, start):
        visited[v] = True
        path.append(v)
        for u in range(n):
            if adj_matrix[v][u]:  # 如果存在从v到u的边
                if u == start and len(path) > 1:  # 发现环
                #if u == start and len(path) > 0:  # 发现环                    
                    str = ""
                    for v in path:
                        str += chr( v+ 65) 
                    cycles.append(str)    
                elif not visited[u]:
                    dfs(u, start)
        path.pop()
        visited[v] = False
    
    for i in range(n):
        dfs(i, i)
    
    # 去除重复的环
    unique_cycles = []
    result_cycles =[]
    for cycle in cycles:
        cycle_set = set(cycle)
        if cycle_set not in unique_cycles:
            unique_cycles.append(cycle_set)
            result_cycles.append(cycle)
    
    return [''.join(cycle) for cycle in result_cycles]


def find_cycles(adj_matrix):
    n = len(adj_matrix)
    visited = [False] * n
    path = []
    cycles = []
    
    def dfs(v, start):
        visited[v] = True
        path.append(v)
        for u in range(n):
            if adj_matrix[v][u]:  # 如果存在从v到u的边
                if u == start and len(path) > 2:  # 发现环
                    #cycles.append(path[:])
                    str = ""
                    for v in path:
                        str += chr( v+ 65) 
                    cycles.append(str)    
                elif not visited[u]:
                    dfs(u, start)
        path.pop()
        visited[v] = False
    
    for i in range(n):
        dfs(i, i)
    
    return cycles

# Example usage:
'''
adj_matrix = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
adj_matrix = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],   
    [0, 0, 0, 0, 0]
]
adj_matrix = [
    [0, 0, 0,  0],
    [0, 0, 0,  0],
    [0, 0, 0,  0],
    [0, 0, 0,  0]
]
adj_matrix = [
    [0, 0,  0],
    [0, 0,  0],
    [0, 0,  0]
]
'''

adj_matrix = [
    [0, 1, 1, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0],   
    [1, 0, 1, 1, 0]
]

cycles = find_unique_cycles(adj_matrix)
if cycles:
    print("Number of cycles:", len(cycles))
    for cycle in cycles:
        print("Cycle path:", cycle)
else:
    print("No cycles found.")