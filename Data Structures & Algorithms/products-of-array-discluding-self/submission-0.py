class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        product = 1
        zero = False
        zero_index = -1
        
        for i in range(len(nums)):
            if nums[i] == 0:
                if not zero:
                    zero = True
                    zero_index = i
                    continue
                else:
                    return output
            product = product * nums[i]

        if zero:
            output[zero_index] = product
            return output
        else:
            for i in range(len(nums)):
                output[i] = product // nums[i]
        return output
