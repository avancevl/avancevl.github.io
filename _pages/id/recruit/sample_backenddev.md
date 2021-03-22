---
layout: default
title: Contoh Ujian Back-End
lang: id
description: Ujian Bawa Pulang
---



[Daftar Sekarang]({{ site.job_form_url_en }}){: .btn#page-btn}{:target="\_blank"}
[Lihat Instruksi]({{ site.baseurl }}/{{ page.lang }}/recruit/webdev.html){: .btn#page-btn}
[Lihat Rubrik]({{ site.baseurl }}/{{ page.lang }}/recruit/exam_rubric.html){: .btn#page-btn}

## Ujian

Harap buat back-end untuk aplikasi tanya jawab (mockup UI Desktop di bawah)

- Harus menggunakan Firebase untuk back-end.

### UI Desktop

<img src='https://lh3.googleusercontent.com/SBQWfwg0cfPBcIyvuK1qAlIX3F3t25vj6uOVahV-E7Rhg-RTKJABufr4rYEHkLd3Cv35n3isUWyFwdEHMeIfsoQ3yDlKKqdhuWvSTz0JuAn3U92Y0nZ_7aC-_raJ9QdxmISoLb0GMw=w1417' />

## Persyaratan

1. Harus memiliki front-end yang sangat sederhana untuk menguji fungsi back-end Anda.
1. Bisa HTML / CSS.
1. Tidak perlu menggunakan kerangka kerja mewah apa pun untuk placeholder front-end. Anda tidak akan dinilai di bagian depan.
1. **Harus menghosting back-end Anda di Firebase.**
1. Ini bukan ujian front-end. Sisi klien seharusnya hanya untuk menguji fungsi back-end Anda.

## Pengingat

> - Mengembangkan beberapa fitur dengan baik lebih baik daripada banyak fitur dengan buruk.
> - Harap unggah kode Anda ke GitHub / GitLab.
> - Pada 2,5 jam:
>   - Harap kirimkan apa yang telah Anda selesaikan, terlepas dari apakah Anda telah menyelesaikan atau belum.
>   - Luncurkan untuk menghosting situs langsung Anda.

- Kirimkan URL situs demo.
  > - Pastikan untuk melengkapi [Formulir Pengiriman Ujian] ({{ site.exam_submit_form_url }}).

## Menampilkan Rubrik

| Skor | Fiture                            |
| ---- | --------------------------------- |
| 90   | Mengirim Email (wajib)            |
| 45   | Pertanyaan DB                     |
| 70   | Kueri DB                          |
| 35   | Google OAuth and User DB          |
| 60   | Lack Jawaban dan Akurasi Pengguna |

[Lihat Rubrik Ujian]({{ site.baseurl }}/{{ page.lang }}/recruit/exam_rubric.html){: .btn#page-btn}

## Daftar Fiture

Pilih salah satu fitur berikut untuk diterapkan. Tidak perlu urut.

### 1. Mengirim Email (wajib)

- Pertanyaan ini diperlukan untuk semua peserta tes full-stack dan back-end.
- Harap kembangkan fungsi kirim pesan email sederhana, sehingga pengguna dapat mengisi formulir di halaman web dan mengirim pesan teks di bidang teks ke hr@avancevl.com
- Gunakan [Node Mailer](https://nodemailer.com/usage/){:target="\_blank"} atau [SMTP JS](https://www.smtpjs.com/){:target="\_blank"}
- Kembangkan formulir sederhana yang memungkinkan pengguna mengisi beberapa pesan.
- 2 bidang teks masukan pengguna: subjek dan isi (merujuk ke bidang topik dan konten dari gambar contoh front-end serupa).
- Tombol kirim pesan sederhana.
- Antarmuka antarmuka sederhana. Desain tidak dihitung, karena ini adalah ujian full-stack / back-end; itu hanya harus berfungsi.
- Kriteria kelulusan tes kami adalah apakah pesan yang ditulis oleh pengguna akan berhasil dikirim melalui email ke hr@avancevl.com.

<img src='https://lh3.googleusercontent.com/FJZRudzsGLDYNQWxezcyzyJHhg7hCVyr7S_7BNwE_LBsahceanzWVnvewnWn_TVbCutBtIVpAJmegz6y5SUOxyfBLBaxFOMLfG74Va8s8CeVZ-ZgOQoEXJv_flH1EW2Yz61l9Mrp9A=w400' />

### 2. Pertanyaan DB

- Isi Firebase DB dengan [Google Sheet](https://docs.google.com/spreadsheets/d/1EmWraWzyvxt7km7MiPxU6PDTXzy05_jUyvwUqHc5nP0/edit?usp=sharing){:target="\_blank"}
- Simpan dan tampilkan `question_text` untuk setiap pertanyaan
- Simpan dan tampilkan `question_title` untuk setiap pertanyaan.
- Simpan dan tampilkan semua `hashtag` untuk setiap pertanyaan.
- Simpan dan gunakan `/ problem / <question_id>` di URL perutean.

### 3. Kueri DB

- Gunakan Firebase Queries untuk menanyakan DB Pertanyaan menggunakan hashtag.
- Buat kotak pilihan front-end yang sangat sederhana untuk membuat filter / URL pencarian.
- Petakan URL penelusuran ke Firebase Query.
- Kembalikan masalah yang cocok dengan hashtag apa pun di URL pencarian kami.
- Menampilkan jumlah total pertanyaan yang memenuhi kondisi filter, dari total kemungkinan pertanyaan yang tersedia di DB.

<img src='https://lh3.googleusercontent.com/zeYaUx3W0Hb8yaiPLHyzTOI_ShGmEIQqTA_Q7b8hyGZ_bfeC8gSK4s6L1okbGhrFPf817zjp-RbRcDZzZ3p51Vv1QxUza9RGTDupaia0jRcepHtTUNAafjEXJBwhzKMnVC_az-nOAw=w370' />

### 4. Google OAuth dan User DB

- Terapkan Google OAuth dan database pengguna di Firebase.
- Simpan dan tampilkan nama pengguna dan email di halaman web sederhana yang terpisah.
- Gunakan `/ user / <user_id>` dalam perutean URL.

### 5. Lacak Jawaban dan Akurasi Pengguna

- Buat kotak input sederhana bagi pengguna untuk memasukkan jawaban untuk setiap pertanyaan.
- Gunakan kolom `jawaban` untuk menentukan apakah pertanyaan dijawab dengan benar.
- Perbarui metrik berikut untuk setiap pengguna dan tampilkan di sisi klien.
  - **Akurasi.** Jumlah soal yang benar dibagi jumlah soal yang diselesaikan.
  - **Selesai.** Jumlah total masalah yang diselesaikan.
  - **Benar.** Jumlah masalah yang benar.

<img src='https://lh3.googleusercontent.com/zRIxNrIztI22WJYDs4EcrjnciyQ2ByIRVSu6R-JCpBCo0e2hT9_g1RwdcBbmyaSebQRUk06NscQ6waV0eiQZ1HTBjcVSg6Ildeo-sc9qhFLRnx1tKgK0u8tlKD0eyMMgMwNWp0cS4A=w260' />