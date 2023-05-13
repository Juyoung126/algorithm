# 문제 3 Bubble, Insertion, Selection, Merge

import random
# 1~100 사이 random number 20개 발생
random_numbers = []
random_numbers = random.sample(range(1,101),20)
print(f"random number: {random_numbers}")


# buuble Sort
# 데이터 훼손을 방지하기 위해 random_number를 random_numbers_bubble로 복제하여 실행
random_numbers_bubble = random_numbers
def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        # 리스트를 순회하며 인접한 두 원소를 비교하여 큰 값이 오른쪽에 오도록 위치 교환
        for j in range(n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers
# 정렬된 결과 출력
sorted_bubble_numbers = bubble_sort(random_numbers_bubble)
print(f"버블  정렬: {sorted_bubble_numbers}")

# insertion Sort
# 데이터 훼손을 방지하기 위해 random_number를 random_numbers_insertion로 복제하여 실행
random_numbers_insertion= random_numbers
def insertion_sort(numbers):
    n = len(numbers)
    for i in range(1, n):
        # key값(삽입할 값)을 설정
        key = numbers[i]
        j = i - 1
        # key값보다 큰 값을 찾으면 그 값을 우측으로 한 칸씩 이동시키면서 key값 삽입
        while j >= 0 and numbers[j] > key:
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = key
    return numbers
# 정렬된 결과 출력
sorted_insertion_numbers = insertion_sort(random_numbers_insertion)
print(f"삽입 정렬: {sorted_insertion_numbers}")


# selection Sort
# 데이터 훼손을 방지하기 위해 random_number를 random_numbers_selection로 복제하여 실행
random_numbers_selection= random_numbers
def selection_sort(numbers):
    n = len(numbers)
    for i in range(n):
        # i번째 이후의 가장 작은 값을 찾아 i번째 값과 교환
        min_index = i
        for j in range(i+1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers
# 정렬된 결과 출력
sorted_selection_numbers = selection_sort(random_numbers_selection)
print(f"선택 정렬: {sorted_selection_numbers}")


# merge Sort
# 데이터 훼손을 방지하기 위해 random_number를 random_numbers_merge로 복제하여 실행
random_numbers_merge = random_numbers
def merge_sort(numbers):
    # 재귀 종료 조건
    if len(numbers) <= 1:
        return numbers
    
    # 리스트를 절반으로 분할
    mid = len(numbers) // 2
    left_half = numbers[:mid]
    right_half = numbers[mid:]
    
    # 분할된 리스트에 대해 재귀적으로 병합 정렬 수행
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # 병합된 결과 반환
    sorted_numbers = []
    i = j = 0
    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] < right_sorted[j]:
            sorted_numbers.append(left_sorted[i])
            i += 1
        else:
            sorted_numbers.append(right_sorted[j])
            j += 1
    sorted_numbers += left_sorted[i:]
    sorted_numbers += right_sorted[j:]
    return sorted_numbers

# 정렬된 결과 출력
sorted_merge_numbers = selection_sort(random_numbers_merge)
print(f"선택 정렬: {sorted_merge_numbers}")