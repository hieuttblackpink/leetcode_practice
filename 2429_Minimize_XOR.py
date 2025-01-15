# Medium
# Given two positive integers num1 and num2, find the positive integer x such that:
# x has the same number of set bits as num2, and
# The value x XOR num1 is minimal.
# Note that XOR is the bitwise XOR operation.
# Return the integer x. The test cases are generated such that x is uniquely determined.
# The number of set bits of an integer is the number of 1's in its binary representation.

class Solution:
    def minimizeXor(num1: int, num2: int) -> int:
        c = bin(num2).count('1')
        x = 0
        for i in range(31, -1, -1):
            if c == 0:
                break
            if num1 & (1 << i):
                x |= (1 << i)
                c -= 1
        for i in range(32):
            if c == 0:
                break
            if not (x & (1 << i)):
                x |= (1 << i)
                c -= 1
        return x
    
num1 = 3
num2 = 5
x = Solution.minimizeXor(num1, num2) #Expect output: 3
print(x)

num1 = 1
num2 = 12
x = Solution.minimizeXor(num1, num2) #Expect output: 3
print(x)

num1 = 7
num2 = 2
x = Solution.minimizeXor(num1, num2) #Expect output: 4
print(x)