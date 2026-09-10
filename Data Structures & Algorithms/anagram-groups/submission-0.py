class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for word in strs:
            char_freq = {}

            for char in word:
                if char in char_freq:
                    char_freq[char] += 1
                else:
                    char_freq[char] = 1

            key = tuple(sorted(char_freq.items()))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())



        