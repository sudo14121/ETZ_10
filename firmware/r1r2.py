number = int(input("КОЛИЧЕСТВО ЧИСЕЛ "))

def output(F):
    naborone = 0
    n = 2 ** number
    for A in [0, 1]:
        for B in [0, 1]:
            for C in [0, 1]:
                for D in [0, 1]:
                    print(f"{A} | {B} | {C} | {D} | {F(A, B, C, D)}")
                    
                    naborone += F(A, B, C, D)
    if naborone == 0:
        print("ПРОТИВОРЕЧИЕ")
    elif naborone == n:
        print("ТАВТОЛОГИЯ")
    else:
        print("ВЫЧИСЛИМОЕ")
        
    print(f"КОЛИЧСЕТВО ИСТИННЫХ {naborone}")
    print(f"КОЛИЧЕСТВО СТРОК {n}")         
    
F = lambda A, B, C, D: int(A or B or C or D)
print("A | B | C | D | F")
output(F)