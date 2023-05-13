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

#문제 2 Heap 구성 및 Sorting
#데이터 훼손을 방지하기 위해 random_number를 random_numbers_heap로 복제하여 실행
random_numbers_heap = random_numbers

def heapify(arr, n, i):
    smallest = i  # 현재 노드가 최소값을 가진다고 가정
    left = 2 * i + 1  # 왼쪽 자식 노드 인덱스
    right = 2 * i + 2 # 오른쪽 자식 노드 인덱스
 
    # 왼쪽 자식이 현재 노드보다 작으면 왼쪽 자식을 최소값으로 선택
    if left < n and arr[left] < arr[smallest]:
        smallest = left

    # 오른쪽 자식이 현재 노드보다 작으면 오른쪽 자식을 최소값으로 선택
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    # 현재 노드가 최소값을 가지지 않으면 노드 교환
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

def build_heap(arr):
    n = len(arr)
    # 마지막 노드의 부모 노드부터 heapify 수행
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        
def heap_sort(arr):
    build_heap(arr)
    print("Heap 구성 결과:", arr) # 힙 구성 결과 출력
    
    # heapify를 수행하면 가장 큰 값이 맨 앞으로 오므로 하나씩 제거하면서 정렬 수행
    for i in range(len(arr)-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # 맨 끝 값과 가장 큰 값의 자리를 변경
        heapify(arr, i, 0) # 변경된 리스트에서 heapify 수행
    print("Heap 정렬 결과:", arr) # 힙 정렬 결과 출력

heap_sort(random_numbers_heap)

# 문제 3 Bubble, Insertion, Selection, Merge

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

# 4. 이진트리 생성, 검색, 삭제
## 이진 트리 노드 클래스 생성
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# 이진 트리 삽입 함수 생성
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

# 이진 트리 탐색 함수 생성
def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)

# 이진 트리 삭제 함수 생성
def delete(root, key):
    if root is None:
        return root
    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        # 삭제할 노드의 자식이 없거나, 하나만 있을 경우
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        # 삭제할 노드의 자식이 둘인 경우
        temp = find_min(root.right)
        root.val = temp.val
        root.right = delete(root.right, temp.val)
    return root

# 오른쪽 자식 노드 중 가장 작은 값을 반환하는 함수
def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# 이진 트리 중위 순회 함수 생성
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)
# 이진 트리 생성
root = None
for num in random_numbers:
    root = insert(root, num)

# 이진 트리 탐색
while True:
    target_s = int(input("검색할 값을 입력하세요(검색을 종료하려면 -1을 입력하세요.): "))
    if target_s == -1:
        break
    result = search(root, target_s)
    if result is not None:
        print(f"{target_s}은(는) 존재합니다.")
    else:
        print(f"{target_s}은(는) 존재하지 않습니다.")

# 이진 트리 삭제
while True:
    target_d = int(input("삭제할 값을 입력하세요(삭제를 종료하려면 -1을 입력하세요.): "))
    if target_d == -1:
        break
    root = delete(root, target_d)
    if root is not None:
        print(f"{target_d}이(가) 삭제되었습니다.")
        print("현재 이진 트리의 상태: ", end="")
        inorder_traversal(root)
        print()
    else:
        print(f"{target_d}을(를) 삭제할 수 없습니다.")