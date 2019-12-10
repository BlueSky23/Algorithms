# 稳定排序
# 时间复杂度：最坏情况下O(nlog(n))
# 空间复杂度： O(n)

def mergeSort(nums):
    if len(nums) < 2:
        return nums
    mid = (len(nums)-1) // 2
    # 左半部分排序
    left = mergeSort(nums[:mid + 1])
    # 右半部分排序
    right = mergeSort(nums[mid + 1:])
    # 合并已排好序的两部分
    temp = merge(left, right)
    return temp

# 合并
def merge(left, right):
    temp = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1

    if i < len(left):
        temp.extend(left[i:])
    if j < len(right):
        temp.extend(right[j:])

    return temp


nums1 = [-1, 4, 2, 45, -3, -3, 10]
nums2 = [1, 2, 3, 4, 5]
print(mergeSort(nums1))
print(mergeSort(nums2))
