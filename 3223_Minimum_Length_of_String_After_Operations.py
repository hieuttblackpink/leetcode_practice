# Medium
# You are given a string s.
# You can perform the following process on s any number of times:
# Choose an index i in the string such that there is at least one character to the left of index i that is equal to s[i], and at least one character to the right that is also equal to s[i].
# Delete the closest character to the left of index i that is equal to s[i].
# Delete the closest character to the right of index i that is equal to s[i].
# Return the minimum length of the final string s that you can achieve.

class Solution:
    def minimumLength(s: str) -> int:
        n = len(s)
        if n <= 2:
            return n

        freq = {}
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

        r = 0
        for k, v in freq.items():
            if v % 2 != 0:
                r += 1
            else:
                r += 2

        return r
    
s1 = "abaacbcbb" # Expect result: 5
print(Solution.minimumLength(s1))