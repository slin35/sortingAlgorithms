
def quickSort(arr: list, left: int, right: int):
	if left < right:
		idx = partition(arr, left, right)
		quickSort(arr, left, idx)
		quickSort(arr, idx + 1, right)


def partition(arr: list, left: int, right: int) -> int:
	pivot = (left + right) // 2
	i = left
	j = right
	while True:
		while arr[i] < arr[pivot]:
			i += 1
		while arr[j] > arr[pivot]:
			j -= 1
		if i >= j:
			return j

		swap(arr, i, j)

		i += 1
		j -= 1


def swap(arr: list, idx: int, idx2: int):
	arr[idx], arr[idx2] = arr[idx2], arr[idx]


arr = [10, 7, 8, 9, 1, 5]
arr = [10, 80, 30, 90, 40, 50, 70]
quickSort(arr, 0, len(arr) - 1)
print(arr)

