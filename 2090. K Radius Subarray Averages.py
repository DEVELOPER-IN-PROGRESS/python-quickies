class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if not k :
            return nums
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        
        res = [-1]*len(nums)

        for i in range(len(nums)):
            if i - k < 0 or i + k > len(nums) -1:
                continue 
            else:
                if i - k -1 <0:
                    b = 0 
                else:
                    b = nums[i-k-1]
                tsum = (nums[i+k] - b)// (2*k +1)
                res[i] = tsum 

        return res  
