class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        nums_sort = sorted(nums)
        start_idx = 0
        last_idx = len(nums_sort) - 1
        
        p2 = nums_sort[start_idx]
        p3 = nums_sort[last_idx]

        for i in range(len(nums_sort) - 2):

            p1 = nums_sort[i]
            start_idx = i + 1
            last_idx = len(nums_sort) - 1

            p2 = nums_sort[start_idx]
            p3 = nums_sort[last_idx]

            while start_idx < last_idx:

                if p1 + p2 + p3 < 0:
                    start_idx += 1
                    p2 = nums_sort[start_idx]

                elif p1 + p2 + p3 > 0:
                    last_idx -= 1
                    p3 = nums_sort[last_idx]
                else:
                    triplet = (p1, p2, p3)
                    if triplet not in result:
                        result.append(triplet)
                    
                    start_idx += 1
                    last_idx -= 1
                    p2 = nums_sort[start_idx]
                    p3 = nums_sort[last_idx]


                    
                    
        

        return result

                



        