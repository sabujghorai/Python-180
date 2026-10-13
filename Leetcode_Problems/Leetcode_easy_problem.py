# 2235. Add Two Integers


# sum1 = int(input("Enter a number :"))
# sum2 = int(input("Enter another number :"))

# print(sum1+sum2)



# 1480. Running Sum of 1d Array


# Hint
# Given an array nums. We define a 
# running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].


nums = [1,2,3,4]
empty_list = []
total = 0

for num in nums:
    total += num
    empty_list.append(total)
print(empty_list)



class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
