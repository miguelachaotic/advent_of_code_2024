def decode(data: str) -> list[int | str]:
    parity: int = 0
    block_id: int = 0
    output: list[str] = []
    for char in data:
        if parity:
            output += ['.'] * int(char)
            parity = 0
        else:
            output += [block_id] * int(char)
            block_id += 1
            parity = 1
    return output

def compact_fragmented(parsed: list[int | str]) -> None:
    
    def swap(i: int, j: int) -> None:
        tmp = parsed[i]
        parsed[i] = parsed[j]
        parsed[j] = tmp
    
    left: int = 0
    right: int = len(parsed) - 1
    while left < right:
        if parsed[left] == '.':
            while parsed[right] == '.':
                right -= 1
            swap(left, right)
            right -= 1
        else:
            left += 1

def compact_files(inp: str) -> int:
    d: int = 0          # Parseo distinto, por eso no uso
    idx: int = 0        # la función anterior
    data: list = []
    free: list = []
    for i in inp:
        if d % 2 == 0:
            data.append([idx, int(i)])
        else:
            free.append([idx, int(i)])
        d += 1
        idx += int(i)
    
    for i in range(len(data) - 1, -1, -1):
        for j in range(len(free)):
            if free[j][0] > data[i][0]:
                break
            if free[j][1] >= data[i][1]:
                data[i][0] = free[j][0]
                if free[j][1] == data[i][1]:
                    free.pop(j)
                else:
                    free[j][0] += data[i][1]
                    free[j][1] -= data[i][1]
                break
    output: int = 0
    for i in range(len(data)):
        output += i * sum(range(data[i][0], data[i][0] + data[i][1]))
    return output
            

def checksum(parsed: list[int | str]) -> int:
    return sum(i * block for i, block in enumerate(parsed) if block != ".")
                        
def main() -> None:
    data: str = open('day09/input.txt', 'r').read().strip('\n')
    parsed: list = decode(data)
    compact_fragmented(parsed)
    checksum1: int = checksum(parsed)
    checksum2: int = compact_files(data)
    print("Parte 1:", checksum1)
    print("Parte 2:", checksum2)


if __name__ == '__main__':
    main()