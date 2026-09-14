class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        first_i = 0
        last_i = len(numbers) - 1
        p1 = numbers[first_i]
        p2 = numbers[last_i]

        while first_i < last_i:
    
            if p1 + p2 > target:
                last_i -= 1
                p2 = numbers[last_i]
            elif p1 + p2 < target:
                first_i += 1
                p1 = numbers[first_i]
            elif p1 + p2 == target:
                return [first_i + 1, last_i + 1]
            
