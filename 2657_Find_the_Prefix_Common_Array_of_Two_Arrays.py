# Medium
# You are given two 0-indexed integer permutations A and B of length n.
# A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.
# Return the prefix common array of A and B.
# A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

from typing import List

class Solution:
    def findThePrefixCommonArray(A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        m = {}
        c = 0
        r = [0] * n
        for i in range(n):
            if A[i] not in m:
                m[A[i]] = 1
            else:
                c += 1
            if B[i] not in m:
                m[B[i]] = 1
            else:
                c += 1
            r[i] = c
        return r
    
A = [1, 3, 2, 4]
B = [3, 1, 2, 4]
C = Solution.findThePrefixCommonArray(A, B) # Expect output: [0,2,3,4]
print(C)

A = [2, 3, 1]
B = [3, 1, 2]
C = Solution.findThePrefixCommonArray(A, B) # Expect output: [0,1,3]
print(C)