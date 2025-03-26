# Üs Hesaplama (Exponentiation by Squaring)
# Bu algoritma, üssü hızlı bir şekilde hesaplamak için üs alma işlemini kareler yoluyla yapar. Zaman karmaşıklığı: O(log n).

def power(a, b):
    result = 1
    while b > 0:
        if b % 2 == 1:  # Eğer b tekse, sonucu base ile çarp
            result *= a
        a *= a  # Tabanı karesini al
        b //= 2  # Üssü yarıya indir

    return result


# Örnek Kullanım
a = 2
b = 5
print(power(a, b))  # Çıktı: 32
