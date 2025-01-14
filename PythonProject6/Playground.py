from operator import index


def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    # arr 1 -  [1,2,3,0,0,0]
    # arr 2 - [2,5,6]
    index_one = m - 1
    index_two = n - 1
    insert_pos = m + n - 1
    while index_two > -1:
        if index_one >= 0 and nums1[index_one] > nums2[index_two]:
            nums1[insert_pos] = nums1[index_one]
            index_one -= 1
        else:
            nums1[insert_pos] = nums2[index_two]
            index_two -= 1
        insert_pos -= 1

arr1 = [1,2,3,0,0,0]
arr2 = [2,5,6]
merge(arr1,3,arr2,3)



def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    index_start = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index_start] = nums[i]
            index_start += 1
    return index_start

nums = [3,2,2,3]




def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    index_start = 0
    duplicates = set()
    for i in range(len(nums)):
        if nums[i] not in duplicates:
            duplicates.add(nums[i])
            nums[index_start] = nums[i]
            index_start += 1
    return index_start


def removeDuplicatesTwo(self, nums):
    index_start = 0
    count_map = {}

    for num in nums:
        if num not in count_map:
            count_map[num] = 1
            nums[index_start] = num
            index_start += 1
        elif count_map[num] == 1:
            count_map[num] += 1
            nums[index_start] = num
            index_start += 1

    return index_start

def majorityElement(self, nums):
    candidate = None
    times = 0
    for num in nums:
        if times == 0:
            candidate = num
            times = 1
        elif num == candidate:
            times += 1
        else:
            times -= 1

    return candidate

def rotate(nums, k):
    n = len(nums)
    k = k % n
    nums[:] = nums[-k:] + nums[:-k]

#prices = [7,1,5,3,6,4] buy on day 2 sell on day 5 best profit.
#prices = [7,6,4,3,1] can't have any profit.


def maxProfit(self, prices):
    current_profit = 0
    min_price = prices[0]

    for num in prices:
        if prices[num] < min_price:
            min_price = prices[num]
        profit = num - min_price
        if profit > current_profit:
            current_profit = profit
    return current_profit
# harder
def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    sum_profit = 0
    for i in range(1,len(prices)):
        if prices[i] > prices[i-1]:
            sum_profit += prices[i] - prices[i-1]
    return sum_profit

def canJump(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    max_reach = 0
    for i in range(0, len(nums)-1):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])
        if max_reach > len(nums)-1:
            return True
    return False

arr = [1,2,3,4,5]
print(len(arr))
