from itertools import product

def generate_permutations_1(length: int) -> list[list[int]]:
    return [list(p) for p in product([0, 1], repeat=length)]

def generate_permutations_2(length: int) -> list[list[int]]:
    return [list(p) for p in product([0, 1, 2], repeat=length)]

def eval_perm(perm: list[int], nums: list[int]) -> int:
    res: int = nums[0]
    for i in range(len(perm)):
        if perm[i] == 0:
            res += nums[i + 1]
        elif perm[i] == 1:
            res *= nums[i + 1]
        else: 
            res = int(str(res) + str(nums[i + 1]))
    return res

def valid_line_1(target: int, nums: list[int]) -> int:
    perms: list[list[int]] = generate_permutations_1(len(nums) - 1)
    valids: int = 0
    for perm in perms:
        if target == eval_perm(perm, nums):
            valids += 1
    return valids

def valid_line_2(target: int, nums: list[int]) -> int:
    perms: list[list[int]] = generate_permutations_2(len(nums) - 1)
    valids: int = 0
    for perm in perms:
        if target == eval_perm(perm, nums):
            valids += 1
    return valids

def main() -> None:
    data: list[str] = open("day07/input.txt", 'r').readlines()
    sum1: int = 0
    sum2: int = 0
    for line in data:
        div = line.split(':')
        target: int = [*map(int, [div[0]])][0]
        nums: list[int] = [*map(int, div[1][1:].split(' '))]
        if valid_line_1(target, nums):
            sum1 += target
        if valid_line_2(target, nums):
            sum2 += target
        
    print("Parte 1:", sum1)
    print("Parte 2:", sum2) # Extremadamente lento xDDDD
    
if __name__ == '__main__':
    main()
        