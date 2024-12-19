def get_score_sum(data: list[str]) -> int:
    
    def inside(i: int, j: int) -> bool:
        return i >= 0 and j >= 0 and i < len(data) and j < len(data[0])
    
    def up(i: int, j: int) -> bool:
        return (data[i - 1][j] - data[i][j]) == 1
    
    def down(i: int, j: int) -> bool:
        return (data[i + 1][j] - data[i][j]) == 1
    
    def left(i: int, j: int) -> bool:
        return (data[i][j - 1] - data[i][j]) == 1
    
    def right(i: int, j: int) -> bool:
        return (data[i][j +1] - data[i][j]) == 1
    
    
    def get_score(i: int, j: int) -> int:
        score1: int = 0
        score2: int = 0
        score3: int = 0
        score4: int = 0
        
        if data[i][j] == 9: return 1
        if inside(i - 1, j) and up(i, j):    score1 = get_score(i - 1, j)
        if inside(i + 1, j) and down(i, j):  score2 = get_score(i + 1, j)
        if inside(i, j - 1) and left(i, j):  score3 = get_score(i, j - 1)
        if inside(i, j + 1) and right(i, j): score4 = get_score(i, j + 1)
        #print(data[i][j], sum([score1, score2, score3, score4]))
        return sum([score1, score2, score3, score4])
    
    score_sum: int = 0
    
    for i in range(len(data)):
        for j, c in enumerate(data[i]):
            if c == 0:
                score_sum += get_score(i, j)
    return score_sum
    




def main() -> None:
    data: list[str] = open('day10/input.txt', 'r').readlines()
    
    data_int: list[list[int]] = []
    
    for line in data:
        data_int.append([*map(int, [c for c in line.strip('\n')])])
    
    data: list[list[int]] = data_int
            
    score_sum: int = get_score_sum(data)
    print("Parte 2:", score_sum)
    
if __name__ == '__main__':
    main()
    