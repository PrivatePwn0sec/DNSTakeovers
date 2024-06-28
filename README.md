# DNSTakeovers

DNSTake adalah alat otomatis yang cepat dan canggih untuk memeriksa zona DNS yang hilang yang dapat menyebabkan pengambilalihan subdomain. Kerentanan pengambilalihan DNS terjadi ketika subdomain atau domain memiliki nameserver otoritatif yang disetel ke penyedia (misalnya, AWS Route 53, Akamai, Microsoft Azure, dll.), tetapi zona yang dihosting telah dihapus atau dihapus. Akibatnya, ketika melakukan permintaan untuk catatan DNS, server merespons dengan kesalahan SERVFAIL. Ini memungkinkan penyerang untuk membuat zona yang dihosting yang hilang pada layanan yang digunakan dan dengan demikian mengontrol semua catatan DNS untuk (sub)domain tersebut.

## Fitur

- **Pemeriksaan Subdomain:** Memeriksa subdomain untuk kerentanan pengambilalihan DNS.
- **Penyedia DNS Umum:** Mendukung berbagai penyedia DNS umum seperti AWS, Azure, Google, Akamai, dan Cloudflare.
- **Pemrosesan Batch:** Memeriksa beberapa subdomain secara bersamaan.
- **Penyimpanan Hasil:** Menyimpan hasil pemeriksaan ke dalam file.
- **Email Notifikasi:** Mengirimkan notifikasi melalui email jika ditemukan kerentanan.
- **Log Aktivitas:** Mencatat semua aktivitas pemeriksaan untuk audit dan analisis.
- **Integrasi API:** Integrasi dengan API untuk memperluas fungsionalitas.

## Teknologi yang Digunakan

- **Bahasa Pemrograman:** Python 3.x
- **Modul Python:** `requests`, `dnspython`, `smtplib`, `logging`, `json`

## Cara Menggunakan

### 1. Instalasi Modul yang Dibutuhkan

Pastikan Anda telah menginstal Python 3.x. Anda dapat menginstal modul yang dibutuhkan dengan perintah berikut:
```bash
pip install requests dnspython
```
### 2.  Menjalankan Alat DNSTakeovers
Jalankan alat ini dari command line dengan perintah berikut:
```
python dnstake.py subdomain.example.com
```
Untuk pemeriksaan batch:
```
python dnstake.py --batch subdomains.txt
```
Untuk menyimpan hasil ke dalam file:
```
python dnstake.py subdomain.example.com --output hasil.json
```
Untuk mengirim notifikasi email jika ditemukan kerentanan:
```
python dnstake.py subdomain.example.com --email your_email@example.com
```
### Hasil
 * Jika subdomain rentan terhadap pengambilalihan DNS, Anda akan melihat pesan yang menunjukkan bahwa subdomain tersebut rentan dan email notifikasi akan dikirim jika opsi email digunakan.
 * Jika tidak rentan, Anda akan melihat pesan yang menunjukkan bahwa subdomain tidak rentan.

### Catatan

 * Alat ini bertujuan untuk membantu administrator sistem dan peneliti keamanan dalam mengidentifikasi potensi kerentanan DNS takeover pada subdomain server.
 * Penggunaan alat ini harus dilakukan secara etis dan hanya pada domain yang Anda miliki atau Anda memiliki izin untuk mengujinya.

 