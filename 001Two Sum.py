class Solution:
    def twoSum(self, nums, target):
        hashMap = {}
        for ind,value in enumerate(nums):
            hashMap[value] = ind
        for ind2,value2 in enumerate(nums):
            if target-value2 in hashMap:
                ind3 = hashMap[target - value2]
                if ind2 != ind3:
                    return ind2,ind3
if __name__ == '__main__':
    print(Solution().twoSum([3,2,4],6))