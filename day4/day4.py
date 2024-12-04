

def check_upper_left(s: list[str], start: tuple[int, int]) -> bool:
    if start[0] < 3 or start[1] < 3: return False
    return s[start[0] - 1][start[1] - 1] == 'M' and \
        s[start[0] - 2][start[1] - 2] == 'A' and \
        s[start[0] - 3][start[1] - 3] == 'S'

def check_up(s: list[str], start: tuple[int, int]) -> bool:
    if start[1] < 3: return False
    return s[start[0]][start[1] - 1] == 'M' and \
        s[start[0]][start[1] - 2] == 'A' and \
        s[start[0]][start[1] - 3] == 'S'
        
def check_upper_right(s: list[str], start: tuple[int, int]) -> bool:
    if start[0] >= len(s) - 3 or start[1] < 3: return False
    return s[start[0] + 1][start[1] - 1] == 'M' and \
        s[start[0] + 2][start[1] - 2] == 'A' and \
        s[start[0] + 3][start[1] - 3] == 'S'
 
def check_right(s: list[str], start: tuple[int, int]) -> bool:
    if start[0] >= len(s) - 3: return False
    return s[start[0] + 1][start[1]] == 'M' and \
        s[start[0] + 2][start[1]] == 'A' and \
        s[start[0] + 3][start[1]] == 'S'
        
def check_bottom_right(s: list[str], start: tuple[int, int]) -> bool:
    if start[0] >= len(s) - 3 or start[1] >= len(s[0]) - 3: return False
    return s[start[0] + 1][start[1] + 1] == 'M' and \
        s[start[0] + 2][start[1] + 2] == 'A' and \
        s[start[0] + 3][start[0] + 3] == 'S'

def check_down(s: list[str], start: tuple[int, int]) -> bool:
    if start[1] >= len(s[0]) - 3: return False
    return s[start[0]][start[1] + 1] == 'M' and \
        s[start[0]][start[1] + 2] == 'M' and \
        s[start[0]][start[1] + 3] == 'S'
        
def check_bottom_left(s: list[str], start: tuple[int, int]) -> bool:
    if start[0] < 3 or start[1] >= len(s[0]) - 3: return False
    return s[start[0] - 1][start[1] + 1] and \
        s[start[0] - 2][start[1] + 2] and \
        s[start[0] - 3][start[1] + 3]
        
def check_left(s: list[str], start: tuple[int, int]) -> bool:
    if start[0] < 3: return False
    return s[start[0] - 1][start[1]] == 'M' and \
        s[start[0] - 2][start[1]] == 'A' and \
        s[start[0] - 3][start[1]] == 'S'


def check_xmas(s: list[str], position: tuple[int, int]) -> int:
    if s[position[0]][position[1]] != 'X': return 0
    total: int = 0
    if check_upper_left(s, position): total += 1
    if check_up(s, position): total += 1
    if check_upper_right(s, position): total += 1
    if check_right(s, position): total += 1
    if check_bottom_right(s, position): total += 1
    if check_down(s, position): total += 1
    if check_bottom_left(s, position): total += 1
    if check_left(s, position): total += 1
    return total

def main() -> None:
    data: list[str] = open('input.txt').readlines()
    total: int = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            total += check_xmas(data, (i, j))
    print("Parte 1:", total)
            
    
if __name__ == '__name__':
    main()
