#**Manajemen Nilai Mahasiswa**

**Deskripsi singkat :**
Program ini dibuat untuk mengelola nilai mahasiswa. Program ini memungkinkan user menentukan jumlah mahasiswa yang akan diolah datanya. Program ini memungkinkan pengguna untuk memantau kapasitas kelas, memeriksa nilai, serta memperbarui data nilai dan mendapatkan total akumulasi dan nilai rata-rata. Program ini dapat menampung sejumlah mahasiswa yang ditentukan oleh user di awal. Dengan begitu, pengajar dapat memastikan bahwa data yang dimasukkan sesuai dengan jumlah mahasiswa di kelas.

Program ini memiliki menu sederhana yang memudahkan pengguna untuk:

1. Memantau kapasitas kelas

2. Memeriksa rincian nilai tiap mahasiswa

3. Memperbarui data nilai

4. Mendapatkan total akumulasi dan nilai rata-rata

Program ini dirancang untuk mencegah kerusakan jika pengguna memasukkan data yang tidak valid. Program ini hanya menerima nilai antara 0 hingga 100.

Program ini menggunaakan list sebagai struktur data utamanya karena menyimpan data secara berurutan dan mengakses data secara cepat.

**Source Code:**

<img width="789" height="1288" alt="Image" src="https://github.com/user-attachments/assets/5397ac74-487f-40ba-adaa-004bfe03e192" />
Baris 1-5: Mendefinisikan fungsi menu(). Fungsinya hanya untuk menampilkan daftar pilihan interaksi kepada user.

Baris 7: Memasuki fungsi utama main().

Baris 8: Program meminta input jumlah kuota mahasiswa (n) dari pengguna dan mengubahnya menjadi tipe data integer (bilangan bulat) karena setiap input dari user itu bertipe string.

Baris 9: Membuat struktur data List bernama nilai dengan panjang sebanyak n. Semua elemen diisi dengan angka 0 sebagai nilai awal.

Baris 10: Menetapkan variabel running = True sebagai penanda bahwa loop program sedang aktif.

Baris 11: Memulai loop while. Selama running bernilai True, program akan terus kembali ke menu utama.

Baris 12: Memanggil fungsi menu() untuk menampilkan pilihan.

Baris 13-17: Menggunakan blok try-except untuk mengambil input choice (pilihan menu). Jika user memasukkan selain angka, program akan menangkap kesalahan tersebut, menampilkan pesan peringatan, dan perintah continue akan memaksa program mengulang ke awal baris 11.

Baris 19-20: Jika pilihan adalah 1, program menghitung panjang list menggunakan len(nilai) dan menampilkannya. Ini menunjukkan jumlah mahasiswa yang telah ditentukan oleh user sebelumnya.

Baris 22-23: Jika pilihan adalah 2, program mencetak daftar nilai mahasiswa.

Baris 24-25: Melakukan loop for sebanyak panjang list. Program mencetak nilai tiap mahasiswa berdasarkan indeksnya (i). Penggunaan {i+1} hanya untuk tampilan agar urutan dimulai dari angka 1, bukan 0, karena indeks selalu dimulai dari 0.

Baris 28: Menyiapkan variabel total = 0 untuk menampung jumlah seluruh nilai.

Baris 30: Mulai mengulang untuk mengisi setiap slot di dalam list nilai.

Baris 31-42: Di dalam setiap urutan mahasiswa, terdapat while True untuk memastikan input yang masuk benar.

Baris 33: Meminta input skor (tipe float agar bisa desimal).

Baris 34-36: Mengecek apakah skor berada di rentang 0-100. Jika ya, simpan ke dalam list nilai[i] dan tambahkan ke variabel total.

Baris 37-42: Jika nilai di luar rentang atau bukan angka, tampilkan pesan kesalahan dan minta input ulang untuk mahasiswa yang sama.

Baris 44: Setelah semua mahasiswa diinput, program menghitung rata_rata dengan membagi total dengan jumlah mahasiswa.

Baris 45-46: Menampilkan hasil perhitungan total dan rata-rata ke layar.

Baris 48-50: Jika pilihan adalah 4, ubah running = False. Ini akan menghentikan perulangan while di baris 11 pada putaran berikutnya, lalu mencetak "Program selesai."

Baris 52-53: Jika angka yang dimasukkan bukan 1, 2, 3, atau 4, program akan memberikan peringatan bahwa pilihan tidak tersedia.

Baris 55-56: Merupakan standar Python untuk memastikan fungsi main() hanya dijalankan jika file ini dieksekusi secara langsung (bukan diimpor oleh file lain).

**Ouput program:**
<img width="441" height="40" alt="Image" src="https://github.com/user-attachments/assets/010ab2a3-8d66-451e-91a5-47aa5200cdff" />
Output ini muncul saat pertama kali program dijalankan. Program meminta user menentukan kapasitas data. Pada tahap ini, variabel n diisi melalui input user untuk menentukan berapa banyak jumlah mahasiswa yang akan diproses datanya dalam program ini.

<img width="474" height="114" alt="Image" src="https://github.com/user-attachments/assets/4c7fcd42-119e-4457-bb47-060bebcd60cd" />
Setelah kuota ditentukan, program menampilkan pilihan kepada user. Output ini berasal dari pemanggilan fungsi menu(). Terdapat empat opsi utama yang bisa dipilih dengan memasukkan angka 1 sampai 4 pada bagian "Pilihan (1-4):".

<img width="467" height="157" alt="Image" src="https://github.com/user-attachments/assets/98c351c1-07d5-4574-a6ec-7b60a1dffac6" />
Ketika user memasukkan angka 1, program menampilkan informasi jumlah mahasiswa yang telah ditentukan sebelumnya. Berdasarkan output tersebut, diketahui bahwa user telah memasukkan 3 sebagai kuota, sehingga program menampilkan pesan "Jumlah Kuota Mahasiswa adalah 3 orang". Setelah itu, program akan mengulang kembali menampilkan pilihan kepada user.

<img width="476" height="217" alt="Image" src="https://github.com/user-attachments/assets/6e21f140-d9f3-4ad6-aa64-611c8867cc2e" />
Ketika user memasukkan angka 2, program akan menampilkan nilai mahasiswa. Berdasarkan output tersebut, diketahui bahwa nilai mahasiswa masih 0 karena belum ada input dari user.

<img width="449" height="77" alt="Image" src="https://github.com/user-attachments/assets/05b31524-4b05-4628-9296-82664109fbef" />
Output ini muncul saat user memasukkan angka 3. Program mulai masuk ke dalam siklus pengisian data. Pesan "Masukkan nilai mahasiswa:" menandakan program siap menerima input nilai secara berurutan mulai dari mahasiswa pertama.

<img width="493" height="262" alt="Image" src="https://github.com/user-attachments/assets/52a7c59b-0ac2-4453-9346-ba8c73f872aa" />
Setelah user selesai memasukkan semua nilai (seperti pada gambar: 90, 85, dan 95), program melakukan pemrosesan data. Output ini menampilkan:

Total nilai mahasiswa: Penjumlahan seluruh nilai yang diinput (270.0).

Rata-Rata nilai mahasiswa: Hasil pembagian total nilai dengan jumlah kuota (90.0).
Setelah hasil ditampilkan, program kembali memunculkan menu utama karena variabel running masih bernilai True.

<img width="494" height="72" alt="Image" src="https://github.com/user-attachments/assets/62f5b94d-4fcc-4fba-9f46-0ea8efba61d8" />
Namun, saat user memasukkan nilai lebih dari 100, program akan mengeluarkan pemberitahuan "Nilai tidak valid!" dan akan meminta user menginputkan nilai kembali ke mahasiswa yang sama.

<img width="192" height="52" alt="Image" src="https://github.com/user-attachments/assets/14e4c75c-41cf-47e5-914d-cc84611923e9" />
Output ini adalah tahap akhir dari program. Ketika pengguna memasukkan angka 4, program menjalankan logika untuk mengubah status perulangan menjadi berhenti. Pesan "Program selesai." menandakan bahwa aplikasi telah ditutup secara normal dan tidak ada lagi proses yang berjalan.


**Link Youtube:**
