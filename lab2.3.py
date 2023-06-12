n = int(input('Введите число: '))
result = n
if not sname in sets:
    sets.add(sname)
    sets2.add(sname)
elif sname in sets2:
    a += 2
    sets2.remove(sname)
else:
    a += 1

print(a)
