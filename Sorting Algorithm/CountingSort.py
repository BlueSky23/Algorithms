# 稳定排序
# 时间复杂度：O(n+k)，n为待排序数组大小，k为数组元素的取值范围
# 空间复杂度：中间数组和目标数组，O(n+k)
# 注：只适用于在一定范围内取值的整数序列
def countingSort(nums):
    # 确定中间数组大小
    min, max = nums[0], nums[0]
    for i in range(len(nums)):
        if nums[i] < min:
            min = nums[i]
        elif nums[i] > max:
            max = nums[i]
    mid_array = [0] * (max - min + 1)
    # 转存到计数数组
    for i in range(len(nums)):
        mid_array[nums[i] - min] += 1
    # 为确保稳定性，统计小于等于当前元素的元素个数
    for i in range(1, len(mid_array)):
        mid_array[i] += mid_array[i - 1]
    # 逆序遍历原始数组，根据mid_array保存的小于等于元素个数将结果保存到目标数组
    result_array = [0] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        result_array[mid_array[nums[i] - min] - 1] = nums[i]
        mid_array[nums[i] - min] -= 1

    return result_array


# 最后改为从前向后遍历原始数组
def countingSort2(nums):
    # 确定中间数组大小
    min, max = nums[0], nums[0]
    for i in range(len(nums)):
        if nums[i] < min:
            min = nums[i]
        elif nums[i] > max:
            max = nums[i]
    mid_array = [0] * (max - min + 1)
    # 转存到计数数组
    for i in range(len(nums)):
        mid_array[nums[i] - min] += 1
    # 为确保稳定性，统计大于等于当前元素的元素个数
    for i in range(len(mid_array) - 2, -1, -1):
        mid_array[i] += mid_array[i + 1]
    # 顺序遍历原始数组，根据mid_array保存的小于等于元素个数将结果保存到目标数组
    result_array = [0] * len(nums)
    for i in range(len(nums)):
        result_array[len(nums)-mid_array[nums[i] - min]] = nums[i]
        mid_array[nums[i] - min] -= 1

    return result_array


nums1 = [85, 81, 79, 87, 90, 73]
nums2 = [-3, 6, 3, 0, -6]
print(countingSort2(nums1))
print(countingSort2(nums2))