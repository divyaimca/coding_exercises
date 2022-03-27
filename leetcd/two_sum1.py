from typing import List
import time

def twoSumOn2(nums: List[int], target: int) -> List[int]:
        
        res = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    if sorted([i,j]) not in res and i !=j :
                        res.append([i,j])
                    #print(f"Sum of {nums[i]} and {nums[j]} is {target}, i position {i}, j position {j}")

        for a in res: return a

def twoSumOn(nums: List[int], target: int) -> List[int]:
        
        res = []
        for i in range(len(nums)):
            value = target - nums[i]
            if value in nums:
                j = nums.index(value)
                if sorted([i,j]) not in res and i !=j :
                    res.append([i,j])
                #print(f"Sum of {nums[i]} and {nums[j]} is {target}, i position {i}, j position {j}")

        for a in res: return a

def twoSumOn1(nums: List[int], target: int) -> List[int]:
        
        dict = {}
        for i,value in enumerate(nums):
            if target - value in dict:
                return [dict[target - value], i]
            else:
                dict[value] = i





#print(twoSum([2,5,5,11],10))


list1 = list(range(10001))
sum1 = 19999


now = time.time()
print(twoSumOn2(list1,sum1))
print(f'Time taken by twoSumOn2 {(time.time() - now):5f} seconds ')


now = time.time()
print(twoSumOn(list1,sum1))
print(f'Time taken by twoSumOn {(time.time() - now):5f} seconds')


now = time.time()
print(twoSumOn1(list1,sum1))
print(f'Time taken by twoSumOn1 {(time.time() - now):5f} seconds')