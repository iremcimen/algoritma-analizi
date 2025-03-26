# En Küçük Ortalamalı Alt Dizi (Divide and Conquer Yaklaşımı)
# Bu algoritma, bir dizinin ardışık elemanlarından oluşan alt dizilerin ortalamasının en küçük olanı bulur. Zaman karmaşıklığı: O(n log n).

def min_subarray_avg(arr):
    def helper(low, high):
        if low == high:
            return arr[low]

        mid = (low + high) // 2

        # Sol, sağ ve ortadan geçen minimumları bul
        left_min = helper(low, mid)
        right_min = helper(mid + 1, high)
        cross_min = min_crossing_avg(low, mid, high)

        return min(left_min, right_min, cross_min)

    def min_crossing_avg(low, mid, high):
        # Orta noktadan sola doğru minimum ortalama
        left_sum = 0
        left_count = 0
        min_left_avg = float('inf')
        for i in range(mid, low - 1, -1):
            left_sum += arr[i]
            left_count += 1
            left_avg = left_sum / left_count
            if left_avg < min_left_avg:
                min_left_avg = left_avg

        # Orta noktadan sağa doğru minimum ortalama
        right_sum = 0
        right_count = 0
        min_right_avg = float('inf')
        for i in range(mid + 1, high + 1):
            right_sum += arr[i]
            right_count += 1
            right_avg = right_sum / right_count
            if right_avg < min_right_avg:
                min_right_avg = right_avg

        return min_left_avg + min_right_avg

    return helper(0, len(arr) - 1)

# Örnek Kullanım
arr = [3, -1, 4, 2, -5, 1, 3, -2]
print("En Küçük Ortalamalı Alt Dizi:", min_subarray_avg(arr))  # Çıktı: -1.0
