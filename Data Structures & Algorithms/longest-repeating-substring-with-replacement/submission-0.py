class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        counts = {}
        max_freq = 0
        best = 0

        for right in range(len(s)):
            if s[right] in counts:
                counts[s[right]] += 1
            else:
                counts[s[right]] = 1

            max_freq = max(counts.values())

            while (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1
                max_freq = max(counts.values())

            if (right - left + 1) > best:
                best = (right - left + 1)

        return best