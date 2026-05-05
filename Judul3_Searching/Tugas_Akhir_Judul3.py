def binary_search(data, n, target):
    l = 0
    r = n - 1
    pos = -1
    while l <= r:
        m = l + (r - l) // 2
        print(f"Median: {m}, nilai: {data[m]}")
        if data[m] == target:
            pos = m
            break
        elif data[m] < target:
            print("Mencari ke Halaman Belakang")
            l = m + 1
        else:
            print("Mencari ke Halaman Depan")
            r = m - 1
    return pos

def main():
    data = [12, 15, 28, 32, 56, 98, 110, 125]
    n = len(data)
    print(f"Data nomor: {data}")
    while True:
        try:
            target = int(input("Masukkan nomor yang ingin dicari: "))
            break
        except ValueError:
            print("Input tidak valid, silakan masukkan angka!")
    pos = binary_search(data, n, target)
    if pos < 4:
        print(f"Nomor {data[pos]} ditemukan pada indeks {pos} di Halaman Depan")
    elif pos >= 4:
        print(f"Nomor {data[pos]} ditemukan pada indeks {pos} di Halaman Belakang")  
    else:
        print("Nomor tidak ditemukan")

if __name__ == "__main__":
    main()
