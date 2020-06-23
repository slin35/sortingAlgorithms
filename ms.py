def mergeSort(arr: list):
	if len(arr) > 1:
		m = len(arr) // 2
		left = arr[:m]
		right = arr[m:]
		mergeSort(left)
		mergeSort(right)
		merge(arr, left, right)


def merge(arr: list, left: list, right: list):
	i = 0
	j = 0
	k = 0

	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			arr[k] = left[i]
			i += 1
		else:
			arr[k] = right[j]
			j += 1
		k += 1

	while i < len(left):
		arr[k] = left[i]
		i += 1
		k += 1

	while j < len(right):
		arr[k] = right[j]
		j += 1
		k += 1


arr = [10, 80, 30, 90, 40, 50, 70]
mergeSort(arr)
print(arr)