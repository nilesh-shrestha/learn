def selection(arr = []):
    n = len(arr)
    i = 0
    while i < n:
        smallest = i
        for j in range(i+1, n):
            if arr[smallest] > arr[j]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]
    return arr