def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]  # Eklenmesi gereken eleman
        j = i - 1

        # Diziyi sola kaydırarak uygun konumu bul
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current  # Elemanı doğru yere yerleştir
    return arr

# Örnek kullanım
nums = [29, 10, 14, 37, 13]
sorted_nums = insertion_sort(nums)
print("Sıralı liste:", sorted_nums)
