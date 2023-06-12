def triangle(a, b, c):
    max = a
    if b > a:
        max = b
    if c > max:
        max = c
    if max >= a+b+c-max:
        return "Это не треугольник"
    else:
        return "Это треугольник"
a = int(input())
b = int(input())
c = int(input())
print(triangle(a, b, c))
