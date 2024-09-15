
# Problem: Walls and Gates (LeetCode 663)

## Problem Statement

You are given a 2D grid of size `m x n` initialized with the following three possible values:

- **-1**: A wall or an obstacle.
- **0**: A gate.
- **INF**: Infinity, represented by the value `2147483647` (which is `2^31 - 1`). This denotes an empty room, and you can assume the distance to a gate is always less than this value.

### Task
For each empty room (INF), fill it with the distance to its nearest gate. If it is impossible to reach a gate, leave the value as `INF`.

### Example 1:

#### Input:
```plaintext
[[2147483647,-1,0,2147483647],
 [2147483647,2147483647,2147483647,-1],
 [2147483647,-1,2147483647,-1],
 [0,-1,2147483647,2147483647]]
```

#### Output:
```plaintext
[[3,-1,0,1],
 [2,2,1,-1],
 [1,-1,2,-1],
 [0,-1,3,4]]
```

#### Explanation:
The initial 2D grid is:
```
INF  -1   0   INF
INF  INF  INF  -1
INF  -1   INF  -1
 0   -1   INF  INF
```
After calculating the shortest distances to the nearest gates, the resulting grid is:
```
 3   -1    0    1
 2    2    1   -1
 1   -1    2   -1
 0   -1    3    4
```

### Example 2:

#### Input:
```plaintext
[[0,-1],
 [2147483647,2147483647]]
```

#### Output:
```plaintext
[[0,-1],
 [1,2]]
```

#### Explanation:
The grid is initially:
```
 0  -1
INF  INF
```
The distances from the nearest gate are:
```
 0  -1
 1   2
```

### Constraints:
- The `m x n` grid will have at least one gate.
- It is guaranteed that there are no cycles, meaning there is no way to loop back to an already visited cell.

### Approach:
The idea is to treat the gates (cells with value `0`) as sources and perform a breadth-first search (BFS) to fill the empty rooms (cells with value `INF`) with the minimum distance to any gate.
