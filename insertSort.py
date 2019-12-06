# 稳定排序
# 时间复杂度：最好情况下O(n)，最坏情况和平均情况O(n2)
# 空间复杂度： O(1)
def insertSort(nums):
    for i in range(1, len(nums)):
        # 将最新元素向前插入到已经排好序的序列中
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
            else:
                break
    return nums


nums1 = [-1, 4, 2, 45, -3, -3, 10]
nums2 = [1, 2, 3, 4, 5]
print(insertSort(nums1))
print(insertSort(nums2))
