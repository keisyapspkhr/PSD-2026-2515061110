# **Mengelola Peringkat Pemain Berdasarkan Skor**

**Deskripsi**: Program ini merupakan implementasi dari Struktur Data Binary Search Tree. Program ini memanfaatkan setiap operasi yang berada di dalam Binary Search Tree, yaitu penyisipan, penghapusan, dan pencarian. Program ini dirancang untuk mendapat input dari user berupa nama pemain dan skornya, lalu dapat mengurutkannya secara descending (kanan-root-kiri) untuk mendapatkan daftar juara berdasarkan urutan skor dari besar ke kecil.

**Source Code**:

<img width="790" height="3760" alt="merged-image-2026-05-21T13-29-40" src="https://github.com/user-attachments/assets/d97f3f77-9838-4048-a4dc-a96413f0d691" />

Baris 1: Mendefinisikan kelas untuk membuat Tree

Baris 2: Konstruktor yang akan dipanggil saat objek Node dibuat. Parameter key untuk skor dan nama untuk pemain.

Baris 3-4: Menyimpan nilai skor dan nama pemain

Baris 5-6: Pointer ke kiri dan kanan yang dimulai dengan None.

Baris 8: Kelas utama dari Binary Search yang dibuat.

Baris 9: Konstruktor

Baris 10: Root diisi dengan Node yang menandakan bahwa Root dalam kondisi kosong dan belum terisi.

Baris 12: Fungsi untuk menyisipkan node baru.

Baris 13-14: Memeriksa apakah root dalam kondisi kosong.

Baris 15-16: Jika skor lebih kecil dari skor root yang ada, maka skor akan diletakkan di sebelah kiri root (left-child).

Baris 17-18: Jika skor lebih besar dari skor root yang ada, maka skor akan diletakkan di sebelah kanan root (right-child).

Baris 19: Mengembalikan root yang sudah dimodifikasi.

Baris 21-22: Untuk memperbarui Tree.

Baris 24-28: Fungsi untuk mencari nilai skor terkecil dalam Tree dengan selalu mencari disebelah kiri.

Baris 30: Fungsi untuk mencari nilai skor (key). 

Baris 31-32: Jika root dalam kondisi kosong, maka akan mengembalikan nilai None (tidak ada yang bisa dicari).

Baris 33-38: Untuk menemukan skor yang dicari oleh pengguna. Jika key = root, maka akan mengembalikan nilai root. Jika key lebih kecil dari root, maka program akan mencari ke sebelah kiri root (Left-Child). Jika kondisi yang lain, yaitu key lebih besar dari root, maka program akan mencari ke sebelah kanan root (Right-Child).

Baris 40: Fungsi untuk menghapus node berdasarkan key (skor yang dicari pengguna).

Baris 41-42: Jika root tidak ada, maka tidak ada yang dihapus.

Baris 43-46: Membandingkan key dengan root. Jika key lebih kecil, maka mencari ke kiri. Jika key lebih besar, maka mencari ke kanan. 

Baris 47: Kondisi Node ditemukan

Baris 48-49: Jika tidak ada anak (leaf), maka program akan menghapus dengan mengembalikan nilai None.

Baris 50-53: Jika hanya punya anak kanan, maka ganti dengan node anak kanannya. Begitu pula sebaliknya.

Baris 54: Kondisi jika Node memiliki 2 anak.

Baris 55-58: Cari pengganti dengan nilai terkecil di subtree kanan. Setelah itu, ganti skor dan nama node dengan node pengganti. Lalu, hapus node awal pengganti.

Baris 59: Kembalikan root yang sudah dimodifikasi.

Baris 61: Fungsi untuk menghapus key (skor).

Baris 62: Mencari node berdasarkan skor.

Baris 63-65: Jika node tidak ditemukan, maka akan menampilkan pesan error, lalu keluar dari fungsi.

Baris 66: Menyimpan nama pemain sebelum dihapus.

Baris 67: Menghapus dan memperbarui root.

Baris 68: Mencatak konfirmasi kalau skor dari pemain berhasil dihapus.

Baris 70: Fungsi untuk mengurutkan data secara descending (besar ke kecil / kanan-root-kiri).

Baris 71-72: Jika root kosong, maka keluar dari fungsi.

Baris 73-76: Mengunjungi subtree kanan terlebih dahulu karena memiliki nilai yang lebih besar. Setelah itu, masukkan root. Terakhir, mengunjungi subtree kiri karena memiliki nilai yang lebih kecil.

Baris 77: Fungsi untuk menampilkan urutan juara.

Baris 78-79: Jika root dalam kondisi kosong, maka akan mencetak pesan dan keluar dari fungsi.

Baris 80: List untuk menyimpan hasil.

Baris 81: Memanggil fungsi descending . Hasilnya akan berupa urutan skor dari tinggi ke terendah dengan nama pemain.

Baris 84 : untuk loop sepanjang daftar yang ada.

Baris 85: Mmebongkar tuple.

Baris 86: Mencetak peringkat.

Baris 87: Baris kosong.

Baris 89: Fungsi utama dari program.

Baris 90: Membuat objek bst.

Baris 91: Inisialisasi variabel.

Baris 92: Loop menu hingga pilih 4.

Baris 93-97: Mencetak pilihan menu.

Baris 98-102: Meminta pengguna menginputkan pilihan. Jika pengguna memasukkan selain agka, maka akan mencetak error dan melanjutkan loop untuk meminta pengguna menginputkan ulang.

Baris 103-110: Jika pengguna menginputkan angka 1, maka pengguna akan diminta untuk menginputkan nama dan skor dari pemain. Setelah itu, fungsi insert akan dipanggil dan mencetak pesan berhasil. Namun, jika pengguna salah menginputkan, maka pesan error akan keluar. Fungsi .strip() adalah untuk menghapus spasi di awal dan akhir sebuah string yang mungkin tidak sengaja pengguna input.

Baris 111-116: Jika pengguna menginputkan angka 2, maka pengguna akan diminta menginputkan skor yang akan dihapus. Setelah itu, fungsi delete akan dipanggil. Jika pengguna salah menginputkan, maka pesan error akan keluar.

117-118: Jika pengguna menginputkan angka 3, maka fungsi tampilkan_juara akan dipanggil.

Baris 119-120: Jika pengguna menginputkan akan 4, maka program selesai.

Baris 121-122: Jika pengguna menginputkan selain angka 1-4, maka pesan error akan meuncul dan meminta pengguna menginputkan ulang.

Baris 124: Memastikan bahwa file dijalankan secara langsung.

Baris 125: Memanggil fungsi utama.

**Output:**

<img width="265" height="117" alt="image" src="https://github.com/user-attachments/assets/be23de0d-2fe6-4636-b856-18f2af1dbb1c" />

Tampilan pertama saat program baru saja dimulai.

<img width="256" height="166" alt="image" src="https://github.com/user-attachments/assets/05d507ab-00b7-4377-a3f3-6ab4ae5fc0be" />
<img width="253" height="167" alt="image" src="https://github.com/user-attachments/assets/8d74e592-1ed0-4389-95c0-e0022dbaf017" />

Jika Pengguna menginputkan pilihan selain angka 1-4, maka akan muncul pesan error.

<img width="295" height="130" alt="image" src="https://github.com/user-attachments/assets/15d7f5cc-6167-4df6-b37a-2ed948e51a73" />
<img width="368" height="151" alt="image" src="https://github.com/user-attachments/assets/7d34c0dc-8bea-459f-a151-46c9b6eab1c8" />
<img width="304" height="188" alt="image" src="https://github.com/user-attachments/assets/ba5a9c3e-a011-4f9e-9dc8-2209811c71f2" />

Jika pengguna memilih menu 1, maka program akan meminta pengguna menginputkan nama dan skor dari pemain yang ingin disimpan. Setelah itu, program akan kembali meminta input dari user terkait pilihan menu.

<img width="305" height="362" alt="image" src="https://github.com/user-attachments/assets/8ed0473e-4f8b-43ed-b0b6-88cd7d06cba9" />

Jika pengguna memilih menu 3, maka program akan menampilkan urutan juara berdasarkan skor. Program akan kembali berjalan.

<img width="283" height="132" alt="image" src="https://github.com/user-attachments/assets/c293c2a1-d552-4c50-9c4a-c2f660a8f1ef" />
<img width="349" height="272" alt="image" src="https://github.com/user-attachments/assets/2d59d49f-edd8-4d92-87d3-0638de0c6c2c" />
<img width="305" height="201" alt="image" src="https://github.com/user-attachments/assets/5a21a183-7ba5-4149-9402-3a708e3f0155" />

Jika pengguna memilih menu 2, maka program akan meminta pengguna untuk menginputkan skor yang ingin dihapus. Setelah itu, program akan kembali berjalan.

<img width="230" height="137" alt="image" src="https://github.com/user-attachments/assets/fb91f847-bc3e-4fbb-a230-ab17fee04fdc" />

Saat pengguna memilih menu 4, barulah progran benar-benar berhenti dan tidak akan meminta inputkan apa pun lagi dair pengguna.

**Link YouTube:** https://youtu.be/BG6W3Az4Ye8
