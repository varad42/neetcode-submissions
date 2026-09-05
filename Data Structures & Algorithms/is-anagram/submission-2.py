class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freq_s = {}
        freq_t = {}
        for i in s:
            if i in freq_s:
                freq_s[i] = freq_s[i] + 1
            else:
                freq_s[i] = 1
        
        for i in t:
            if i in freq_t:
                freq_t[i] = freq_t[i] + 1
            else:
                freq_t[i] = 1
        return freq_t == freq_s

                