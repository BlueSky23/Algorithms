# 不稳定排序
# 时间复杂度：都要执行两次循环，最好、最坏和平均都是O(n2)
# 空间复杂度: O(1)

def selectSort(nums):

    for i in range(len(nums), 0, -1):
        # 每一轮循环找到最大值，并与未排序数组的最后一个交换
        max_idx = 0
        for j in range(i):
            if nums[j] > nums[max_idx]:
                max_idx = j
        nums[max_idx], nums[i - 1] = nums[i - 1], nums[max_idx]
    return nums

nums1 = [-1, 4, 2, 45, -3, -3, 10]
nums2 = [1, 2, 3, 4, 5]
print(selectSort(nums1))
print(selectSort(nums2))
