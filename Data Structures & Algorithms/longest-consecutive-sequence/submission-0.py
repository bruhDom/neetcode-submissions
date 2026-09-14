class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        # Find longest sequence of nums
        # Could store the values and index in order in hashmap, then print out values
        # First element may not always be smallest.

        # elements in original array do not need to be consecutive
        # element n + 1 must be 1 greater than element n

        elements = set(nums)
        longest_sequence = 0
        
        for num in nums:
            i = 1
            if (num - 1) not in elements:
                while num+1 in elements:
                    i += 1
                    num += 1
                if i > longest_sequence:
                    longest_sequence = i
            else:
                continue

        return longest_sequence





        



