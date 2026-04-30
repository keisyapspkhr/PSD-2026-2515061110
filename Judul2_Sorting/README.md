# **Mengurutkan Nilai Siswa**

**Deskripsi:** Program ini mengurutkan daftar nilai siswa secara _descending_ (dari tertinggi ke terendah) menggunakan algoritma Bubble Sort. User dapat memasukkan jumlah siswa, lalu untuk setiap siswa tersebut user akan memasukkan nama dan nilai dalam bentuk float. Fungsi _Bubble Sort_ adalah membandingkan pasangan elemen berurutan, yaitu jika nilai kiri lebih kecil dari kanan, kedua elemen ditukar. Proses diulang hingga seluruh data terurut menurun.

**Source Code:**
<img width="675" height="1022" alt="merged-image-2026-04-30T14-18-49" src="https://github.com/user-attachments/assets/b39c70f1-18ad-4dcf-b098-3005de0eac0e" />


Baris 1: Mendefinisikan fungsi bernama tukar dengan tiga parameter: arr (list yang akan diubah), i (indeks pertama), j (indeks kedua).

Baris 2: Menyimpan nilai arr[i] ke variabel sementara temp.

Baris 3: Mengisi arr[i] dengan nilai arr[j].

Baris 4: Mengisi arr[j] dengan nilai yang tadi disimpan di temp.

Hasilnya: Elemen pada posisi i dan j dalam list arr saling bertukar tempat.

Baris 7: Mendefinisikan fungsi bubble_sort dengan parameter arr (list yang akan diurutkan) dan n (panjang list/jumlah siswa).

Baris 8: Perulangan luar (i) dari 0 sampai n-2. Banyaknya iterasi adalah n-1. Setiap iterasi akan menggerakkan satu elemen terbesar ke akhir (karena pengurutan descending – nilai besar di depan).

Baris 9: Perulangan dalam (j) dari 0 sampai n-i-2. Perulangan ini membandingkan pasangan elemen yang berdekatan. Batasnya berkurang setiap iterasi luar karena elemen terakhir sudah terurut.

Baris 10: Jika nilai di indeks j lebih kecil dari nilai di indeks j+1 (artinya urutan tidak descending) 

Baris 11: panggil fungsi tukar untuk menukar kedua elemen tersebut. Setelah loop selesai, list terurut menurun.

Baris 14: Definisikan fungsi main sebagai titik masuk program.

Baris 15: Mulai blok try untuk menangkap kesalahan konversi tipe data.

Baris 16: Minta pengguna memasukkan jumlah siswa, lalu konversi ke integer (int). Hasil disimpan di variabel n.

Baris 17: Jika pengguna memasukkan bukan angka (misal huruf), Python akan memunculkan ValueError, dan program langsung lompat ke except.

Baris 18: Cetak pesan "Input tidak valid!".

Baris 19: return untuk keluar dari fungsi main tanpa melanjutkan ke proses berikutnya (program berhenti).

Baris 21: Membuat list kosong arr untuk menyimpan data siswa (setiap siswa berupa list [nilai, nama]).

Baris 22: Mencetak instruksi.

Baris 23: Perulangan for sebanyak n kali (untuk setiap siswa). i dimulai dari 0.

Baris 24: while True – loop tak terbatas yang akan berhenti hanya jika input nilai berhasil (menggunakan break).

Baris 25: Mulai blok try di dalam loop, untuk validasi input nilai.

Baris 26: Minta nama siswa. String f"siswa ke-{i+1}: " akan menampilkan nomor urut siswa (i+1 karena i mulai 0).

Baris 27: Minta nilai siswa, lalu konversi ke float (bukan integer). Ini memungkinkan nilai desimal seperti 85.5.

Baris 28: Menambahkan elemen baru ke arr berupa list kecil [nilai, nama]. Contoh: [90.0, "Ali"].

Baris 29: break membuat keluar dari loop while True karena input sudah valid. Program lanjut ke siswa berikutnya.

Baris 30: Jika terjadi ValueError (misal input "abc" untuk nilai), program akan eksekusi blok except.

Baris 31: Cetak pesan error, lalu loop while akan mengulang dari awal (input nama dan nilai lagi untuk siswa yang sama).

Baris 33: Cetak isi arr sebelum diurutkan.

Baris 35: Panggil fungsi bubble_sort(arr, n). Fungsi ini akan mengurutkan arr secara descending berdasarkan nilai (elemen pertama dari tiap sublist). Fungsi bubble_sort mengubah arr secara langsung (in-place).

Baris 37: Cetak "Nilai setelah diurutkan:" tanpa ganti baris (end=" ").

Baris 38–39: Loop for i in range(n) mencetak setiap elemen arr[i] diikuti spasi, tanpa pindah baris.

Baris 40: Cetak baris kosong (print()) agar tampilan rapi.

Baris 43: Kondisi khusus Python. __name__ akan bernilai "__main__" jika file dijalankan langsung.

Baris 44: Memanggil fungsi main() sehingga program mulai berjalan.

**Output Program:**
<img width="447" height="38" alt="Cuplikan layar 2026-04-30 223733" src="https://github.com/user-attachments/assets/10c9d189-309c-4af3-8a57-6cdea8f33f2c" />
Saat pertama kali program dijalankan, program akan meminta user untuk menginputkan jumlah dari siswa yang ingin diurutkan nilainya.

<img width="348" height="51" alt="Cuplikan layar 2026-04-30 223751" src="https://github.com/user-attachments/assets/728cf502-2733-4b3d-9c59-8a2227b77a2f" />
Setelah memasukkan jumlah siswa, program akan mulai meminta user untuk menginputkan nama dari siwa tersebut.

<img width="356" height="71" alt="Cuplikan layar 2026-04-30 223808" src="https://github.com/user-attachments/assets/096b9b08-ecfe-47ab-806e-12da116beeee" />
Setelah menginputkan nama, user akan meminta program untuk menginputkan nilai dari siswa tersebut.

<img width="417" height="155" alt="Cuplikan layar 2026-04-30 223912" src="https://github.com/user-attachments/assets/4b919df3-cfce-4ffc-b055-2558f6d2c9f8" />
Saat user tanpa sengaja menginputkan nilai yang salah, maka program akan mengeluarkan pemberitahuan dan meminta user untuk menginput ulang nilai mahasiswa yang salah tersebut mulai dari namanya.

<img width="707" height="276" alt="Cuplikan layar 2026-04-30 224256" src="https://github.com/user-attachments/assets/79b0d8ad-3872-4055-b646-d6c33ea9dd4a" />
Karena sebelumnya user sudah memasukkan jumlah siswa yang akan diurutkan berjumlah 3 orang, maka setelah melakukan pengulangan tiga kali, program akan menampilkan hasilnya.

<img width="705" height="52" alt="Cuplikan layar 2026-04-30 224304" src="https://github.com/user-attachments/assets/8a4d5b86-5de9-4b9f-ae08-cba72d6ec931" />
Program akan menampilkan data sebelum dan sesudah diurutkan.

**Link YouTube:**
https://youtu.be/H1JvVLCOk3U
