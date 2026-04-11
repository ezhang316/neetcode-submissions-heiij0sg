class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # for each element, go through the rest of the list and see if
        # it's the longest consecutive sequence
        # O(n^2)

        # seen_list contains a tuple with (element, consecutive_number)
        # for each element, check if element is in seen_list:
        #     if yes, skip
        #     if no, check if element - 1 is in seen_list
        #         if yes, put seen_list.append((element, previous consecutive_number + 1))
        #         else seen_list.append((element, 0))

        # CASE WHEN element already exists in list -> do not insert


        # seen_list = {}

        # for n in nums:
        #     if n - 1 in seen_list.keys():
        #         seen_list[n] = seen_list[n - 1] + 1
        #     else:
        #         seen_list[n] = 1
        # print(seen_list)
        # return max(seen_list.values())

        # # if the element in seen_list.keys():
        # #     if element - 1 in seen_list.keys():

        # remove duplicates by putting into a set
        # sort set
        # O(nlogn)

        # remove duplicates by putting into a set
        # go through set and find chains
        # put each chain into a dictionary
        # chain cannot already be in dictionary since no duplicates
        # if chain - 1 in dictionary, dictionary[chain] = dictionary[chain - 1] + 1

        seen_set = set(nums)

        chain_dictionary = {}

        # for num in seen_set:
        #     if num - 1 not in seen_set and num - 1 not in chain_dictionary.keys():
        #         chain_dictionary[num] = 1
        #     else:
        #         chain_dictionary[num] = chain_dictionary[num - 1] + 1
        
        # if chain_dictionary.values():
        #     return max(chain_dictionary.values())
        # else:
        #     return 0


        # not in seen set
        # result = 0

        while seen_set:
            count = 1
            current = seen_set.pop()
            start = current

            while current - 1 in seen_set:
                print(current)
                seen_set.remove(current - 1)
                current -= 1
                count += 1

            if start - 1 in chain_dictionary.keys():
                chain_dictionary[start] = chain_dictionary[start - 1] + count
            else:
                chain_dictionary[start] = count
        
        print(chain_dictionary)
        if chain_dictionary:
            return max(chain_dictionary.values())
        return 0

            
            


