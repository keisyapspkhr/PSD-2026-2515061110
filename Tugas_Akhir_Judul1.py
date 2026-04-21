def menu():
    print("1. Tampilkan Jumlah Kuota Mahasiswa")
    print("2. Tampilkan Semua Nilai Mahasiswa")
    print("3. Input Nilai Mahasiswa & Menghitung Rata-Rata")
    print("4. Keluar")

def main():
    n = int(input("Kuota nilai mahasiwa = "))
    nilai = [0] * n
    running = True
    while running:
        menu()
        try:
            choice = int(input("Pilihan (1-4): "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if choice == 1:
            print(f"Jumlah Kuota Mahasiswa adalah {len(nilai)} orang")

        elif choice == 2:
            print("Daftar nilai mahasiswa saat ini")
            for i in range(len(nilai)):
                print (f"Mahasiswa ke-{i+1}: {nilai[i]}")

        elif choice == 3:
            total = 0
            print("Masukkan nilai mahasiswa:")
            for i in range(len(nilai)):
                while True:
                    try:
                        skor = float(input(f"Nilai mahasiswa ke-{i+1} = "))
                        if 0 <= skor <= 100:
                            nilai[i] = skor
                            total += skor
                        else:
                            print("Nilai tidak valid!")
                            continue
                        break
                    except ValueError:
                        print("Input tidak valid, silakan masukkan angka 0-100!")

            rata_rata = total/len(nilai)
            print(f"Total nilai mahasiswa = {total}")
            print(f"Rata-Rata nilai mahasiswa = {rata_rata}")

        elif choice == 4:
            running = False
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()