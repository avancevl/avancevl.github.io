---
layout: default
title: 後端測驗樣本
lang: zh-tw
description: 後端測驗樣本
---



[立即申請]({{ site.job_form_url_zh-tw }}){: .btn#page-btn}{:target="\_blank"}
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

