



def parse_mul(s: str, begin: int) -> int | None:
    num1 = "" ; num2 = ""
    if(s[begin] != '('):
        return None
    while(s[begin] != ','):
        num1 += s[begin]
        begin = -~begin
    begin = -~begin
    while(s[begin] != ')'):
        num2 += s[begin]
        begin = -~begin
    num1 = int(num1)
    num2 = int(num2)
    print(num1, num2)
    return num1 * num2

    


def main() -> None:
    data: str = open('input.txt', 'r').read()
    sum: int = 0

    for i in range(len(data)):
        if data[i:i+3] == 'mul':
            prod: int | None = parse_mul(data, i+4)
            if prod == None:
                continue
            sum += prod
    print("Parte 1: ", sum)

if __name__ == '__main__':
    main()