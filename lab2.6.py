from collections import Counter
s = input('Введите строку: ').lower()
L = Counter(s).most_common()
maxNminS = ['я', 0]
for i in range(len(L)):
    if L[i][1] > maxNminS[1]:
        maxNminS = L[i]
    elif L[i][1] == maxNminS[1]:
        if ord(L[i][0]) < ord(maxNminS[0]):
            maxNminS = L[i]
if ord(maxNminS[0]) == 32:
    print('символ пробела')
else:
    print(maxNminS[0])