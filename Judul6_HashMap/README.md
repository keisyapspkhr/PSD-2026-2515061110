# **DAFTAR BUKU DI PERPUSTAKAAN**

**Deskripsi:** Program Sistem Perpustakaan ini adalah sebuah program sederhana untuk mengelola data buku menggunakan metode HASH MAP dengan SEPARATE CHAINING. 

Fitur yang tersedia antara lain: (1) Menampilkan seluruh data buku (Melihat daftar buku yang tersimpan di setiap bucket hash table), (2) Menambahkan buku baru (Memasukkan kode buku (angka) dan judul buku ke dalam sistem), (3) Mencari buku (Mencari buku berdasarkan kode buku), (4) Keluar (Mengakhiri program).

Program sudah memiliki beberapa data awal

**Source Code:**



Baris 1: Mendefinisikan Class Node untuk Linked List

Baris 2: Inisialisasi objek dari class Node dengan 3 parameter, yaitu self, key, value.

Baris 3: Menyimpan key yang akan menjadi Kode Buku

Baris 4: Menyimpan Value yang akan menjadi Judul Buku

Baris 5: Pointer ke node berikutnya yang di mana awalnya None karena masih dalam keadaan kosong.

Baris 7: Menfinisikan class utama Hash Map dengan Separate Chaining.

Baris 8: Konstruktor. Pada parameter, menunjukkan size default-nya, yaitu 10. Size ini merupakan besar memori yang ada pada program.

Baris 9: Menyimpan ukuran Hash Table

Baris 10: Membuat Array berisi Node sebanyak Size (10). Bernilai Node karena masih kosong.

Baris 12: Fungsi Hash untuk menentukan indeks data.

Baris 13: Rumus untuk menghasilkan indeks dari key (kode buku) yang dimasukkan pengguna. Dilakukan modulus 2 kali adalah untuk meminimalisir error.

Baris 15: Fungsi untuk menambahkan buku baru.

Baris 16: Menghitung indeks dari key dengan menggunakan fungsi hash_function.

Baris 17: Mengambil elemen pertama Linked List di indeks tersebut.

Baris 18: Loop sepanjang Linked List jika Linked List dalam indeks yang dituju tidak kosong.

Baris 19-21: Jika key sudah ada dalam daftar, maka value (judul buku) lama dari indeks tersebut akan dihapus dan diganti dengan yang baru.

Baris 22: Pindah ke Node berikutnya.

Baris 23: Membuat node baru.

Baris 24: Node baru menunjuk ke elemen pertama lama yang ada pada linked list.

Baris 25: Elemen pertama pada Linked List di indeks diganti dengan node baru.

Baris 26: Berhasil menambahkan data baru ke dalam program.

Baris 28: Fungsi untuk mencari buku berdasarkan key (kode buku)
.
Baris 29-30: Menghitung indeks dan mengambil elemen pertama yang ada pada indeks yang dituju.

Baris 31: Loop sepanjang Linked List jika Linked List dalam indeks yang dituju tidak kosong.

Baris 32-33: Jika ketemu, kembalikan nilai node tersebut.

Baris 34: Lanjut ke node berikutnya.

Baris 35: Menghentikan proses dan mengembalikan nilai None.

Baris 37: Fungsi untuk menampilkan seluruh isi Hash.

Baris 38-40: Mencetak garis pemisah dan nama program.

Baris 41: Loop sepanjang ukuran dari program.

Baris 42: Mencetak nomor rak yang merupakan indeks untuk Hash.

Baris 43: Mengambil elemen pertama yang ada pada indeks (rak).

Baris 44-45: Jika kosong, maka cetak "Kosong".

Baris 46: Kondisi lainnya, yaitu jika ada isinya.

Baris 47: Loop semua node yang ada pada indeks (rak).

Baris 48: Mencetak isi yang ada pada indeks tersebut.

Baris 49-50: Jika pada indeks memiliki lebih dari satu isi/elemen, maka akan diberikan "->" untuk menunjuk ke elemen selanjutnya.

Baris 55: Fungsi utama yang akan dijalankan oleh program untuk pengguna.

Baris 56: Membuat objek Hash Map yang mempresentasikan dari Class HashMapSeparateChaining()

Baris 57: Inisialisasi variabel pilihan untuk menu.

Baris 59-62: Menambahkan buku yang sudah tersedia dari sistem.

Baris 64: Loop menu sampai pilih 4.

Baris 65-73: Menampilkan pilihan menu kepada pengguna.

Baris 74-75: Mencegah error saat pengguna menginputkan yang bukan angka saat diminta pengiputan pilihan menu.

Baris 76-79: Saat pengguna menginputkan selain angka 1-4 dan program akan mengulang Loop.

Baris 81-82: Saat pengguna memilih menu 1 yang merupakan menampilkan seluruh isi Hash, maka program akan memanggil fungsi display untuk menampilkan seluruh data.

Baris 83-92: Jika pengguna memilih menu 2 yang merupakan menambahkan buku baru, maka program akan meminta pengguna menginputkan kode buku yang merupakan angka dan memasukkan judul buku. Setelah itu, program akan memanggil fungsi insert untuk menambahkan buku tersebut ke dalam data program dan program akan menampilkan pesan keberhasilan penambahan buku baru. Namun, jika pengguna menginputkan kode buku bukan angka, maka akan muncul pesan error.

Baris 93-106: Jika pengguna memilih menu 3 yang merupakan pencarian buku, maka proggram akan meminta pengguna untuk menginputkan kode buku yang sedang dicari. Setelah itu, program akan memanggil fungsi search untuk mencari buku tersebut. Jika buku ditemukan, program akan menampilkan kode dan judul bukunya, jika tidak ditemukan, program akan menampilkan pesan tidak ditemukan. Input dari pengguna harus berupa angka, jika tidak maka akan memunculkan pesan error.

Baris 107-109: Jika pengguna memiliki menu 4 yang merupakan keluar dari program, maka program akan berhenti.

Baris 110-112: Kondisi dimana pengguna memasukkan angka selain angka 1-4.

Baris 114-115: Memastikan bahwa main() dijalankan dan file digunakan secara langsung.

**Output:**

**Link YouTube:**
