def parse_mul(s: str, begin: int) -> int | None:
    num1 = "" ; num2 = ""
    numerical: list[str] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if(s[begin - 1] != '('):
        return None
    while(s[begin] != ','):
        if(s[begin] not in numerical): return None
        num1 += s[begin]
        begin = -~begin
    begin = -~begin
    
    while(s[begin] != ')'):
        if(s[begin] not in numerical): return None
        num2 += s[begin]
        begin = -~begin
    num1 = int(num1)
    num2 = int(num2)
    return num1 * num2

def main() -> None:
    data: str = open('input.txt', 'r').read()
    sum1: int = 0
    sum2: int = 0
    do: str = "do()"
    dont: str = "don't()"
    enabled: bool = True

    for i in range(len(data)):
        if data[i:i+4] == do:
            enabled = True
        elif data[i:i+7] == dont:
            enabled = False
        if data[i:i+3] == 'mul':
            prod: int | None = parse_mul(data, i+4)
            if prod == None:
                continue
            if enabled: sum2 += prod
            sum1 += prod
    print("Parte 1:", sum1)
    print("Parte 2:", sum2)

if __name__ == '__main__':
    main()