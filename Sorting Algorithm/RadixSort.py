# 稳定排序，因为中间的每一次计数排序都是稳定的
# 时间复杂度：没有比较操作，最好、最坏和平均都是O(k*(n+m))，k为元素的长度，n为待排序数组的大小，m为计数部分的取值范围
# 空间复杂度：O(n+m)
def radixSort(nums):  # 待排序元素只由数字构成
    # 假设所有元素长度一样，如不一样，可以适当在前或后补全
    len_e = len(nums[0])
    for i in range(len_e - 1, -1, -1):
        stat_array = [0] * 10
        # 计数
        for j in range(len(nums)):
            idx = int(nums[j][i])
            stat_array[idx] += 1
        # 确保稳定性，计算小于等于当前元素的元素个数
        for k in range(1, 10):
            stat_array[k] += stat_array[k - 1]
        # 逆序遍历原数组，获取当前轮次稳定的排序结果
        sort_array = [0] * len(nums)
        for m in range(len(nums) - 1, -1, -1):
            idx = int(nums[m][i])
            sort_array[stat_array[idx] - 1] = nums[m]
            stat_array[idx] -= 1
        # 保留当前排序结果，进行一下轮
        nums = sort_array

    return nums


def radixSort2(nums):  # 待排序元素只由小写字母构成
    # 假设所有元素长度一样，如不一样，可以适当在前或后补全
    len_e = len(nums[0])
    for i in range(len_e - 1, -1, -1):
        stat_array = [0] * 26
        # 计数
        for j in range(len(nums)):
            idx = ord(nums[j][i]) - 97
            stat_array[idx] += 1
        # 确保稳定性，计算小于等于当前元素的元素个数
        for k in range(1, 26):
            stat_array[k] += stat_array[k - 1]
        # 逆序遍历原数组，获取当前轮次稳定的排序结果
        sort_array = [0] * len(nums)
        for m in range(len(nums) - 1, -1, -1):
            idx = ord(nums[m][i]) - 97
            sort_array[stat_array[idx] - 1] = nums[m]
            stat_array[idx] -= 1
        # 保留当前排序结果，进行一下轮
        nums = sort_array

    return nums


nums = [1358976, 2387465, 6452187, 9623748, 1263748]
nums = [str(i) for i in nums]
print(radixSort(nums))

nums = ['abdedg', 'edfawd', 'abdwhr', 'opkslf']
print(radixSort2(nums))
