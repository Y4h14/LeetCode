class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        i = 0
        j = i + 1

        while j < len(words):
            # wordi = sum(ord(c) for c in words[i])
            # wordj = sum(ord(c) for c in words[j])
            wordi = sorted(words[i])
            wordj = sorted(words[j])
            if wordi == wordj:
                words.pop(j)
            else:
                j += 1
                i += 1
        
        return words
        
        