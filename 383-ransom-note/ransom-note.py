class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # dict_1 = {}
        # dict_2 = {}
        # for i in ransomNote:
        #     dict_1[i] = dict_1.get(i, 0) + 1
        # for j in magazine:
        #     dict_2[j] = dict_2.get(j, 0) + 1
        # return all(dict_2.get(k, 0) >= v for k, v in dict_1.items())

        # count = {}
        # for i in magazine:
        #     count[i] = count.get(i, 0) + 1

        # for j in ransomNote:
        #     if count.get(j, 0) == 0:
        #         return False
        #     count[j] -= 1
        
        # return True
        
        return Counter(ransomNote) <= Counter(magazine)