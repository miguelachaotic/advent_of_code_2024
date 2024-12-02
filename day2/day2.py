import math

def is_safe(line : list[int]) -> bool:
    dec = False ; inc = False
    for i in range(len(line)-1):
        if line[i+1] > line[i] and dec:
            return False
        elif line[i+1] < line[i] and inc:
            return False
        else:
            if (0 == math.fabs(line[i+1] - line[i])) or math.fabs(line[i+1] - line[i]) > 3: return False
            elif line[i+1] > line[i]: inc = True
            else: dec = True
    return True

def is_extra_safe(line : list[int]) -> bool:
    for i in range(len(line)):
        new_list = [x for j, x in enumerate(line) if j != i]
        if(is_safe(new_list)):
            return True
        
    return False

def main():
    safes = 0
    safes_no_deleting = 0
    with open("input.txt", 'r') as input:
        lines = input.readlines()
        for line in lines:
            line = [*map(int, line.split(' '))]
            if is_safe(line):
                safes = -~safes
                safes_no_deleting = -~safes_no_deleting
            elif is_extra_safe(line):
                safes = -~safes
    print("No deleting (part 1):", safes_no_deleting.__str__())
    print("Deleting one or zero (part 2):", safes.__str__())

    

if __name__ == '__main__':
    main()
        