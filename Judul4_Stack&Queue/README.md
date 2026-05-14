# **Antrian Kasir dengan Menggunakan Struktur Data Queue**

**Deskripsi**: Program ini merupakan implementasi dari Struktur Data Queue yang menggunakan Array berukuran tetap. Queue disini digunakan untuk mengatur dalam antrian dalam pembayaran kasir. Pengguna dapat menambah antrian (enqueue), menghapus antrian setelah seleai (dequeue), melihat antrian yang sedang dilayani (peek), dan menampilkan seluruh antrian. Ukuran dari program ini dirancang hanya memiliki maksimal 10 antrian saja. 

**Source Code**:

<img width="539" height="1697" alt="merged-image-2026-05-14T12-54-14" src="https://github.com/user-attachments/assets/b09e1bd9-025f-482e-8b12-14fdd38c39a0" />


Baris 1: Mendefinisikan kelas QueueArray yang akan mengelola antrian.

Baris 2: Konstruktor kelas, nenerima parameter max_size dengan nilai default 10 yang merupakan nilai maksimum dari antrian yang dapat diterima.

Baris 3: Menyimpan ukuran maksimum dari antrian ke dalam MAXN.

Baris 4: Ini merupakan List yang akan menampung data antrian.

Baris 5: Menyimpan indeks yang paling depan. Nilai -1 menandakan kalau antrian masih dalam keadaan kosong.

Baris 6: Menyimpan indeks yang paling belakang. Nilai -1 menandakan kalau antrian masih dalam keadaan kosong.

Baris 7-8: Fungsi untuk mengecek apakah antrian kosong. Program akan mengembalikan nilai True jika indeks bernilai -1, yang mana artinya bahwa antrian dalam keadaan kosong.

Baris 11-12: Fungsi untuk mengecek apakah antrian dalam keadaan penuh. Jika posisi belakang ditambah satu sama dengan posisi depan, artinya antrian dalam keadaan penuh. Fungsi % adalah untuk kembali ke awal.

Baris 14: Fungsi untuk menambahkan elemen x ke belakang antrian.

Baris 15-17: Kondisi di mana jika antrian dalam kondisi penuh, maka program akan mencetak pesan "Antrian Sudah Penuh" dan keluar dari fungsi tanpa menambah elemen apa pun.

Baris 18-20: Kondisi di mana jika antrian dalam kondisi kosong, maka posisi depan dan belakang akan ke indeks 0 (antrian pertama).

Baris 22-23: Kondisi di mana jika antrian tidak dalam kondisi kosong, maka antrian yang baru ditambahkan akan digeser ke kanan satu langkah, yaitu tepat di belakang antrian yang sudah ditambahkan sebelumnya.

Baris 23-24: Menyimpan nilai yang baru dimasukkan ke posisi belakang, lalu tampilkan pesan berhasil.

Baris 26: Fungsi untuk menghapus elemen yang paling depan.

Baris 27-29: Kondisi di mana jika antrian dalam kondisi kosong, maka program akan mencetak pesan "Tidak Ada Antrian saat ini" dan langsung keluar dari program.

Baris 30: Mencetak pesan yang akan dihapus di depan.

Baris 31-33: Kondisi di mana jika antrian hanya ada, maka depan dan belakang akan berindeks -1 (kosong) setelah dihapus.

Baris 34-35: Kondiisi dimana jika antrian lebih dari satu, maka nilai akan bergeser.

Baris 37-41: Fungsi untuk mengecek antrian yang berada di paling depan. Jika antrian kosong, maka akan mencetak "Tidak Ada Antrian dan Saat Ini". Jika tidak antrian tidak kosong, maka program akan memberitahukan antrian terdepan saat itu.

Baris 43: Fungsi untuk melihat seluruh antrian.

Baris 44-46: Kondisi untuk mengecek apakah antrian kosong.

Baris 47: Mencetak pesna untuk memberitahukan antrian yang ada tanpa pindah baris.

Baris 48-54: Antrian yang akan dicetak dimulai dari antrian yang ada paling depan terlebih dahulu. Jika sudah sampai ke antrian paling belakang, maka berhenti. Setelah selesai, akan pindah baris.

Baris 56: Fungsi yang akan dijalankan pertama kali.

Baris 57: Buat objek antrian dengan ukuran default maksimal 10.

Baris 58: Variabel pilih untuk menyimpan pilihan menu.

Baris 59: Selama pilihan tidak sama dengan 5 (keluar).

Baris 60-65: Mencetak menu plihan.

Baris 66-70: Program meminta input berupa angka, jika user menginputkan yang bukan angka, maka program akan menampilkan pesan error dan meminta user menginputkan ulang.

Baris 71-76: Jika user memilih 1, maka akan memanggil fungsi enqueue (menambahkan antrian). Disini, user bisa menginputkan dalam bentuk string (teks) ataupun integer (angka).

Baris 77-78: Jika user memilih 2, maka akan memanggil fungsi dequeue (menghapus antrian).

Baris 79-80: Jika user memilih 3, maka akan memanggil fungsi peek (melihat antrian paling depan).

Baris 81-82: Jika user memilih 4, maka akan memanggil fungsi display (melihat keseluruhan antrian yang ada).

Baris 83-84: Jika user memilih 5, maka akan keluar dari program dan program akan berhenti.

Baris 85-86: Jika user memilih selain angka 1-5, maka program akan mengeluarkan pesan "Pilihan Tidak Valid".

Baris 88-89: Memastikan bahwa jika file dijalankan secara langsung, maka akan menjalankan fungsi main.

**Ouput Code**:

<img width="296" height="134" alt="image" src="https://github.com/user-attachments/assets/621a1a13-2e90-4cc7-8250-41e11a0ed800" />

Tampilan pertama saat kode baru dijalankan. Program akan meminta user menginputkan pilihan.

<img width="276" height="180" alt="image" src="https://github.com/user-attachments/assets/f270bda1-9a49-4d65-9441-00c60dc8ee91" />
<img width="263" height="184" alt="image" src="https://github.com/user-attachments/assets/9189fff9-4b12-4d7d-bdd3-7ae65696fe5f" />

Ini akan terjadi jika user menginputkan nilai selain dari 1-5, maka program akan mengulang untuk meminta inputan pilihan dari user.

<img width="283" height="152" alt="image" src="https://github.com/user-attachments/assets/c5ca66ac-e828-4690-8bbc-7e1201f8992e" />
<img width="277" height="202" alt="image" src="https://github.com/user-attachments/assets/c68357e6-b2df-4a6b-9a1e-f4f0bb9d97bd" />
<img width="289" height="168" alt="image" src="https://github.com/user-attachments/assets/08d0ea03-c93b-4cf6-a53a-8673f2df4d16" />

Jika user memilih 1, maka program akan meminta user memasukkan nama atau angka yang ingin ditambahkan ke dalam antrian. Dan program akan mengulang meminta user menginputkan pilihan.

<img width="280" height="289" alt="image" src="https://github.com/user-attachments/assets/6ab35d22-7eda-4aea-97dd-5c15bc9b15b9" />

Jika user meilih 3, maka program akan menunjukkan antrian yang ada paling depan saat itu. Setelah itu, program akan meminta kembali user untuk memilih.

<img width="286" height="288" alt="image" src="https://github.com/user-attachments/assets/29c7037e-691f-4239-8861-9835654623da" />

Jika user memilih 4, maka program akan menunjukkan seluruh antrian. Setelah itu, perogram akan kembali meminta user untuk memilih.

<img width="273" height="293" alt="image" src="https://github.com/user-attachments/assets/01409e64-df35-455c-8aaa-51d879cb3969" />
<img width="295" height="151" alt="image" src="https://github.com/user-attachments/assets/0ee66b83-3188-4167-a7f1-4d4a62a317bc" />

Jika user memilih 2, maka secara otomatis program akan mengeluarkan antrian paling depan.

<img width="282" height="150" alt="image" src="https://github.com/user-attachments/assets/78feadbb-7455-4ee6-83d7-a7a2c002890f" />

Setelah user memilih 5, barulah program akan selesai dijalankan.

**Video YouTube**: https://youtu.be/HpnJIVtURuI
