from sympy.combinatorics import Permutation, PermutationGroup

class sym:
    def __init__(self, n) -> None:
        self.trans = []
        for i in range(1, n):
            self.trans.append(Permutation(i, i+1))
    def grp(self):
        return PermutationGroup(self.trans)

class representation(sym):
    def __init__(self, n) -> None:
        super().__init__(n)
        self.id_matrix = []
        for i in range(n):
            col = [0]*n
            col[i] = 1
            self.id_matrix.append(col)
    def print(self, element: Permutation):
        self.matrix = []


print(Permutation(1,3,2)(3))