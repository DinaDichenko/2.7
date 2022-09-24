#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    A = {"a", "f", "I", "n", "o"}
    B = {"f", "g", "o", "p", "z"}
    C = {"i", "j", "u", "w"}
    D = {"f", "h", "n", "t", "u", "y", "z"}

    X = C.union(A.intersection(B))

    AB = A.union(B)
    CD = C.union(D)
    ABCD = AB.union(CD)
    ab = ABCD.difference(AB)
    Y = ab.difference(CD)

    print("X= ", X)
    print("Y= ", Y)
