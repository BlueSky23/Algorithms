# 不稳定排序
# 时间复杂度：通过选择合适的增量，可以使时间复杂度降到O(n3/2)或O(n4/3)
# 空间复杂度：O(1)
# 注：即跨步的插入排序，最坏情况下，如果每次增量排序都不能改变整个序列的顺序，则只会徒增跨步操作

def shellSort(nums):
    d = len(nums)
    while d > 1:
        # 更新增量，直至1
        d = d // 2
        for i in range(0, d):
            # 基于增量，设置初始步范围
            for j in range(i + d, len(nums), d):
                # 在增量范围内执行插入排序操作
                k = j
                while k > i and nums[k] < nums[k - d]:
                    nums[k], nums[k - d] = nums[k - d], nums[k]
                    k -= d
    return nums


nums1 = [-1, 4, 2, 45, -3, -3, 10]
nums2 = [1, 3, 2, 3, 4, 5]
print(shellSort(nums1))
print(shellSort(nums2))