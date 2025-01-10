# Medium
# You are given two string arrays words1 and words2.
# A string b is a subset of string a if every letter in b occurs in a including multiplicity.
# For example, "wrr" is a subset of "warrior" but is not a subset of "world".
# A string a from words1 is universal if for every string b in words2, b is a subset of a.
# Return an array of all the universal strings in words1. You may return the answer in any order.

from typing import List

class Solution:
    def wordSubsets(words1: List[str], words2: List[str]) -> List[str]:
        def count_freq(word: str):
            freq = [0] * 26
            for c in word:
                freq[ord(c) - ord('a')] += 1
            return freq

        max_freq = [0] * 26
        for w in words2:
            w_f = count_freq(w)
            for i in range(26):
                max_freq[i] = max(max_freq[i], w_f[i])

        r = []
        for w in words1:
            w_f = count_freq(w)
            c = True
            for i in range(26):
                if w_f[i] < max_freq[i]:
                    c = False
                    break
            if c:
                r.append(w)
        
        return r
    
test_case_1 = {
    "words1": ["amazon","apple","facebook","google","leetcode"],
    "words2": ["e","o"],
} # Expect output: ["facebook","google","leetcode"]

test_case_2 = {
    "words1": ["amazon","apple","facebook","google","leetcode"],
    "words2": ["l","e"],
} # Expect output: ["apple","google","leetcode"]

print(Solution.wordSubsets(test_case_1["words1"], test_case_1["words2"]))