'''
TWO SUM
    



Problem:
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

 

 Example 1:
 Input: nums = [2,7,11,15], target = 9
 Output: [0,1]
 Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

 Example 2:
 Input: nums = [3,2,4], target = 6
 Output: [1,2]

 Example 3:
 Input: nums = [3,3], target = 6
 Output: [0,1]
  

  Constraints:

  2 <= nums.length <= 104
  -109 <= nums[i] <= 109
  -109 <= target <= 109
  Only one valid answer exists.
   

   Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


'''


nums = [5,2,7,11,15]
target = 9


def twoSum(nums, target):
#	#BRUTE FORCE
#   #   double for loop
#	for i in range(len(nums)):
#		print("i: ", i)
#		for j in range(len(nums)):
#			print("j: ", j)
#			if nums[i] + nums[j] == target:
#				return [i,j] #returning solution
#
#	return [] #no solution found


    #OPTIMIZATION
	#   hash map
    map={}
    for i in range(len(nums)):
        if target - nums[i] in map:
            return [map[target-nums[i]], i]   #map[target-nums[i]] ; index of value, i; index of current num
        map[nums[i]] = i
    return []




print("map: ", map)
ind=twoSum(nums, target) #returns indecies of vals
print("nums: ", nums)
print("vals: ", vals)
print(nums[ind[0]], nums[ind[1]])
print("target: ", target)


