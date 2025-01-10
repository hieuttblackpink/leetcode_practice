# Medium
# You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.
# In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.
# Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.
# Each answer[i] is calculated considering the initial state of the boxes.

from typing import List

class Solution:
    def minOperations(boxes: str) -> List[int]:
        n = len(boxes)
        r = [0] * n

        l_c = 0
        l_b = 0
        for i in range(n):
            r[i] += l_c
            if boxes[i] == '1':
                l_b += 1
            l_c += l_b

        r_c = 0
        r_b = 0
        for i in range(n - 1, -1, -1):
            r[i] += r_c
            if boxes[i] == '1':
                r_b += 1
            r_c += r_b
        
        return r
    
boxes1 = "110" # Expect output: [1,1,3]
boxes2 = "001011" # Expect output: [11,8,5,4,3,4]

print(Solution.minOperations(boxes2))