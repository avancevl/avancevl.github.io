---
layout: default
title: 后端测验样本
lang: zh-cn
description: 后端测验样本
---



[立即申请]({{ site.job_form_url_zh-cn }}){: .btn#page-btn}{:target="_blank"}
[检阅考试指示]({{ site.baseurl }}/{{ page.lang }}/recruit/webdev.html){: .btn#page-btn}
[测验分数评估]({{ site.baseurl }}/{{ page.lang }}/recruit/exam_rubric.html){: .btn#page-btn}

## 考试

请实作一下网页画面的后端（以下桌面介面)
* 为了省时间，请用Firebase实作后端

### 桌面介面

<img src='https://lh3.googleusercontent.com/SBQWfwg0cfPBcIyvuK1qAlIX3F3t25vj6uOVahV-E7Rhg-RTKJABufr4rYEHkLd3Cv35n3isUWyFwdEHMeIfsoQ3yDlKKqdhuWvSTz0JuAn3U92Y0nZ_7aC-_raJ9QdxmISoLb0GMw=w1417' />

## 需求规范

1. 必实作非常简单
1. 简单HTML/CSS也行。
1. 不需用任何前端架构。您的前端完全不会影响考试分数。
1. **后端必须上架在Firebase**
1. 这不是前端考试。任何前端的目的只是在测后端。

## 重要提醒

> * 我们并不期望你完整开发每个功能。重点不是要全部 “做完”，是要查看有尝试部分的能力、进度，尽力而为就可以。
> * 请使用 GitHub/GitLab.
> * 这份线上测验分数会决定您的职级与薪资范围。每个网页功能有分数。请必定要交卷。
> * 2.5小时到时：
> * 有开发多少，就交卷多少，考试并没有所谓的 “完成”。
> * 请必定要上架，并提供网页 URL.
> * 请填写测验完成表格 [Exam Submission Form]({{ site.exam_submit_form_url }}).

## 考题大纲


| 满分 | 网页功能 |
| --- | --- |
| 90 | 寄 Email 电子邮件 (必答题) |
| 45 | 题目资料库 |
| 70 | 寻找题目 |
| 35 | Google OAuth登入及使用者资料库 |
| 60 | 使用者答案及题目结果 |

[测验分数评估]({{ site.baseurl }}/{{ page.lang }}/recruit/exam_rubric.html){: .btn#page-btn}

## 网页功能

请以下表单选任网页功能实作，不用照顺序。

### 1. 寄 Email 电子邮件 (必答题) 
* 这题是考全、后端的必答题。
* 请开发一个简单的 send email message 功能，让使用者可以在网页上填写一个表格，并发送栏位里面的文字讯息到 hr@avancevl.com
* 使用 [Node Mailer](https://nodemailer.com/usage/){:target="_blank"} 或 [SMTP JS](https://www.smtpjs.com/){:target="_blank"}
* 简单开发一个让 user 可以填写讯息的表格。
* 需要 2 个文字栏位：subject 和 body (请参考前端类似的样本图片的 topic 和 content 栏位)。
* 一个简单的发送讯息按钮。
* 前端的 UI 简单、可以用就可以，不算分，因为是后端的功能。
* 我们测试的标准是 user 写的 message 是否会成功的寄 email 到 hr@avancevl.com 信箱里。

<img src='https://lh3.googleusercontent.com/FJZRudzsGLDYNQWxezcyzyJHhg7hCVyr7S_7BNwE_LBsahceanzWVnvewnWn_TVbCutBtIVpAJmegz6y5SUOxyfBLBaxFOMLfG74Va8s8CeVZ-ZgOQoEXJv_flH1EW2Yz61l9Mrp9A=w400' />

### 2. 题目资料库

* 把[Google Sheet](https://docs.google.com/spreadsheets/d/1EmWraWzyvxt7km7MiPxU6PDTXzy05_jUyvwUqHc5nP0/edit?usp=sharing){:target="_blank"}的资料输入到Firebase资料库。
* 每一题目，`question_text`栏位输入到资料库及显示在网页。
* 每一题目，`question_title`栏位输入到资料库及显示在网页。
* 每一题目，`hashtags`栏位输入到资料库及显示在网页。
* 每一题目，用`/problem/<question_id>`在routing网址。

### 3. 寻找题目

* 使用Firebase Queries及hashtags来query资料库。
* 在前端实作简单的选项单，造query后端的URL。
* 把query后端URL跟Firebase资料库接起来。
* 把后端回覆的资料结果显示在网页。
* 在网页显示几个结果的总数量。

<img src='https://lh3.googleusercontent.com/zeYaUx3W0Hb8yaiPLHyzTOI_ShGmEIQqTA_Q7b8hyGZ_bfeC8gSK4s6L1okbGhrFPf817zjp-RbRcDZzZ3p51Vv1QxUza9RGTDupaia0jRcepHtTUNAafjEXJBwhzKMnVC_az-nOAw=w370' />

### 4. Google OAuth登入及使用者资料库

* 实作Google OAuth及使用者资料库。
* 把Google使用者的名称及电子邮件网址存在资料库及显示在另张User Profile网页。
* User Profile请用`/user/<user_id>`的routing网址

### 5. 使用者答案及题目结果

* 建立简单的input box给使用者输入题目答案。
* 跟资料库里的`answer`栏位对使用者答案是对还是错。
* 纪录每位使用者对几题，错几题，准确率。
* **准确率。 **
* **总共实作集体。 **
* **对几题。 **

<img src='https://lh3.googleusercontent.com/zRIxNrIztI22WJYDs4EcrjnciyQ2ByIRVSu6R-JCpBCo0e2hT9_g1RwdcBbmyaSebQRUk06NscQ6waV0eiQZ1HTBjcVSg6Ildeo-sc9qhFLRnx1tKgK0u8tlKD0eyMMgMwNWp0cS4A=w260' />

<br>

