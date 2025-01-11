# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 23:07:06 2023

@author: nm
"""

# Reference: https://docs.sympy.org/latest/modules/combinatorics/perm_groups.html

import numpy as np
from sympy.combinatorics import free_group, Permutation, PermutationGroup
from sympy.combinatorics import Polyhedron
from sympy.combinatorics.named_groups import CyclicGroup
from sympy.combinatorics.homomorphisms import homomorphism
from sympy.combinatorics.fp_groups import FpGroup
from sympy.combinatorics.named_groups import SymmetricGroup
from sympy.combinatorics.testutil import _verify_bsgs
from sympy.combinatorics.named_groups import AlternatingGroup


F = Permutation(2, 19, 21, 8)(3, 17, 20, 10)(4, 6, 7, 5)
R = Permutation(1, 5, 21, 14)(3, 7, 23, 12)(8, 10, 11, 9)
D = Permutation(6, 18, 14, 10)(7, 19, 15, 11)(20, 22, 23, 21)

G = PermutationGroup(F, R, D)
G.order()

A = Permutation(2, 1)
B = Permutation(1, 0)
G = PermutationGroup(A, B)
P = Polyhedron(list('ABC'), pgroup=G)
P.corners
P.rotate(0) # apply permutation 0
P.corners
P.reset()
P.corners

P10 = G.make_perm([0, 1])
print(P10('ABC'))

G = CyclicGroup(5)
H = G*G
print(H)

H = PermutationGroup(Permutation(0, 2), Permutation (1, 5))
K = PermutationGroup(Permutation(5)(0, 2))
F = free_group("x_0 x_1")[0]
gens = F.generators
phi = homomorphism(F, H, F.generators, H.generators)
rels_k = [gens[0]**2] # relators for presentation of K
z= Permutation(1, 5)
check, rels_h = H._verify(K, phi, z, 1)
check
rels = rels_k + rels_h
G = FpGroup(F, rels) # presentation of H
G.order() == H.order()

from sympy.combinatorics import Permutation, PermutationGroup
a = Permutation([0, 2, 1])
b = Permutation([1, 0, 2])
G = PermutationGroup([a, b])
G.abelian_invariants()

from sympy.combinatorics import CyclicGroup
G = CyclicGroup(7)
G.abelian_invariants()

G = PermutationGroup([Permutation(0, 1, 3)(2, 4)])
G.base

S = SymmetricGroup(4)
S.schreier_sims()
S.base
base, gens = S.baseswap(S.base, S.strong_gens, 1, randomized=False)
base, gens

S1 = PermutationGroup(gens)
_verify_bsgs(S1, base, gens)

S = SymmetricGroup(4)
S.basic_orbits

A = AlternatingGroup(4)
A.schreier_sims()
A.base
for g in A.basic_stabilizers:
    print(g)

A = AlternatingGroup(4)
A.basic_transversals

