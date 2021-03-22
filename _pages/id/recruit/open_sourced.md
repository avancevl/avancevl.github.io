---
layout: default
title: Kontribusi Sumber Terbuka
lang: id
description: Lihat apa yang bisa dilakukan Jekyl.
---



## Panggilan untuk Fitur

Berkontribusi pada upaya kami untuk membuka sumber cara perusahaan kami dijalankan dengan menerapkan fitur-fitur keren Jekyll di bawah ini.

* Diketahui oleh HR kami dan percepat proses wawancara Anda.
* Berkontribusi pada Open Source [Jekyll komunitas](https://jekyllrb.com/){:target="_blank"}.
* Bangun portofolio dan kehadiran GitHub Anda
* Dapatkan pengakuan dengan berteriak.

<br>

[Fork GitHub](https://github.com/avancevl/avl.github.io){: .btn#page-btn}{:target="_blank"}.

### Fitur 1. Perbaiki Terjemahan dan Salah Ketik Mandarin

Bahasa Cina adalah bahasa kedua kami, jadi tentu saja akan ada banyak kesalahan ketik, salah terjemahan. Kami berkomitmen untuk lingkungan dwibahasa, jadi kami berterima kasih atas kontribusi apa pun di bidang ini.

### Fitur 2. Dimana Saya?

Kami ingin memiliki bilah navigasi kecil di bagian atas setiap halaman untuk menunjukkan di mana pengguna saat ini berada di pohon navigasi, mirip dengan gambar di bawah.

> Kamu di sini: **徵才 Recruiting** > **職缺 Open Positions** > *全端軟體工程師 Full Stack Developer*

Bilah navigasi harus memudahkan navigasi satu tingkat ke atas dan ke bawah pohon.

### Manajemen Mudah dan Beralih antara Beberapa Halaman

Untuk tetap setia pada komitmen kami sebagai perusahaan dwibahasa Inggris-Mandarin, kami perlu memiliki halaman GitHub versi bahasa Inggris dan Mandarin. Saat ini, kami membagi teks bahasa Inggris dan Mandarin menjadi beberapa bagian terpisah di halaman marketdown yang sama. Idealnya, kita dapat memodifikasi Jekyll untuk mendukung:

1. Mudah beralih antara versi bahasa Mandarin dan Inggris dari halaman yang sama.
1. Manajemen markdown yang mudah, file HTML dalam struktur direktori yang jelas sehingga kami tidak harus secara efektif mempertahankan dua versi dari situs yang sama.

### Fitur 4. Daftar Halaman Anak

Sometimes, for a given page, you just want to be able to list the child pages in the markdown file without expliciting spelling out the URL.

* This can be implemented in HTML-Liquid.
* If we add a new child page to the navigation tree, we should not have to update teh HTML-Liquid in the markdown.

> 職缺 Open Positions
> * 全端軟體工程師 Full Stack Developer
> * 前端軟體工程師 Front End Developer
> * 後端軟體工程師 Back End Developer

### Fitur 5. Sembunyikan Halaman Anak dalam Navigasi

Pohon navigasi peta situs kami semakin panjang dan panjang. Kami ingin semua sub-pohon diciutkan / disembunyikan, kecuali untuk halaman saat ini. Untuk halaman saat ini, menampilkan halaman anak tidak apa-apa.

> * 介紹 Pengantar
> * 公司理念 Prinsip
> * 人資管理 Orang
> * 徵才 Perekrutan
> 	* 職缺 Posisi Terbuka
> 	* 面試過程 Proses Wawancara
> 	* 在家線上考試 Ujian Bawa Pulang
> 	* **開源貢獻 Kontribusi Sumber Terbuka**
> * 工程流程 Teknik

### Fitur 6. Bilah Pencarian

Karena dokumen bersumber terbuka kami semakin banyak, kami memerlukan bilah pencarian untuk membantu karyawan dan calon potensial menavigasi dokumen-dokumen ini.

* Harus mendukung istilah pencarian bahasa Cina dan Inggris.
* Hanya klien, tanpa server.

### Pohon Navigasi Sisi Kiri / Lengket

Saat ini, pohon navigasi ada di bagian bawah halaman kita. Beberapa di antaranya panjang dan membutuhkan banyak pengguliran untuk mencapai pohon. Akan sangat membantu jika memiliki pohon navigasi di sisi kiri halaman. Ini juga tidak boleh bergulir dengan halaman: itu harus tetap (lengket) ke sisi kiri.

<br>

## Bagaimana Berkontribusi

1. Fork repo kami [here](https://github.com/avancevl/avancevl.github.io){:target="_blank"}.
1. Kirimkan permintaan penarikan.
1. Setujui dan digabungkan dalam 1 minggu.

<br>

## Terima kasih khusus

Berteriak dan terima kasih kepada kontributor GitHub kami:
* [0t2 (Jesse)](https://github.com/0t2){:target="_blank"}
* [da21510](https://github.com/da21510){:target="_blank"}