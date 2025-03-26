def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Değişim olup olmadığını kontrol et
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:  # Büyükten küçüğe sıralama için yönü değiştirdik
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap işlemi
                swapped = True
        if not swapped:  # Eğer hiç değişim olmadıysa, liste zaten sıralıdır
            break
    return arr

# Örnek kullanım
arr = [5, 3, 8, 1, 2]
sorted_arr = bubble_sort(arr)
print("Büyükten küçüğe sıralı liste:", sorted_arr)
