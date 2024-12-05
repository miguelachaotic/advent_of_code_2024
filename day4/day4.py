def find_word_in_grid(grid: list[str], word: str):
    
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),   # Horizontal right
        (0, -1),  # Horizontal left
        (1, 0),   # Vertical down
        (-1, 0),  # Vertical up
        (1, 1),   # Diagonal down-right
        (1, -1),  # Diagonal down-left
        (-1, 1),  # Diagonal up-right
        (-1, -1)  # Diagonal up-left
    ]

    def is_valid(x: int, y: int):
        return 0 <= x < rows and 0 <= y < cols

    def search_from(x: int, y: int, dx: int, dy: int):
        
        for k in range(word_len):
            nx, ny = x + k * dx, y + k * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[k]:
                return False
        return True

    count = 0
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if search_from(i, j, dx, dy):
                    count += 1
    return count

def find_x_mas_pattern(grid: list[str]):
    rows, cols = len(grid), len(grid[0])
    pattern_count = 0

    # Define relative positions for all 8 orientations of the pattern
    patterns = [
        # Original orientation
        [(-1, -1, 'M'), (-1, 1, 'S'), (1, -1, 'M'), (1, 1, 'S')],
        # Rotated 90°
        [(-1, -1, 'M'), (-1, 1, 'M'), (1, -1, 'S'), (1, 1, 'S')],
        # Rotated 180°
        [(-1, -1, 'S'), (-1, 1, 'M'), (1, -1, 'S'), (1, 1, 'M')],
        # Rotated 270°
        [(-1, -1, 'S'), (-1, 1, 'S'), (1, -1, 'M'), (1, 1, 'M')],
    ]

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if grid[i][j] == 'A':  
                for pattern in patterns:
                    if all(
                        grid[i + dx][j + dy] == char for dx, dy, char in pattern
                    ):
                        pattern_count += 1

    return pattern_count

def main() -> None:
    grid: list[str] = open("day4/input.txt", 'r').readlines()
    word: str = "XMAS"
    occurrences = find_word_in_grid(grid, word)
    x_mas_occurrences = find_x_mas_pattern(grid)
    print("Parte 1:", occurrences)
    print("Parte 2:", x_mas_occurrences)

if __name__ == '__main__':
    main()
