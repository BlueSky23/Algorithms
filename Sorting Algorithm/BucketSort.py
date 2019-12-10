# 稳定性，取决于为每个桶进行排序时选择的排序算法
# 时间复杂度，也依赖每个桶进行排序的排序算法，O(n+m*f)，其中n为数组大小，m为桶的个数，f为选择的排序算法的时间复杂度
# 空间复杂度，m*s，m为桶的个数，s为桶的大小。
# 注：最坏情况下，桶排序退化为比较排序，最好情况下，变为计数排序
def bucketSort(nums):
    # 确定桶的个数，应该依据待排序数组元素的分布情况，这里简单设为同元素个数
    buckets = [[] for i in range(len(nums))]
    # 计算最大和最小值，用以计算桶的取值区间
    min, max = nums[0], nums[0]
    for i in range(1, len(nums)):
        if nums[i] < min:
            min = nums[i]
        if nums[i] > max:
            max = nums[i]
    # 计算取值区间
    interval = (max - min) / len(buckets)
    # 将待排序数组元素分配到桶中
    for i in range(len(nums)):
        idx = int((nums[i] - min) // interval)
        buckets[idx].append(nums[i])
    # 为每个桶进行排序
    for bucket in buckets:
        bucket.sort()
    # 按序取出桶中元素，即为最终排序结果
    sort_array = []
    for bucket in buckets:
        for item in bucket:
            sort_array.append(item)

    return sort_array


nums = [4.5, 0.84, 3.25, 2.18, 0.5]
print(bucketSort(nums))