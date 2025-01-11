# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 23:07:06 2023

@author: nm
"""

import numpy as np
from sympy.combinatorics import Permutation, PermutationGroup

F = Permutation(2, 19, 21, 8)(3, 17, 20, 10)(4, 6, 7, 5)
R = Permutation(1, 5, 21, 14)(3, 7, 23, 12)(8, 10, 11, 9)
D = Permutation(6, 18, 14, 10)(7, 19, 15, 11)(20, 22, 23, 21)

G = PermutationGroup(F, R, D)
G.order()