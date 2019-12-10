# 稳定排序
# 时间复杂度：都要执行两次循环，最好、最坏和平均都是O(n2)
# 空间复杂度：O(1)

def bubbleSort(nums):
    for i in range(len(nums) - 1, -1, -1):
        # 从前向后比较，每一次循环都会将未排序数组中的最大值移动到最后
        for j in range(0, i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


# 改进：在最好的情况下，时间复杂度可以降到O(n)
def bubbleSort2(nums):
    for i in range(len(nums) - 1, -1, -1):
        # 从前向后比较，每一次循环都会将未排序数组中的最大值移动到最后
        flag = False  # 标志该次循环是否有交换
        for j in range(0, i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = True
        if not flag:
            break

    return nums


nums1 = [-1, 4, 2, 45, -3, -3, 10]
nums2 = [1, 2, 3, 4, 5]
print(bubbleSort2(nums1))
print(bubbleSort2(nums2))