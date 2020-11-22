import math
import random
import statistics
import sys

N = int(sys.stdin.readline())  # read number of nodes from the input
maxWeight = int(sys.stdin.readline())  # read the largest weight of the graph
maxNodes = int(sys.stdin.readline()) - 1  # we read the desired approximation
g_asked = {}


def get_neighbors(node=1):
    if node in g_asked:
        return g_asked[node]
    print(node)
    sys.stdout.flush()
    line = sys.stdin.readline().split()
    r_v = [(int(line[i]), int(line[i + 1])) for i in range(1, len(line), 2)]
    g_asked[node] = r_v
    return r_v


def bfs(root=1, limit=1, max_weight=1, visited=None):
    if visited is None:
        visited = set()
    queue = [root]
    visited.add(root)
    limit -= 1
    while queue:
        vertex = queue.pop(0)
        for neighbour in get_neighbors(vertex):
            if (neighbour[1] <= max_weight) and (neighbour[0] not in visited):
                visited.add(neighbour[0])
                limit -= 1
                if limit <= -1:
                    return 0, visited
                queue.append(neighbour[0])
    return 1, visited


def approx_connected_comps(s=1, n=1, i=1, visited=None):
    if visited is None:
        visited = set()
    b_sum = 0
    for j in random.sample(range(0, N), s):
        x_rand = random.random()
        u = int(j)
        x = 1.0 // (1.0 - x_rand)
        if u not in visited:
            ret_v, visited = bfs(u, x, i, visited)
            b_sum += ret_v
    a = (n / s) * b_sum
    return a, visited


def approx_msf_weight(W=1, n=1, max_sample=1):
    if W == 0:
        return 0
    sq = math.sqrt(N)
    s = max(int(statistics.mean([sq / 100, sq / 10])), 50)
    c_sum = 0
    acc = 0
    for i in range(1, W + 1):
        acc, visited = approx_connected_comps(s, n, i, set())
        c_sum += acc
    return n - W + c_sum - acc * (W + 1) if acc >= 2 else n - W + c_sum


weight = approx_msf_weight(maxWeight, N, maxNodes)
print(f"end {weight}")
sys.stdout.flush()
