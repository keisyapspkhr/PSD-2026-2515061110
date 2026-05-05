# **Mencari Nomor dalam List Menggunakan Binary Search**

**Deskripsi**: Program ini digunakan untuk mencari sebuah nomor yang sudah disimpan di dalam List, yaitu [12, 15, 28, 32, 56, 98, 110, 125]. Program ini menerapkan Algoritma Binary Search, yaitu salah satu dari Algoritma Searching yang berkerja dengan syarat utamanya data sudah terurut. Cara kerjanya adalah mencari nilai tengah (median) dari data, lalu menbandingkannya dengan angka yang dicari. Ibaratkan data yang diurutkan adalah bersifat ascending. Jika angka tengah lebih besar dibandingkan dengan target, maka data akan fokus mencari ke sebelah kanan dengan cara memcari nilai tengahnya kembali, begitu pula sebaliknya. Program akan melakukan hal yang sama secara terus-menerus hingga menemukan data yang dicari atau bahkan tidak ditemukan sama sekali hingga mengeluarkan peringatan "Data Tidak Ditemukan".

**Source Code**:
<img width="760" height="830" alt="Cuplikan layar 2026-05-05 223023" src="https://github.com/user-attachments/assets/fba6cd34-d8d2-4877-8914-3754cdb8ee34" />

Baris 1: Mendefinisikan fungsi binary_search dengan tiga parameter, yaitu data sebagai list yang sudah terurut (dari kecil ke besar), n sebagai panjang list (jumlah elemen), dan target sebagai nilai yang ingin dicari.

Baris 2: l yang mendefinisikan left, yaitu indeks paling kiri dari area pencarian, diinisialisasi dengan 0.

Baris 3: r yang mendefinisikan right, yaitu indeks paling kanan, memuat n - 1 karena indeks list mulai dari 0 sehingga jumlah data(n) - 1.

Baris 4: pos = -1 sebagai tanda bahwa target belum ditemukan. Nanti akan diisi indeks jika ketemu.

Baris 5: Selama l masih lebih kecil atau sama dengan r, artinya masih ada ruang pencarian. Jika l > r, berarti target tidak ada.

Baris 6: Menghitung indeks tengah (m) dengan rumus l + (r - l) // 2. 

Baris 7: Mencetak nilai tengah (m) dan nilai data di indeks tersebut. Ini membantu untuk melihat proses pencarian.

Baris 8–10: Jika nilai tengah sama dengan target, maka target ditemukan. Simpan indeks di pos, lalu break keluar dari loop.

Baris 11–13: Jika nilai tengah lebih kecil dari target, berarti target berada di kanan (karena list terurut membesar (ascending)). Maka geser batas kiri (l(left)) ke m + 1. Cetak "Mencari ke Halaman Belakang".

Baris 14–16: Jika nilai tengah lebih besar dari target, target berada di kiri. Geser batas kanan r ke m - 1. Cetak "Mencari ke Halaman Depan".

Baris 17: Mengembalikan nilai pos. Jika target ditemukan, pos berisi indeks. Jika tidak, maka tetap -1.

Baris 19: Mendefinisikan fungsi main sebagai titik masuk program.

Baris 20: Membuat list data berisi 8 angka yang sudah terurut secara ascending.

Baris 21: n = len(data) untuk mengeluarkan panjang data list, yaitu 8.

Baris 22: Mencetak isi list.

Baris 23: Loop tak terbatas untuk meminta input hingga bernilai TRUE atau valid

Baris 24: Blok try untuk mencoba menangkap kode yang ada di dalamnya

Baris 25: Minta input dari user, lalu konversi ke int (angka). Ini dikarenakan nilai dari setiap input adalah string.

Baris 26: Jika sukses, break untuk keluar dari loop while.

Baris 27–28: Jika pengguna memasukkan bukan angka (misal huruf), terjadi ValueError, maka cetak pesan error dan loop berulang, yaitu kembali ke loop aawwal untuk meminta user menginputkan nilai ulang, Loop ini akan terus berulang hingga user memasukkan nilai yang bernilai TRUE atau valid.

Baris 29: Memanggil fungsi binary_search dengan data, panjang list, dan target. Hasil indeks (atau -1) disimpan di variabel pos.

Baris 30: Kondisi pertama, jika pos bukan -1 (artinya ditemukan) dan pos kurang dari 4 (indeks 0,1,2,3), maka cetak bahwa nomor ditemukan di Halaman Depan. Kode ini akan berjalan hanya jika kedua syarat terpenuhi.

Baris 31: Jika pos < 4 (termasuk -1), cetak bahwa nomor ditemukan di "Halaman Depan".

Baris 32–33: Jika pos >= 4, cetak di "Halaman Belakang".

Baris 34–35: Jika pos == -1 (tidak ditemukan), maka cetak "Nomor tidak ditemukan".

Baris 37: Kondisi standar Python. Jika file ini dijalankan langsung.

Baris 38: Memanggil fungsi main() sehingga program mulai.

**Output Program**:
<img width="611" height="67" alt="image" src="https://github.com/user-attachments/assets/dacc8314-e41c-49be-972d-9fb9a0b9011f" />
Saat program baru dijalankan, program akan meminta user untuk menginputkan nilai yang ingin dicari terlebih dahulu.

<img width="532" height="198" alt="image" src="https://github.com/user-attachments/assets/83247867-4ff6-4418-86d6-8ff73384dea4" />
Output yang akan keluar jika user memasukkan angka yang lebih KECIL dari nilai tengahnya, yaitu indeks ke-3 (32).

<img width="580" height="203" alt="image" src="https://github.com/user-attachments/assets/d8806418-4620-4deb-9436-134eaac0569f" />
Output yang akan keluar jika user memasukkan angka yang lebih BESAR dari nilai tengahnya, yaitu indeks ke-3 (32).

<img width="500" height="267" alt="image" src="https://github.com/user-attachments/assets/b4d001d9-a912-4549-937a-b9a380332166" />
Output yang akan keluar jika user memasukkan angka yang TIDAK ADA di dalam list yang tersedia.

<img width="610" height="116" alt="image" src="https://github.com/user-attachments/assets/f5ae780f-ef28-4816-bdf6-cd10142a94f0" />
Hal yang akan terjadi jika user salah memasukkan input, yaitu BUKAN angka.
