---
layout: default
title: 後端測驗樣本
description: Back-End Sample Exam
locales:
  zh-tw:
    title: 後端測驗樣本
    description: 後端測驗樣本
  zh-cn:
    title: 后端测验样本
    description: 后端测验样本
  en:
    title: Back-End Sample Exams
    description: Take-home Exam
  id:
    title: Contoh Ujian Back-End
    description: Ujian Bawa Pulang
---

<a name="zh-tw"></a>

[立即申請]({{ site.job_form_url }}){: .btn#page-btn}{:target="\_blank"}
[檢閱考試指示]({{ site.baseurl }}/{{ page.lang }}/recruit/webdev.html){: .btn#page-btn}
[測驗分數評估]({{ site.baseurl }}/{{ page.lang }}/recruit/exam_rubric.html){: .btn#page-btn}

## 考試

請實作一下網頁畫面的後端（以下桌面介面)

- 為了省時間，請用 Firebase 實作後端

### 桌面介面

<img src='https://lh3.googleusercontent.com/SBQWfwg0cfPBcIyvuK1qAlIX3F3t25vj6uOVahV-E7Rhg-RTKJABufr4rYEHkLd3Cv35n3isUWyFwdEHMeIfsoQ3yDlKKqdhuWvSTz0JuAn3U92Y0nZ_7aC-_raJ9QdxmISoLb0GMw=w1417' />

## 需求規範

1. 必實作非常簡單
1. 簡單 HTML/CSS 也行。
1. 不需用任何前端架構。您的前端完全不會影響考試分數。
1. **後端必須上架在 Firebase**
1. 這不是前端考試。任何前端的目的只是在測後端。

## 重要提醒

> - 我們並不期望你完整開發每個功能。重點不是要全部 “做完”，是要查看有嘗試部分的能力、進度，盡力而為就可以。
> - 請使用 GitHub/GitLab.
> - 這份線上測驗分數會決定您的職級與薪資範圍。每個網頁功能有分數。請必定要交卷。
> - 2.5 小時到時：
>   - 有開發多少，就交卷多少，考試並沒有所謂的 “完成”。
>   - 請必定要上架，並提供網頁 URL.
> - 請填寫測驗完成表格 [Exam Submission Form]({{ site.exam_submit_form_url }}).

## 考題大綱

| 滿分 | 網頁功能                        |
| ---- | ------------------------------- |
| 90   | 寄 Email 電子郵件 (必答題)      |
| 45   | 題目資料庫                      |
| 70   | 尋找題目                        |
| 35   | Google OAuth 登入及使用者資料庫 |
| 60   | 使用者答案及題目結果            |

[測驗分數評估]({{ site.baseurl }}/{{ page.lang }}/recruit/exam_rubric.html){: .btn#page-btn}

## 網頁功能

請以下表單選任網頁功能實作，不用照順序。

### 1. 寄 Email 電子郵件 (必答題)

- 這題是考全、後端的必答題。
- 請開發一個簡單的 send email message 功能，讓使用者可以在網頁上填寫一個表格，並發送欄位裡面的文字訊息到 hr@avancevl.com
- 使用 [Node Mailer](https://nodemailer.com/usage/){:target="\_blank"} 或 [SMTP JS](https://www.smtpjs.com/){:target="\_blank"}
- 簡單開發一個讓 user 可以填寫訊息的表格。
- 需要 2 個文字欄位：subject 和 body (請參考前端類似的樣本圖片的 topic 和 content 欄位)。
- 一個簡單的發送訊息按鈕。
- 前端的 UI 簡單、可以用就可以，不算分，因為是後端的功能。
- 我們測試的標準是 user 寫的 message 是否會成功的寄 email 到 hr@avancevl.com 信箱裡。

<img src='https://lh3.googleusercontent.com/FJZRudzsGLDYNQWxezcyzyJHhg7hCVyr7S_7BNwE_LBsahceanzWVnvewnWn_TVbCutBtIVpAJmegz6y5SUOxyfBLBaxFOMLfG74Va8s8CeVZ-ZgOQoEXJv_flH1EW2Yz61l9Mrp9A=w400' />

### 2. 題目資料庫

- 把[Google Sheet](https://docs.google.com/spreadsheets/d/1EmWraWzyvxt7km7MiPxU6PDTXzy05_jUyvwUqHc5nP0/edit?usp=sharing){:target="\_blank"}的資料輸入到 Firebase 資料庫。
- 每一題目，`question_text`欄位輸入到資料庫及顯示在網頁。
- 每一題目，`question_title`欄位輸入到資料庫及顯示在網頁。
- 每一題目，`hashtags`欄位輸入到資料庫及顯示在網頁。
- 每一題目，用`/problem/<question_id>`在 routing 網址。

### 3. 尋找題目

- 使用 Firebase Queries 及 hashtags 來 query 資料庫。
- 在前端實作簡單的選項單，造 query 後端的 URL。
- 把 query 後端 URL 跟 Firebase 資料庫接起來。
- 把後端回覆的資料結果顯示在網頁。
- 在網頁顯示幾個結果的總數量。

<img src='https://lh3.googleusercontent.com/zeYaUx3W0Hb8yaiPLHyzTOI_ShGmEIQqTA_Q7b8hyGZ_bfeC8gSK4s6L1okbGhrFPf817zjp-RbRcDZzZ3p51Vv1QxUza9RGTDupaia0jRcepHtTUNAafjEXJBwhzKMnVC_az-nOAw=w370' />

### 4. Google OAuth 登入及使用者資料庫

- 實作 Google OAuth 及使用者資料庫。
- 把 Google 使用者的名稱及電子郵件網址存在資料庫及顯示在另張 User Profile 網頁。
- User Profile 請用`/user/<user_id>`的 routing 網址

### 5. 使用者答案及題目結果

- 建立簡單的 input box 給使用者輸入題目答案。
- 跟資料庫裡的`answer`欄位對使用者答案是對還是錯。
- 紀錄每位使用者對幾題，錯幾題，準確率。
  - **準確率。**
  - **總共實作集體。**
  - **對幾題。**

<img src='https://lh3.googleusercontent.com/zRIxNrIztI22WJYDs4EcrjnciyQ2ByIRVSu6R-JCpBCo0e2hT9_g1RwdcBbmyaSebQRUk06NscQ6waV0eiQZ1HTBjcVSg6Ildeo-sc9qhFLRnx1tKgK0u8tlKD0eyMMgMwNWp0cS4A=w260' />

<br>

<a name="zh-cn"></a>

[立即申请]({{ site.job_form_url }}){: .btn#page-btn}{:target="\_blank"}
[检阅考试指示]({{ site.baseurl }}/{{ page.lang }}/recruit/webdev.html){: .btn#page-btn}
[测验分数评估]({{ site.baseurl }}/{{ page.lang }}/recruit/exam_rubric.html){: .btn#page-btn}

## 考试

请实作一下网页画面的后端（以下桌面介面)

- 为了省时间，请用 Firebase 实作后端

### 桌面介面

<img src='https://lh3.googleusercontent.com/SBQWfwg0cfPBcIyvuK1qAlIX3F3t25vj6uOVahV-E7Rhg-RTKJABufr4rYEHkLd3Cv35n3isUWyFwdEHMeIfsoQ3yDlKKqdhuWvSTz0JuAn3U92Y0nZ_7aC-_raJ9QdxmISoLb0GMw=w1417' />

## 需求规范

1. 必实作非常简单
1. 简单 HTML/CSS 也行。
1. 不需用任何前端架构。您的前端完全不会影响考试分数。
1. **后端必须上架在 Firebase**
1. 这不是前端考试。任何前端的目的只是在测后端。

## 重要提醒

> - 我们并不期望你完整开发每个功能。重点不是要全部 “做完”，是要查看有尝试部分的能力、进度，尽力而为就可以。
> - 请使用 GitHub/GitLab.
> - 这份线上测验分数会决定您的职级与薪资范围。每个网页功能有分数。请必定要交卷。
> - 2.5 小时到时：
> - 有开发多少，就交卷多少，考试并没有所谓的 “完成”。
> - 请必定要上架，并提供网页 URL.
> - 请填写测验完成表格 [Exam Submission Form]({{ site.exam_submit_form_url }}).

## 考题大纲

| 满分 | 网页功能                        |
| ---- | ------------------------------- |
| 90   | 寄 Email 电子邮件 (必答题)      |
| 45   | 题目资料库                      |
| 70   | 寻找题目                        |
| 35   | Google OAuth 登入及使用者资料库 |
| 60   | 使用者答案及题目结果            |

[测验分数评估]({{ site.baseurl }}/{{ page.lang }}/recruit/exam_rubric.html){: .btn#page-btn}

## 网页功能

请以下表单选任网页功能实作，不用照顺序。

### 1. 寄 Email 电子邮件 (必答题)

- 这题是考全、后端的必答题。
- 请开发一个简单的 send email message 功能，让使用者可以在网页上填写一个表格，并发送栏位里面的文字讯息到 hr@avancevl.com
- 使用 [Node Mailer](https://nodemailer.com/usage/){:target="\_blank"} 或 [SMTP JS](https://www.smtpjs.com/){:target="\_blank"}
- 简单开发一个让 user 可以填写讯息的表格。
- 需要 2 个文字栏位：subject 和 body (请参考前端类似的样本图片的 topic 和 content 栏位)。
- 一个简单的发送讯息按钮。
- 前端的 UI 简单、可以用就可以，不算分，因为是后端的功能。
- 我们测试的标准是 user 写的 message 是否会成功的寄 email 到 hr@avancevl.com 信箱里。

<img src='https://lh3.googleusercontent.com/FJZRudzsGLDYNQWxezcyzyJHhg7hCVyr7S_7BNwE_LBsahceanzWVnvewnWn_TVbCutBtIVpAJmegz6y5SUOxyfBLBaxFOMLfG74Va8s8CeVZ-ZgOQoEXJv_flH1EW2Yz61l9Mrp9A=w400' />

### 2. 题目资料库

- 把[Google Sheet](https://docs.google.com/spreadsheets/d/1EmWraWzyvxt7km7MiPxU6PDTXzy05_jUyvwUqHc5nP0/edit?usp=sharing){:target="\_blank"}的资料输入到 Firebase 资料库。
- 每一题目，`question_text`栏位输入到资料库及显示在网页。
- 每一题目，`question_title`栏位输入到资料库及显示在网页。
- 每一题目，`hashtags`栏位输入到资料库及显示在网页。
- 每一题目，用`/problem/<question_id>`在 routing 网址。

### 3. 寻找题目

- 使用 Firebase Queries 及 hashtags 来 query 资料库。
- 在前端实作简单的选项单，造 query 后端的 URL。
- 把 query 后端 URL 跟 Firebase 资料库接起来。
- 把后端回覆的资料结果显示在网页。
- 在网页显示几个结果的总数量。

<img src='https://lh3.googleusercontent.com/zeYaUx3W0Hb8yaiPLHyzTOI_ShGmEIQqTA_Q7b8hyGZ_bfeC8gSK4s6L1okbGhrFPf817zjp-RbRcDZzZ3p51Vv1QxUza9RGTDupaia0jRcepHtTUNAafjEXJBwhzKMnVC_az-nOAw=w370' />

### 4. Google OAuth 登入及使用者资料库

- 实作 Google OAuth 及使用者资料库。
- 把 Google 使用者的名称及电子邮件网址存在资料库及显示在另张 User Profile 网页。
- User Profile 请用`/user/<user_id>`的 routing 网址

### 5. 使用者答案及题目结果

- 建立简单的 input box 给使用者输入题目答案。
- 跟资料库里的`answer`栏位对使用者答案是对还是错。
- 纪录每位使用者对几题，错几题，准确率。
- **准确率。**
- **总共实作集体。**
- **对几题。**

<img src='https://lh3.googleusercontent.com/zRIxNrIztI22WJYDs4EcrjnciyQ2ByIRVSu6R-JCpBCo0e2hT9_g1RwdcBbmyaSebQRUk06NscQ6waV0eiQZ1HTBjcVSg6Ildeo-sc9qhFLRnx1tKgK0u8tlKD0eyMMgMwNWp0cS4A=w260' />

<br>

<a name="en"></a>

[Apply Now]({{ site.job_form_url }}){: .btn#page-btn}{:target="\_blank"}
[View Instructions]({{ site.baseurl }}/{{ page.lang }}/recruit/webdev.html){: .btn#page-btn}
[View Rubric]({{ site.baseurl }}/{{ page.lang }}/recruit/exam_rubric.html){: .btn#page-btn}

## Exam

Please build the back-end for a question-and-answer app (Destkop UI mockup below)

- Must use Firebase for back-end.

### Desktop UI

<img src='https://lh3.googleusercontent.com/SBQWfwg0cfPBcIyvuK1qAlIX3F3t25vj6uOVahV-E7Rhg-RTKJABufr4rYEHkLd3Cv35n3isUWyFwdEHMeIfsoQ3yDlKKqdhuWvSTz0JuAn3U92Y0nZ_7aC-_raJ9QdxmISoLb0GMw=w1417' />

## Requirements

1. Must have an extremely simple front-end to test your back-end functions.
1. Can be HTML/CSS.
1. No need to use any fancy frameworks for front-end placeholder. You will not be graded on front-end.
1. **Must host your back-end on Firebase.**
1. This is a not a front-end exam. Client side should only be to test your back-end functions.

## Reminders

> - Develop a few features well is better than many features poorly.
> - Please upload your code to GitHub/GitLab.
> - At 2.5-hour:
>   - Please submit what you've completed, regardless of whether you've finished or not.
>   - Launch to host your live site.

- Submit demo site URL.
  > - Make sure to complete this [Exam Submission Form]({{ site.exam_submit_form_url }}).

## Features Rubric

| Score | Feature                        |
| ----- | ------------------------------ |
| 90    | Sending Email (mandatory)      |
| 45    | Question DB                    |
| 70    | Query DB                       |
| 35    | Google OAuth and User DB       |
| 60    | Track User Answer and Accuracy |

[View Exam Rubric]({{ site.baseurl }}/{{ page.lang }}/recruit/exam_rubric.html){: .btn#page-btn}

## Features List

Choose any of the following features to implement. There is no required ordering.

### 1. Sending Email (mandatory)

- This question is required for all full-stack and back-end test takers.
- Please develop a simple send email message function, so that users can fill out a form on the webpage and send the text message in the text fields to hr@avancevl.com
- Use [Node Mailer](https://nodemailer.com/usage/){:target="\_blank"} or [SMTP JS](https://www.smtpjs.com/){:target="\_blank"}
- Develop a simple form that allows users to fill out some messages.
- 2 user-input text fields: subject and body (refer to the topic and content fields of a similiar front-end sample image).
- A simple send message button.
- The front-end UI is simple. The design does not count, because it is a full-stack/back-end exam; it only has to be functional.
- Our test-passing criterion is whether the message written by user will be successfully emailed to hr@avancevl.com.

<img src='https://lh3.googleusercontent.com/FJZRudzsGLDYNQWxezcyzyJHhg7hCVyr7S_7BNwE_LBsahceanzWVnvewnWn_TVbCutBtIVpAJmegz6y5SUOxyfBLBaxFOMLfG74Va8s8CeVZ-ZgOQoEXJv_flH1EW2Yz61l9Mrp9A=w400' />

### 2. Question DB

- Populate Firebase DB with [Google Sheet](https://docs.google.com/spreadsheets/d/1EmWraWzyvxt7km7MiPxU6PDTXzy05_jUyvwUqHc5nP0/edit?usp=sharing){:target="\_blank"}
- Store and display `question_text` for each question.
- Store and display `question_title` for each question.
- Store and display all `hashtags` for each question.
- Store and use `/problem/<question_id>` in routing URL.

### 3. Query DB

- Use Firebase Queries to query Question DB using hashtags.
- Build very simple front-end selection boxes to build filter/search URL.
- Map search URL to Firebase Query.
- Return problems that match any hashtags in our search URL.
- Display total number of questions that satisfy filter conditions, out of total possible available questions in DB.

<img src='https://lh3.googleusercontent.com/zeYaUx3W0Hb8yaiPLHyzTOI_ShGmEIQqTA_Q7b8hyGZ_bfeC8gSK4s6L1okbGhrFPf817zjp-RbRcDZzZ3p51Vv1QxUza9RGTDupaia0jRcepHtTUNAafjEXJBwhzKMnVC_az-nOAw=w370' />

### 4. Google OAuth and User DB

- Implement Google OAuth and user database in Firebase.
- Store and display user name and email in a separate simple webpage.
- Use `/user/<user_id>` in routing URL.

### 5. Track User Answer and Accuracy

- Create simple input box for user to input answer to each question.
- Use the `answer` column to determine if question answered correctly.
- Update the following metrics for each user and display in client side.
  - **Accuracy.** Number of problems correct divided by number of problems completed.
  - **Completed.** Total number of problems completed.
  - **Correct.** Total number of problems correct.

<img src='https://lh3.googleusercontent.com/zRIxNrIztI22WJYDs4EcrjnciyQ2ByIRVSu6R-JCpBCo0e2hT9_g1RwdcBbmyaSebQRUk06NscQ6waV0eiQZ1HTBjcVSg6Ildeo-sc9qhFLRnx1tKgK0u8tlKD0eyMMgMwNWp0cS4A=w260' />

<br>

<a name="id"></a>

[Daftar Sekarang]({{ site.job_form_url }}){: .btn#page-btn}{:target="\_blank"}
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
