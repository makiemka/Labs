fst = [1, 1, 1]
a = int(input())
for i in range(a):
    answ = fst[0] + fst[1] + fst[2]
    print(fst[0])
    fst[0] = fst[1]
    fst[1] = fst[2]
    fst[2] = answ