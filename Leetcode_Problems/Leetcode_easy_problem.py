# 2235. Add Two Integers


sum1 = int(input("Enter a number :"))
sum2 = int(input("Enter another number :"))

print(sum1+sum2)



# 1480. Running Sum of 1d Array

# Hint
# Given an array nums. We define a 
# running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4



nums = [1,2,3,4]


def Running_sum(nums):
    empty_list = []

    total = 0
    for i in range(len(nums)):
        total += nums[i]
        empty_list.append(total)

    return empty_list

print(Running_sum(nums))




# 9. Palindrome Number

# hint: read the number from left to right or right to left always
# get a same number like nums = 121 , 212
text = input("Enter here :")
def palindrome(text):

    text = text.lower()
    if text == text[::-1]:
        print("Palindrome")
    else:
        print("Not palindrome")

print(palindrome(text))


# 15 3 Sum problem leetcode 


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i != j and i != k and j != k:
                        if nums[i] + nums[j] + nums[k] == 0:
                            triplet = sorted([nums[i], nums[j], nums[k]])

                            if triplet not in result:
                                result.append(triplet)

        return result


# Test the code in VS Code
nums = [-1, 0, 1, 2, -1, -4]

solution = Solution()
print(solution.threeSum(nums))




# Reverse linked list
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

class Linked_list:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

node1 = Linked_list(10)
node2 = Linked_list(20)
node3 = Linked_list(30)
node4 = Linked_list(40)

node1.next = node2
node2.next = node3
node3.next = node4

prev = None
current = node1

while current != None:
    next_node = current.next
    prev 


n1 = node1
while(n1 != None):
    print(n1.data,end=" -> ")
    n1 = n1.next

print("None")