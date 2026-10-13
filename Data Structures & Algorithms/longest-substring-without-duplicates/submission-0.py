class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        best = 0
        seen = set()
        for i in range(len(s)):
            if s[i] in seen:
                while s[i]  in seen:
                    seen.remove(s[left])

                    left += 1

            else:
                seen.add(s[i])
                
            seen.add(s[i])

            if (i - left + 1) > best:
                best = i  - left + 1

        return best
        