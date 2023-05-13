import random

# random number 20개 발생
random_numbers = random.sample(range(1,101),20)
print(f"random number: {random_numbers}")

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
