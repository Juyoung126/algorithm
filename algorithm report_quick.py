import random
# 1~100 사이 random number 20개 발생
random_numbers = []
random_numbers = random.sample(range(1,101),20)
print(f"random number: {random_numbers}")

#문제 1. Quick Sort 구현

def quick_sort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q - 1)
        quick_sort(arr, q + 1, r)
    return arr
def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i + 1

sorted_quick_numbers = quick_sort(random_numbers, 0, len(random_numbers) - 1)

print(f"퀵 정렬: {sorted_quick_numbers}")

