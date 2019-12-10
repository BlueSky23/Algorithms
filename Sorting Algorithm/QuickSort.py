# 不稳定排序
# 时间复杂度：平均情况下，循环log(n)次，每轮循环最多比较n次，复杂度为O(nlog(n))；最坏情况下，循环n次，复杂度为O(n2)。
# 空间复杂度：递归时，空间复杂度为递归深度，O(nlog(n))，非递归时为队列的大小，也为O(nlog(n))
def quickSort(nums, start, end):
    if start >= end:
        return
    idx = partition2(nums, start, end)
    quickSort(nums, start, idx - 1)
    quickSort(nums, idx + 1, end)

    return nums

# 双指针交换法，元素交换完毕后，需要处理与pivot的交换关系
def partition(nums, start, end):
    idx, pivot = start, nums[start]  # 取第一个元素为基准元素
    s, e = start, end
    while s < e:
        # 从左侧找到比pivot大的元素
        while s <= end and nums[s] <= pivot:
            s += 1
        # 从右侧找到比pivot小的元素
        while e >= start and nums[e] >= pivot:
            e -= 1
        if s > end:  # 所有数都比pivot小/等于，将pivot换到最后，结束此轮排序
            nums[start], nums[end] = nums[end], nums[start]
            idx = end
        elif e < start:  # 所有数都比pivot大/等于，保持pivot不变，结束此轮排序
            break
        else:
            if s < e:  # 正常交换，使左边小于pivot，右边大于pivot
                nums[s], nums[e] = nums[e], nums[s]
            if s > e:  # 交换完毕，将pivot与e交换
                nums[e], nums[idx] = nums[idx], nums[e]
                idx = e

    return idx


# 占坑法--间接的双指针交换法，每次交换将pivot移向最终位置，元素交换完成后，无需处理与pivot的交换关系
def partition2(nums, start, end):
    idx, pivot = start, nums[start]
    s, e = start, end
    while s < e:
        # 从右侧找到比pivot小的元素
        while e >= idx and nums[e] >= pivot:
            e -= 1
        if e > idx:
            nums[idx], nums[e] = nums[e], nums[idx]
            s = idx + 1
            idx = e
        # 从左侧找到比pivot大的元素
        while s <= idx and nums[s] <= pivot:
            s += 1
        if s < idx:
            nums[idx], nums[s] = nums[s], nums[idx]
            e = idx - 1
            idx = s

    return idx


# 非递归实现：递归过程中主要是利用数组待排序部分的起止索引，可以放到队列中实现非递归
def quickSort2(nums, start, end):
    stack = [(start, end)]
    while stack:
        s, e = stack.pop(0)
        idx = partition(nums, s, e)
        if idx > s:
            stack.append((s, idx - 1))
        if idx < e:
            stack.append((idx + 1, e))
    return nums


nums1 = [-1, 4, 2, 45, -3, -3, 10]
nums2 = [1, 2, 3, 4, 5]
print(quickSort2(nums1, 0, len(nums1) - 1))
print(quickSort2(nums2, 0, len(nums2) - 1))
