class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def plus(self, vector):
        self.x = self.x + vector.x
        self.y = self.y + vector.y
        self.z = self.z + vector.z
        return self

    def minus(self, vector):
        self.x -= vector.x
        self.y -= vector.y
        self.z -= vector.z
        return self

    def umnogenie(self, number):
        self.x *= number
        self.y *= number
        self.z *= number
        return self

    def scaliarnoe_umnogenie(self, vector):
        a = self.x * vector.x + self.y * vector.y + self.z * vector.z
        return a

    def vectornoe_unmogenie(self, vector):
        first = self.y * vector.z - self.z * vector.y
        second = self.x * vector.z - self.z * vector.x
        third = self.x * vector.y - self.y * vector.x
        self.x = first
        self.x = second
        self.x = third
        return self

vector = Vector(1,2,3)
vector1 = Vector(2,3,4)
vector2 = Vector(2,3,4)
vector3 = Vector(2,3,4)
vector4 = Vector(4,5,6)
result = vector.plus(vector1)
print(result.x, result.y, result.z)
result2 = vector.minus(vector2)
print(result2.x, result2.y, result2.z)
result3 = vector.umnogenie(5)
print(result3.x, result3.y, result3.z)
result4 = vector.scaliarnoe_umnogenie(vector3)
print(result4)
result5 = vector.vectornoe_unmogenie(vector4)
print(result5.x, result5.y, result5.z)
