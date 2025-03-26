# En Küçük Alt Dizi Toplamı (Kadane's Algorithm)
# Bu algoritma, bir dizinin ardışık elemanlarından oluşan alt dizilerin toplamı en küçük olanı bulur. Zaman karmaşıklığı: O(n).

def min_subarray(nums):
    min_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = min(nums[i], current_sum + nums[i])
        min_sum = min(min_sum, current_sum)

    return min_sum


# Örnek Kullanım
nums = [3, -1, 4, 2, -5, 1, 3, -2]
print(min_subarray(nums))  # Çıktı: -5
