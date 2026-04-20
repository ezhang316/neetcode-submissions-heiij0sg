class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary_list = {}
        return_value = []

        for s in strs:
            d = {}
            for c in s:
                if c not in d:
                    d[c] = 1
                else:
                    d[c] += 1
            d = frozenset(d)
            if d not in dictionary_list:
                return_value.append([s])
                dictionary_list[d] = return_value.index([s])
            else:
                return_value[dictionary_list[d]].append(s)
        
        return return_value