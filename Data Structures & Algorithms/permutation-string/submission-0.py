class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
            if len(s2) < len(s1):
                return False

            freq_s1 = {}
            k = len(s1)

            for ch in s1:
                if ch in freq_s1:
                    freq_s1[ch] += 1
                else:
                    freq_s1[ch] = 1
            freq_s2 = {}

            for i in range(k):
                if s2[i] in freq_s2:
                    freq_s2[s2[i]] += 1
                else:
                    freq_s2[s2[i]] = 1

            if freq_s2 == freq_s1:
                return True

            for right in range(len(s1), len(s2)):
                if s2[right] in freq_s2:
                    freq_s2[s2[right]] += 1
                else:
                    freq_s2[s2[right]] = 1

                leaving = s2[right - k]
                freq_s2[leaving] -= 1

                if freq_s2[leaving] == 0:
                    del freq_s2[leaving]
                if freq_s2 == freq_s1:
                    return True
            return False
        