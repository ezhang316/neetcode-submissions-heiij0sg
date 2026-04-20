class Solution:

    def encode(self, strs: List[str]) -> str:
        # prefix each string with its length
        # length can be multiple digits
        # how can we figure out the length
        # delimit the length with #
        if not strs:
            return ""

        result = []

        for s in strs:
            result.append(f"{len(s)}#" + s)
        
        # print(result)
        return result


    def decode(self, s: str) -> List[str]:
        
        if not s:
            return []
        
        i = 0

        result = []

        while i < len(s):
            str_len_str = ""
            # get length
            while s[i] != '#':
                str_len_str += s[i]
                i += 1
            # print("str_len_str is : " + str_len_str)
            str_len = int(str_len_str)
            i += 1
        #    #example = 6
        #     0123456
        #    # get string
            string = ""
            for j in range(str_len):
                string += s[i]
                i += 1
                # print("s[i] is : " + s[i])
            result.append(string)
        
        return result

        



        
