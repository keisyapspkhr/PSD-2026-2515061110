# **Mencari Nomor dalam List Menggunakan Binary Search**

**Deskripsi**: Program ini digunakan untuk mencari sebuah nomor yang sudah disimpan di dalam List, yaitu [12, 15, 28, 32, 56, 98, 110, 125]. Program ini menerapkan Algoritma Binary Search, yaitu salah satu dari Algoritma Searching yang berkerja dengan syarat utamanya data sudah terurut. Cara kerjanya adalah mencari nilai tengah (median) dari data, lalu menbandingkannya dengan angka yang dicari. Ibaratkan data yang diurutkan adalah bersifat ascending. Jika angka tengah lebih besar dibandingkan dengan target, maka data akan fokus mencari ke sebelah kanan dengan cara memcari nilai tengahnya kembali, begitu pula sebaliknya. Program akan melakukan hal yang sama secara terus-menerus hingga menemukan data yang dicari atau bahkan tidak ditemukan sama sekali hingga mengeluarkan peringatan "Data Tidak Ditemukan".

**Source Code**:
<img width="768" height="831" alt="Cuplikan layar 2026-05-05 220021" src="https://github.com/user-attachments/assets/430b222a-2001-4e77-bff2-ec07a50a651c" />
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

Baris 24: Blok try untuk menangkap error.

Baris 25: Minta input dari user, lalu konversi ke int (angka). Ini dikarenakan nilai dari setiap input adalah string.

Baris 26: Jika sukses, break untuk keluar dari loop while.

Baris 27–28: Jika pengguna memasukkan bukan angka (misal huruf), terjadi ValueError, maka cetak pesan error dan loop berulang.

Baris 29: Memanggil fungsi binary_search dengan data, panjang list, dan target. Hasil indeks (atau -1) disimpan di variabel pos.

Baris 30: if pos < 4, karena list memiliki indeks 0–7. Angka 4 adalah batas tengah (indeks 0–3 = depan, indeks 4–7 = belakang). Ini hanya benar jika target ditemukan (pos tidak -1). Namun, jika pos = -1, maka -1 < 4 benar, sehingga akan masuk ke baris 31 dan mencoba mengakses data[-1] yang merupakan elemen terakhir (125)! Ini adalah kesalahan logika (bug). Seharusnya kondisi if pos != -1 dulu, baru membedakan depan/belakang. Tapi sesuai gambar, ini memang ditulis demikian.

Baris 31: Jika pos < 4 (termasuk -1), cetak bahwa nomor ditemukan di "Halaman Depan".

Baris 32–33: Jika pos >= 4, cetak di "Halaman Belakang".

Baris 34–35: else tidak akan pernah tercapai karena semua kemungkinan pos (termasuk -1) sudah masuk ke kondisi pertama. Seharusnya else untuk kasus tidak ditemukan, tapi karena bug, pesan "Nomor tidak ditemukan" tidak akan pernah muncul.

Baris 37: Kondisi standar Python. Jika file ini dijalankan langsung (bukan diimpor sebagai modul), maka __name__ akan bernilai "__main__".

Baris 38: Memanggil fungsi main() sehingga program mulai.
