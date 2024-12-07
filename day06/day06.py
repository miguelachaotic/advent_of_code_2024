from json import dumps, loads

def get_guard_pos(_map):
    rows, cols = len(_map), len(_map[0])
    for i in range(rows):
        for j in range(cols):
            if _map[i][j] == "^":
                return (i, j)
    return (0, 0)


def patrol(_map, pos=None, idx=None):
    if not pos:
        pos = get_guard_pos(_map)
        
    if not idx:
        idx = 0

    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
    rows, cols = len(_map), len(_map[0])

    visited = set()
    visited.add((pos[0], pos[1]))

    visited_entry = {} 

    while True:
        d = directions[idx]
        n = (pos[0] + d[0], pos[1] + d[1])

        if n[0] < 0 or n[0] >= rows or n[1] < 0 or n[1] >= cols:
            return True, visited, visited_entry

        if _map[n[0]][n[1]] == "#":
            idx = (idx + 1) % 4
            continue
        else:
            visited.add((n[0], n[1]))
            if n not in visited_entry:
                visited_entry[n] = (pos, idx)
            elif visited_entry[n] == (pos, idx):
                return False, None, None
            pos = n

def path(data):
    _, visited, _ = patrol(data)
    if visited == None: return 0
    return len(visited)

def loops(data):
    _, visited, visited_entry = patrol(data)
    if visited == None or visited_entry == None: return None
    visited.remove(get_guard_pos(data))
    loop_count: int = 0
    
    _map_dump = dumps(data) # Para evitar hacer deepcopies
    
    for vi, vj in visited:
        _map_copy = loads(_map_dump)
        _map_copy[vi][vj] = '#'
        
        pos = visited_entry[(vi, vj)][0]
        idx = visited_entry[(vi, vj)][1]
        
        is_leaving_copy, _, _ = patrol(_map_copy, pos, idx)
        
        if not is_leaving_copy: # Si no sale del bucle
            loop_count += 1
            
    return loop_count
    
def main() -> None:
    data: list[list[str]] = []
    
    with open('day06/input.txt', 'r') as f:
        data = [list(line) for line in f]
    
    print("Parte 1:", path(data))
    print("Parte 2:", loops(data)) # Este tarda mucho (no es eficiente)

if __name__ == '__main__':
    main()