# 합병 정렬(Merge sort)

### 요약

- 분할 정복 알고리즘의 하나이다

- 안정 정렬에 속한다

  - | Name       | Space Complexity | Best  | Avg   | Worst |
    | ---------- | ---------------- | ----- | ----- | ----- |
    | Merge sort | O(n)             | nlogn | nlogn | nlogn |

    

- 분할 정복(divide and conquer) 방법

  - 문제를 작은 2개의 문제로 분리하고 각각을 해결한 다음 결과를 모아서 원래의 문제를 해결하는 전략
  - 재귀적 호출을 이용해 구현

### 구체적 개념

- 분할(Divide) : 입력 배열을 같은 크기의 2개의 부분 배열로 분할
- 정복(Conquer) : 최소 크기가 아니라면 재귀 호출을 이용해 다시 분할정복하며, 최소 크기라면 부분배열을 정렬한다.
- 결합(Combine) : 정렬된 부분 배열을 하나의 배열에 합병한다

### 소스코드

```python
def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list)//2
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = merge_sort(leftlist)
    rightlist = merge_sort(rightlist)
    return merge(leftList, rightList)

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) >0:
        if len(left)>0 and len(right)>0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left)>0:
            result.append(left[0])
            left=left[1:]
        elif len(right)>0:
            result.append(right[0])
            right = right[1:]
    return result
```

