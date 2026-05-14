class QueueArray:
    def __init__(self, max_size=10):
        self.MAXN = max_size
        self.q = [None] * self.MAXN
        self.front_idx = -1
        self.rear_idx = -1

    def is_empty(self):
        return self.front_idx == -1

    def is_full(self):
        return (self.rear_idx + 1) % self.MAXN == self.front_idx

    def enqueue(self, x):
        if self.is_full():
            print("Antrian Sudah Penuh")
            return
        if self.is_empty():
            self.front_idx = 0
            self.rear_idx = 0
        else:
            self.rear_idx = (self.rear_idx + 1) % self.MAXN
        self.q[self.rear_idx] = x
        print(f"{x} Masuk Ke Antrian Pembayaran")

    def dequeue(self):
        if self.is_empty():
            print("Tidak Ada Antrian Saat Ini")
            return
        print(f"{self.q[self.front_idx]} Telah Selesai Membayar")
        if self.front_idx == self.rear_idx:
            self.front_idx = -1
            self.rear_idx = -1
        else:
            self.front_idx = (self.front_idx + 1) % self.MAXN

    def peek(self):
        if self.is_empty():
            print("Tidak Ada Antrian Saat Ini")
            return
        print(f"Yang Dilayani Saat Ini: {self.q[self.front_idx]}")

    def display(self):
        if self.is_empty():
            print("Tidak Ada Antrian Saat Ini")
            return
        print("Antrian Saat Ini: ", end="")
        i = self.front_idx
        while True:
            print(self.q[i], end=" ")
            if i == self.rear_idx:
                break
            i = (i + 1) % self.MAXN
        print()

def main():
    queue = QueueArray()
    pilih = 0
    while pilih != 5:
        print("\n=== Antrian Kasir Serba Ada ===")
        print("1. Menambah Antrian Pembayaran")
        print("2. Selesai Membayar")
        print("3. Antrian Saat Ini")
        print("4. Seluruh Antrian")
        print("5. Keluar")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue
        if pilih == 1:
            try:
                val = input("Antrian: ")
                queue.enqueue(val)
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 2:
            queue.dequeue()
        elif pilih == 3:
            queue.peek()
        elif pilih == 4:
            queue.display()
        elif pilih == 5:
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
