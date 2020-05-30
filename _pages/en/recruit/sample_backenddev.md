---
layout: default
title: Back-End Sample Exams
lang: en
description: Take-home Exam
---



[Apply Now]({{ site.job_form_url }}){: .btn#page-btn}{:target="_blank"}
[View Instructions]({{ site.baseurl }}/{{ page.lang }}/recruit/webdev.html){: .btn#page-btn}
[View Rubric]({{ site.baseurl }}/{{ page.lang }}/recruit/exam_rubric.html){: .btn#page-btn}

## Exam

Please build the back-end for a question-and-answer app (Destkop UI mockup below)
* Must use Firebase for back-end.

### Desktop UI

<img src='https://lh3.googleusercontent.com/SBQWfwg0cfPBcIyvuK1qAlIX3F3t25vj6uOVahV-E7Rhg-RTKJABufr4rYEHkLd3Cv35n3isUWyFwdEHMeIfsoQ3yDlKKqdhuWvSTz0JuAn3U92Y0nZ_7aC-_raJ9QdxmISoLb0GMw=w1417' />

## Requirements

1. Must have an extremely simple front-end to test your back-end functions.
	1. Can be HTML/CSS.
	1. No need to use any fancy frameworks for front-end placeholder. You will not be graded on front-end.
1. **Must host your back-end on Firebase.**
	1. This is a not a front-end exam. Client side should only be to test your back-end functions.

## Reminders

> * Develop a few features well is better than many features poorly.
> * Please upload your code to GitHub/GitLab.
> * At 2.5-hour:
>   * Please submit what you've completed, regardless of whether you've finished or not.
>   * Launch to host your live site.
	* Submit demo site URL.
>	* Make sure to complete this [Exam Submission Form]({{ site.exam_submit_form_url }}).

## Features Rubric

| Score | Feature |
| --- | --- |
| 90 | Sending Email (mandatory) |
| 45 | Question DB |
| 70 | Query DB |
| 35 | Google OAuth and User DB |
| 60 | Track User Answer and Accuracy |

[View Exam Rubric]({{ site.baseurl }}/{{ page.lang }}/recruit/exam_rubric.html){: .btn#page-btn}

## Features List

Choose any of the following features to implement. There is no required ordering.

### 1. Sending Email (mandatory)
* This question is required for all full-stack and back-end test takers.
* Please develop a simple send email message function, so that users can fill out a form on the webpage and send the text message in the text fields to hr@avancevl.com
* Use [Node Mailer](https://nodemailer.com/usage/){:target="_blank"} or [SMTP JS](https://www.smtpjs.com/){:target="_blank"}
* Develop a simple form that allows users to fill out some messages.
* 2 user-input text fields: subject and body (refer to the topic and content fields of a similiar front-end sample image).
* A simple send message button.
* The front-end UI is simple. The design does not count, because it is a full-stack/back-end exam; it only has to be functional.
* Our test-passing criterion is whether the message written by user will be successfully emailed to hr@avancevl.com.

<img src='https://lh3.googleusercontent.com/FJZRudzsGLDYNQWxezcyzyJHhg7hCVyr7S_7BNwE_LBsahceanzWVnvewnWn_TVbCutBtIVpAJmegz6y5SUOxyfBLBaxFOMLfG74Va8s8CeVZ-ZgOQoEXJv_flH1EW2Yz61l9Mrp9A=w400' />

### 2. Question DB

* Populate Firebase DB with [Google Sheet](https://docs.google.com/spreadsheets/d/1EmWraWzyvxt7km7MiPxU6PDTXzy05_jUyvwUqHc5nP0/edit?usp=sharing){:target="_blank"}
* Store and display `question_text` for each question.
* Store and display `question_title` for each question.
* Store and display all `hashtags` for each question.
* Store and use `/problem/<question_id>` in routing URL.

### 3. Query DB

* Use Firebase Queries to query Question DB using hashtags.
* Build very simple front-end selection boxes to build filter/search URL.
* Map search URL to Firebase Query.
* Return problems that match any hashtags in our search URL.
* Display total number of questions that satisfy filter conditions, out of total possible available questions in DB.

<img src='https://lh3.googleusercontent.com/zeYaUx3W0Hb8yaiPLHyzTOI_ShGmEIQqTA_Q7b8hyGZ_bfeC8gSK4s6L1okbGhrFPf817zjp-RbRcDZzZ3p51Vv1QxUza9RGTDupaia0jRcepHtTUNAafjEXJBwhzKMnVC_az-nOAw=w370' />

### 4. Google OAuth and User DB

* Implement Google OAuth and user database in Firebase.
* Store and display user name and email in a separate simple webpage.
* Use `/user/<user_id>` in routing URL.

### 5. Track User Answer and Accuracy

* Create simple input box for user to input answer to each question.
* Use the `answer` column to determine if question answered correctly.
* Update the following metrics for each user and display in client side.
	* **Accuracy.** Number of problems correct divided by number of problems completed.
	* **Completed.** Total number of problems completed.
	* **Correct.** Total number of problems correct.

<img src='https://lh3.googleusercontent.com/zRIxNrIztI22WJYDs4EcrjnciyQ2ByIRVSu6R-JCpBCo0e2hT9_g1RwdcBbmyaSebQRUk06NscQ6waV0eiQZ1HTBjcVSg6Ildeo-sc9qhFLRnx1tKgK0u8tlKD0eyMMgMwNWp0cS4A=w260' />