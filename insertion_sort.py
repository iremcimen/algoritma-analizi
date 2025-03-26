def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Eklenmek istenen eleman
        j = i - 1

        # Key'den küçük elemanları sağa kaydır (büyükten küçüğe sıralama)
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Key'i doğru konuma yerleştir
    return arr

# Örnek kullanım
arr = [42, 17, 8, 99, 23]
sorted_arr = insertion_sort(arr)
print("Büyükten küçüğe sıralı liste:", sorted_arr)
