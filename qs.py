def quickSort(arr: list, left: int, right: int):
	if left < right:
		idx = partition(arr, left, right)
		quickSort(arr, left, idx - 1)
		quickSort(arr, idx + 1, right)

def partition(arr: list, left: int, right: int) -> int:
	pivot = arr[right]
	i = left

	for j in range(i + 1, right + 1):
		if arr[j] < pivot:
			swap(arr, i, j)
			i += 1
	swap(arr, i, right)
	return i

'''	pivot = arr[left]

	while left < right:
		print(left, arr[left], pivot)
		while arr[left] < pivot:

			print("hello", left, arr[left], pivot)
			left += 1
		while arr[right] > pivot:
			right -= 1
		swap(arr, left, right)

	return right
'''

def swap(arr: list, idx: int, idx2: int):
	arr[idx], arr[idx2] = arr[idx2], arr[idx]

#arr = [10, 7, 8, 9, 1, 5]
arr = [10, 80, 30, 90, 40, 50, 70]
arr = [10, 3, 12, 7, 2, 11, 9]
quickSort(arr, 0, len(arr) - 1)
print(arr)
