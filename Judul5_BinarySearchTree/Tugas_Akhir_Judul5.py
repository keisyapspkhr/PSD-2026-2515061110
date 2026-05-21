class Node:
    def __init__(self, key, nama):
        self.key = key
        self.nama = nama
        self.left = None
        self.right = None

class SistemSkor:
    def __init__(self):
        self.root = None

    def insert_node(self, root, key, nama):
        if root is None:
            return Node(key, nama)
        if key < root.key:
            root.left = self.insert_node(root.left, key, nama)
        elif key > root.key:
            root.right = self.insert_node(root.right, key, nama)
        return root

    def insert(self, key, nama):
        self.root = self.insert_node(self.root, key, nama)

    def find_min_node(self, root):
        current = root
        while current is not None and current.left is not None:
            current = current.left
        return current
    
    def find_score(self, root, key):
        if root is None:
            return None
        if key == root.key:
            return root
        elif key < root.key:
            return self.find_score(root.left, key)
        else:
            return self.find_score(root.right, key)

    def delete_node(self, root, key):
        if root is None:
            return None
        if key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                successor = self.find_min_node(root.right)
                root.key = successor.key
                root.nama = successor.nama
                root.right = self.delete_node(root.right, successor.key)
        return root

    def delete(self, key):
        node = self.find_score(self.root, key)
        if node is None:
            print(f"Skor {key} tidak ditemukan!")
            return
        nama = node.nama
        self.root = self.delete_node(self.root, key)
        print(f"Skor {key} dari Pemain {nama} berhasil dihapus.")

    def descending(self, root, result):
        if root is None:
            return
        self.descending(root.right, result)
        result.append((root.key, root.nama))
        self.descending(root.left, result)

    def tampilkan_juara(self):
        if self.root is None:
            print("Belum ada data skor.")
            return
        daftar = []
        self.descending(self.root, daftar)
        print("\n=== Daftar Juara ===")
        for i, (key, nama) in enumerate(daftar, start=1):
            print(f"Juara {i} = Pemain {nama} dengan skor {key}")
        print()

def main():
    bst = SistemSkor()
    pilih = 0
    while pilih != 4:
        print("\n=== Urutan Skor Pemain ===")
        print("1. Masukkan Skor")
        print("2. Hapus Skor")
        print("3. Tampilkan Juara")
        print("4. Keluar")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue
        if pilih == 1:
            try:
                nama = input("Nama pemain: ").strip()
                x = int(input("Masukkan Skor Pemain: "))
                bst.insert(x, nama)
                print(f"Skor {x} dari {nama} berhasil dimasukkan")
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 2:
            try:
                x = int(input("Hapus skor: "))
                bst.delete(x)
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 3:
            bst.tampilkan_juara() 
        elif pilih == 4:
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
