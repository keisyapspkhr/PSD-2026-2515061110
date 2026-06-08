class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next
        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node
        return True

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current
            current = current.next
        return None

    def display(self):
        print("\n" + "="*50)
        print("        --- Daftar Buku di Perpustakaan ---")
        print("="*50)
        for i in range(self.SIZE):
            print(f"Rak {i}: ", end="")
            current = self.table[i]
            if current is None:
                print("Kosong")
            else:
                while current is not None:
                    print(f"({current.key},{current.value}) -> ", end="")
                    if current.next is not None:
                        print("", end="")
                    current = current.next
            print("NULL")
        print("="*50)

def main():
    hashmap = HashMapSeparateChaining()
    pilih = 0

    hashmap.insert(1, "Batozar")
    hashmap.insert(11, "Laskar Pelangi")
    hashmap.insert(21, "Bumi")
    hashmap.insert(2, "Komet Minor")
    
    while pilih != 4:
        print()
        print("="*40)
        print("       ---Sistem Perpustakaan---")
        print("="*40)
        print("1. Tampilkan Seluruh Data Buku")
        print("2. Menambahkan Buku Baru")
        print("3. Mencari Buku")
        print("4. Keluar")
        print("="*40)
        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid!")
            print("Silahkan Masukkan ANGKA 1-4!")
            continue
        
        if pilih == 1:
            hashmap.display()
        elif pilih == 2:
            try:
                print("\n---Tambah Buku Baru---")
                kode = int(input("Masukkan Kode Buku: "))
                judul = input("Masukkan Judul Buku: ").strip()
                hashmap.insert(kode, judul)
                print(f"Buku dengan kode {kode} - \"{judul}\" berhasil ditambahkan!")
            except ValueError:
                print("Input tidak valid!")
                print("Kode Buku Harus Berupa ANGKA.")
        elif pilih == 3:
            try:
                print("\n--- Cari Buku ---")
                cari = int(input("Masukkan Kode Buku yang Dicari: "))
                hasil = hashmap.search(cari)
                if hasil:
                    print(f"\nData ditemukan!")
                    print(f"Kode Buku: [{hasil.key}]")
                    print(f"Judul Buku: \"{hasil.value}\"")
                else:
                    print("Data buku tidak ditemukan!")
            except ValueError:
                print("Input tidak valid!")
                print("Kode Buku Harus berupa ANGKA.")
        elif pilih == 4:
            print("Program selesai. Terima kasih!")
            print()
        else:
            print("Pilihan tidak valid!")
            print("Masukkan ANGKA 1-4.")

if __name__ == "__main__":
    main()    
