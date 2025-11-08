from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagramMap:
                anagramMap[sorted_word].append(word)
            else:
                anagramMap[sorted_word] = [word]

        return list(anagramMap.values())