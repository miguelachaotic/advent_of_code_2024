positions: dict[str, list[tuple[int, int]]] = {}
antinodes: set[tuple[int, int]] = set()
more_antinodes: set[tuple[int, int]] = set()

def parse_input(data: list[str]) -> None:
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '.' or data[i][j] == '\n': continue
            if data[i][j] in positions:
                positions[data[i][j]].append((i, j))
            else:
                positions[data[i][j]] = [(i, j)]


    
              
def check_antinodes(data: list[str], frequency: str) -> None:
    
    def inside(x: int, y: int, dx: int, dy: int) -> bool:
        return x + dx >= 0 and y + dy >= 0 and \
            x + dx < len(data) and y + dy < len(data[0])
    
    def all_antinodes(x, y, dx, dy) -> None:
        if not inside(x, y, dx, dy): return
        new_x: int = x + dx
        new_y: int = y + dy
        more_antinodes.add((new_x, new_y))
        all_antinodes(new_x, new_y, dx, dy)
    
    
    antennas: list[tuple[int, int]] = positions[frequency]
    for i in range(len(antennas)):
        for j in range(len(antennas)):
            if i != j:
                dx: int = antennas[i][0] - antennas[j][0]
                dy: int = antennas[i][1] - antennas[j][1]
                x: int = antennas[i][0] + dx
                y: int = antennas[i][1] + dy
                if inside(antennas[i][0], antennas[i][1], dx, dy):
                    antinodes.add((x, y))
                all_antinodes(antennas[i][0], antennas[i][1], dx, dy)    # primero en una direccion
                all_antinodes(antennas[i][0], antennas[i][1], -dx, -dy)  # luego en la direccion contraria
                more_antinodes.add((x - dx, y - dy))
                    
                    
def main() -> None:
    data: list[str] = open('day08/input.txt', 'r').readlines()
    data = [line.strip() for line in data]
    parse_input(data)
    for freq in positions.keys():
        check_antinodes(data, freq)
         
    print("Parte 1:", len(antinodes))
    print("Parte 2:", len(more_antinodes))
    
    


if __name__ == '__main__':
    main()