def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] == arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            if not swapped:
                break






# Bu Bubble sort tartiblash tuzulmasi hisoblanadi. u eng oddiy tartiblash tuzulmasidir yani ketmaket tartiblab bora veradi  