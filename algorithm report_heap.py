#문제 2 Heap 구성 및 Sorting
import random
# 1~100 사이 random number 20개 발생
random_numbers = []
random_numbers = random.sample(range(1,101),20)
print(f"random number: {random_numbers}")

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
