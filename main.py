from functools import reduce
from math import log, sqrt


class Proof:
    def actual(self, a, b):
        return sqrt(a ** 2 + b ** 2)

    def factor(self, n):
        return reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0))

    def factorize(self, n):
        factors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                factors.append(i)
                factors.append(n // i)
        return factors

    def prove(self, a, b, p=False):
        c = b % round(log(a ** b, 2) + log(b ** a, 2))
        d = (b % a)
        e = len(self.factor(c))
        f = (d % e)
        g = ((a % b) % (b % a))
        h = c
        c += f - g
        j = (b % (round(log(a ** b, 2) + log(b ** a, 2)))) + (((b % a) % len(self.factor(c))) - ((a % b) % (b % a)))
        if p:
            # print(float(c))
            print(j)

        return [float(c), d, e, f, g, h]

    def compare(self, a, b, a1, b1, p=False):
        myproof = self.prove(a, b, p=True)
        mine = myproof[0]
        d = myproof[1]
        e = myproof[2]
        f = myproof[3]
        g = myproof[4]
        actual = self.actual(a, b)
        print('==================\n')
        print(
            f'Mine: {mine}\tActual: {actual}\nCurrent A: {a1}\tCurrent B: {b1}\nOriginal A, B: ({a}, {b})\nD: {d}\tE: {e}\nF: {f}\nG: {g}')

    def print_h(self, a, b):
        return self.prove(a, b)[5]


if __name__ == '__main__':
    p = True
    proof = Proof()

    a1 = 3
    b1 = 4
    a2 = 5
    b2 = 12
    a3 = 8
    b3 = 15
    proof.print_h(3, 4)
    print(proof.factorize(proof.print_h(3, 4)))
    print(proof.factorize(proof.print_h(5, 12)))
    print(proof.factorize(proof.print_h(8, 15)))

    # for i in range(1, 5):
    #     a1_, b1_ = a1 * i, b1 * i
    #     a2_, b2_ = a2 * i, b2 * i
    #     a3_, b3_ = a3 * i, b3 * i

    #     proof.compare(a1_, b1_, a1, b1, p)
    #     proof.compare(a2_, b2_, a2, b2, p)
    #     proof.compare(a3_, b3_, a3, b3, p)

    # (3, 4), (5, 12), (8, 15), (3, 4), (5, 12)
    # (45, 60), (75, 180), (120, 225), (48, 64), (80, 192)
