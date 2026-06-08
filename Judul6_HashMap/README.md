# **DAFTAR BUKU DI PERPUSTAKAAN**

**Deskripsi:** Program Sistem Perpustakaan ini adalah sebuah program sederhana untuk mengelola data buku menggunakan metode HASH MAP dengan SEPARATE CHAINING. 

Fitur yang tersedia antara lain: (1) Menampilkan seluruh data buku (Melihat daftar buku yang tersimpan di setiap bucket hash table), (2) Menambahkan buku baru (Memasukkan kode buku (angka) dan judul buku ke dalam sistem), (3) Mencari buku (Mencari buku berdasarkan kode buku), (4) Keluar (Mengakhiri program).

Program sudah memiliki beberapa data awal

**Source Code:**

<img width="800" height="2276" alt="merged-image-2026-06-08T12-40-51" src="https://github.com/user-attachments/assets/748688d4-d4fe-48b4-8bf6-c64b6b867ce5" />

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

<img width="173" height="82" alt="image" src="https://github.com/user-attachments/assets/ad0ee314-8cc4-44ef-88ef-0eca3f712b06" />

Tampilan yang akan ditampilkan saat program dijalankan pertama kali.

<img width="161" height="38" alt="image" src="https://github.com/user-attachments/assets/8327fe26-88cf-4b62-9bc9-47943828520e" />
<img width="157" height="35" alt="image" src="https://github.com/user-attachments/assets/bca33984-6ee0-4df2-b5fd-149d798f5d41" />
<img width="170" height="188" alt="image" src="https://github.com/user-attachments/assets/ba01741a-d676-4b49-abcb-848556511a36" />

Jika pengguna salah menginputkan menu awal, maka akan muncul pesan kesalahan dan program akan terus mengulang meminta inputan pilihan menu dari pengguna sampai pengguna memasukkan benar antara angka 1-4.

<img width="278" height="280" alt="image" src="https://github.com/user-attachments/assets/1200efcc-d722-4733-a0d8-de16b2e973c8" />

Tampilan saat pengguna memilih menu 1, yaitu menampilkan seluruh data buku yang ada. Setelah itu, program akan kembali meminta inputan pilihan dari pengguna.

<img width="176" height="109" alt="image" src="https://github.com/user-attachments/assets/bc9b29d7-5193-409f-8879-517e988fb711" />
<img width="179" height="119" alt="image" src="https://github.com/user-attachments/assets/de879e4f-7422-4e40-bba4-cbbdaae6bd74" />
<img width="200" height="128" alt="image" src="https://github.com/user-attachments/assets/767d57da-373a-4b1d-925b-16e435ac9bf5" />
<img width="167" height="129" alt="image" src="https://github.com/user-attachments/assets/de3ba46e-503d-449a-9510-cd8a232f64f5" />

Tampilan saat pengguna memilih menu 1, yaitu menambahkan buku baru ke dalam daftar. Pengguna akan diminta untuk menginputkan kode dan judul bukunya. Namun, jika pengguna salah menginputkan kode buku, maka program akan menampilkan pesan kesalahan.

<img width="221" height="111" alt="image" src="https://github.com/user-attachments/assets/15f9eda3-3823-46d7-9c19-a0a49d8dd689" />
<img width="167" height="118" alt="image" src="https://github.com/user-attachments/assets/7505479c-9aad-46e1-8841-113783ae7249" />
<img width="164" height="145" alt="image" src="https://github.com/user-attachments/assets/e4f67b93-8b8c-43f3-b99f-be57608f8517" />
<img width="164" height="128" alt="image" src="https://github.com/user-attachments/assets/966b511a-a90a-4f29-8972-468aac3b0133" />

Tampilan saat pengguna memilih menu 3, yaitu mencari buku dalam data. Jika pengguna memasukkan buku yang tidak ada dalam pencarian, maka program akan menampilkan pesan bahwa buku tidak ditemukan. Namun, jika ditemukan, program akan menampilkan judul buku dari kode yang dicari pengguna. Ada juga jika pengguna menginputkan selain angka, maka program akan menampilkan pesan kesalahan.

<img width="167" height="90" alt="image" src="https://github.com/user-attachments/assets/6feb7662-216e-4239-b538-58e7ae1aeb69" />

Tampilan jika pengguna memilih menu 4, yaitu keluar dari program. Maka program akan berhenti dan selesai.

Program ini akan terus meminta pengguna untuk menginputkan pilihan sampai pengguna memilih menu 4, yaitu menu untuk keluar dari program.

**Link YouTube:**
