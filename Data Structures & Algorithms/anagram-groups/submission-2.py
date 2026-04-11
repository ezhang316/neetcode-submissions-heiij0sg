class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary_list = []
        return_value = []

        for s in strs:
            d = {}
            for c in s:
                if c not in d:
                    d[c] = 1
                else:
                    d[c] += 1
            found = False
            if d in dictionary_list:
                i = dictionary_list.index(d)
                return_value[i].append(s)
                found = True
            if not found:
                dictionary_list.append(d)
                return_value.append([s])
        
        return return_value

        # for s in strs:
        #     create dictionary of characters
        #     for array in dictionary array:
        #         add if equals
        #         found = True
        #     if not found:
        #         append to result array and dictionary array