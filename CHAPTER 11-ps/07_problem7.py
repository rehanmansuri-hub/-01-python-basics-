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

    def __len__(self):
        return len(self.values)


v = Vector([1, 2, 3, 4, 5])

print(len(v))