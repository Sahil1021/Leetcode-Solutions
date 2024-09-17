class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        words = s1.split() + s2.split()

        wordscount={}

        for word in words:
            if word in wordscount:
                wordscount[word] +=1
            else:
                wordscount[word] = 1

        uncommon_words = []

        for word in wordscount:
            if wordscount[word] == 1:
                uncommon_words.append(word)

        return uncommon_words