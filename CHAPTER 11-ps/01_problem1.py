class Vector2D:
    def __init__(self, i, j):
        self.i = i
        self.j = j


class Vector3D(Vector2D):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k


v = Vector3D(2, 3, 4)

print(v.i, "i +", v.j, "j +", v.k, "k")