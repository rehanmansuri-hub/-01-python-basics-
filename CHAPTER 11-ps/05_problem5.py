class Vector:

    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        result = []

        for i in range(len(self.values)):
            result.append(self.values[i] + other.values[i])

        return Vector(result)

    def __mul__(self, other):
        result = 0

        for i in range(len(self.values)):
            result += self.values[i] * other.values[i]

        return result


v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

v3 = v1 + v2

print(v3.values)

print(v1 * v2)