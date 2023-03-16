# given an array of integars and an integar target find which two add up the the target


class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):   
            print (i)   
            for j in range(i, len(nums)):
                print(i)
                if nums[i] + nums[j] == target:
                    return [i,j]            
                
            
        
print(Solution.twoSum([],0))