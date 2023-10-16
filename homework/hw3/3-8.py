# 随机生成多组长度递增的随机数列，使用不同的排序算法（如选择排序和归并排序）对这些数列的数据排序，
# 请分析不同排序算法在不同长度数列下的运行效果

import random
import time

# 选择排序
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[i] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# 归并排序
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result

# 主函数
if __name__ == "__main__":
    lengths = [1000, 2000, 4000, 8000, 16000]  # 数列的长度

    for length in lengths:
        arr = [random.randint(1, 100000) for _ in range(length)]
        print(f"Sorting array of length: {length}")

        # 选择排序
        start_time = time.time()
        selection_sort(arr.copy())
        print(f"Selection sort took {time.time() - start_time:.5f} seconds.")

        # 归并排序
        start_time = time.time()
        merge_sort(arr.copy())
        print(f"Merge sort took {time.time() - start_time:.5f} seconds.")