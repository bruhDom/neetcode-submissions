class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # res = []
        # value = 1

        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         else:
        #             value *= nums[j]
            
        #     res.append(value)
        #     value = 1

        # return res

        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1

        for j in range(len(nums) - 1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]

        return res

            
