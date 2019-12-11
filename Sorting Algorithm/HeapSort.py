# 不稳定排序
# 时间复杂度：O(nlog(n))
# 空间复杂度：O(1)
# 注：构建最大堆时，需从下至上；交换根节点和子节点时，只交换一次，否则两个子树都要重新heapify
def heapSort(nums):
    # 构建最大堆
    maxHeap(nums)
    # 依次将最大值nums[0]交换至未排序数组的最后，并重新维护最大堆性质
    for i in range(len(nums) - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, 0, i)
    return nums


def maxHeap(nums):
    # 作为父节点的最大索引值
    idx = (len(nums) - 2) // 2
    #  从下至上heapify每个父节点
    for i in range(idx, -1, -1):
        heapify(nums, i, len(nums))


# 维持最大堆的性质，这里用size参数，因为随着最大值的弹出，待排序的数组元素会变少
def heapify(nums, i, size):
    # 考虑有两个子节点的情况
    while 2 * i + 2 < size:
        temp = i
        # 获取较大值节点的索引值
        larger = 2 * i + 1 if nums[2 * i + 1] > nums[2 * i + 2] else 2 * i + 2
        # 交换
        if nums[i] < nums[larger]:
            nums[i], nums[larger] = nums[larger], nums[i]
            temp = larger
        # 当前节点值比左、右都大，没有发生交换
        if temp == i:
            return
        # 更新当前节点索引
        i = temp

    # 考虑只有左子节点的情况
    if 2 * i + 1 < size:
        if nums[i] < nums[2 * i + 1]:
            nums[i], nums[2 * i + 1] = nums[2 * i + 1], nums[i]


nums1 = [85, 81, 79, 87, 90, 73]
nums2 = [-3, 6, 3, 0, -6]
print(heapSort(nums1))
print(heapSort(nums2))
