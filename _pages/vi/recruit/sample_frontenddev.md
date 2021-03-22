---
layout: default
title: Front-End Sample Exam
lang: vi
description: Take-Home
---



<br>

[Apply Now]({{ site.job_form_url_en }}){: .btn#page-btn}{:target="\_blank"}
[View Instructions]({{ site.baseurl }}/{{ page.lang }}/recruit/webdev.html){: .btn#page-btn}
[View Rubric]({{ site.baseurl }}/{{ page.lang }}/recruit/exam_rubric.html){: .btn#page-btn}

## Exam

Please build a **pixel-perfect** interactive desktop and mobile browser front-end of the following design mockups.

- Must use **React.js, Flexbox, and a React UI component library framework.**
- Host as static pages (no back-end) on **Firebase** or alternative free solution.

### Desktop UI

<img src='https://lh3.googleusercontent.com/SBQWfwg0cfPBcIyvuK1qAlIX3F3t25vj6uOVahV-E7Rhg-RTKJABufr4rYEHkLd3Cv35n3isUWyFwdEHMeIfsoQ3yDlKKqdhuWvSTz0JuAn3U92Y0nZ_7aC-_raJ9QdxmISoLb0GMw=w1417' />

### Mobile UI

<img src='https://lh3.googleusercontent.com/d7JgqvyPNjQOZEZEoVyTMJcAHRnBTDIZDDJo9rjbIVU-dLiQ2SYOacqNqheAbNkK_A1DBHQS-7qNwkaAb4fvgUa-bx4pJcUOjS0lKGpcK0Dm32KjXLzy_M9yjVwkd1gopwESZau8iw=w308' />

## Requirements

1. **RWD.** Responsive Web Design for both mobile and web.
1. Must use **JavaScript.**
1. Must use **React.js.**
1. Must use **CSS Flexbox**
1. Must use a **React UI framework** from this list:
1. Material UI
1. Semantic UI
1. React Bootstrap
1. React Toolbox
1. Elemental UI
1. **Must host your site as a live static page.**
1. Please use a free hosting service like Heroku, Firebase, ZEIT, or Netilfy to host your site as a live static page.
1. This is a not a back-end exam. The web page interactions should all be client side.

## Reminders

> - We'd rather you do a few features well, rather than all the features poorly.
> - Please be sure to upload code to GitHub/GitLab.
> - At the 2.5-hour mark:
>   - Please submit however much you've completed, regardless of whether you've finished or not.
>   - Make sure your site is live, and submit URL.
> - Make sure to complete [Exam Submission Form]({{ site.exam_submit_form_url }}).

## Features Rubric

1. Pixel perfect on:
1. Desktop (Chrome)
1. Mobile (Android, iOS)
1. Fill in gaps not in the design mockups in a polished manner
1. Effects
1. Hover
1. Selection
1. Disable
1. Keyboard and mouse events

| Score | Feature                                                        |
| ----- | -------------------------------------------------------------- |
| 50    | Numbers Entry Box                                              |
| 50    | Radial Chart and Stats Pane                                    |
| 60    | Search Filters and Dropdown Menu (20 pts per type of selector) |
| 40    | Main Pane and Hashtags                                         |

[View Exam Rubric]({{ site.baseurl }}/{{ page.lang }}/recruit/exam_rubric.html){: .btn#page-btn}

## Features List

Choose any of the following features to implement. There are no required ordering.

### 1. Numbers Entry Box

- Only numbers (0-9), period (.), and backslash (/) allowed in the numbers box.
- Right and left arrows disable for numbers box.
- Clicking disabled for numbers box.
- Keyboard is automatically in focus on the numbers box on page load. No need to click on numbers box to bring it in focus.
- "Press Enter" text and "Submit" button becomes enabled only when numbers are entered into numbers box.

<img src='https://lh3.googleusercontent.com/ox5SLTTaUphHmgJiyjktWSEvtiw14pCxqL151hVq27BQbfuc2ur7X5B0UoFnIUwI6tGlxbKCD8WyGG1iszRx1h3JJBDDl9fFYEh2UXDIALI4JpIMmf24qqghg27Kp4hkt2Ed9qFUcQ=w386' />

<img src='https://lh3.googleusercontent.com/rB8z7QO1lzjB2QjQBmrjg1B9-hOkowQUVVwG-jHCGgqIWe-KFQ4dSkYWwYJvrZYOo9oPwr4Vd5PyW1oxF316LsNqys1Nw-Q8iXab-y5wBRoMthow3P_1ycTyt45RjouxjCUrH5QLTQ=w386' />

### 2. Radial Chart and Stats Pane

- Pixel perfect desktop and mobile
- Not a static image, but real chart that could update if page is connected to server side.

#### Desktop UI

<img src='https://lh3.googleusercontent.com/zRIxNrIztI22WJYDs4EcrjnciyQ2ByIRVSu6R-JCpBCo0e2hT9_g1RwdcBbmyaSebQRUk06NscQ6waV0eiQZ1HTBjcVSg6Ildeo-sc9qhFLRnx1tKgK0u8tlKD0eyMMgMwNWp0cS4A=w260' />

#### Mobile UI

<img src='https://lh3.googleusercontent.com/KgF-3-t90xkaH0efRhGiskSRs-lXZhbwQNtvL2GRiWiw76Os7hmvNe4T8kqSlbxNVDmqpUKDLPeODxVZk5P6yTqTiFYxqamU0GogSxARSAKaBy_lmLHnWNdgjw4oURMaxW5G4KBOtg=w358' />

### 3. Search Filters and Dropdown Menu

- Pixel perfect desktop and mobile
- 3 types of filters
  - Simple Selector
  - Multiple Selector
  - Checkboxes

#### Simple Selector

<img src='https://lh3.googleusercontent.com/_Yq-Q8WnX2cV3y305Q4GbHNuugYC173fCTPixp3aigX7ZxKyf5ok1nRGoCQ1-ProqM2GNGr3VI0CyBTCkHCuSpie3yH8vGgY9AqfqRk6PL7Hx7fRf2QDpQoisxPgCQNwt5Jlzl3X4w=w288' />

<img src='https://lh3.googleusercontent.com/nclQ6N-I6LaATouvMOo2bFDGud5yWOteWi1uGUpWg-1rKdHo4yJGm5o-YiDERAMyi-Vm3ayJ48XavVloBfnKB7nInGjqN5ElQApx7f9e0dr3VrYusCoDLndZvHzzxikn29f6I3bqaw=w374' />

#### Multiple Selector

<img src='https://lh3.googleusercontent.com/zeYaUx3W0Hb8yaiPLHyzTOI_ShGmEIQqTA_Q7b8hyGZ_bfeC8gSK4s6L1okbGhrFPf817zjp-RbRcDZzZ3p51Vv1QxUza9RGTDupaia0jRcepHtTUNAafjEXJBwhzKMnVC_az-nOAw=w370' />

<img src='https://lh3.googleusercontent.com/4YZ6BQyxTr0RiPlGIyASjeaO_M8B_Vv-pgTFn6yG2b_aGa8Fdvrwyru534ZnoeE_rG3Z5NPuZRKifDqvTYA51I0hkXYxO9Ga4VWjnB1uj8Z4R0jd-Ofha1no2LAaGXmmeutLMlcgJQ=w378' />

#### Checkbox Selector

<img src='https://lh3.googleusercontent.com/YhLAUXhAFGxs5GlJMv-HZB3i9Gji9TCU3RS8lxlrpKoGOyyBfT_xyEtM71a6hENCzCei1ZHsHSEtRWqLtnZsVgEOR-dFXQ1zmb9ysYYjsaKjuSsbpwagENtwmzcSiwvIXuc0Es2kSA=w379' />

<img src='https://lh3.googleusercontent.com/8HvHKaJr974UaC8OcbBfsL-VJGIELAvEmnGJBucCbLHK3kTvIdUXIErRK2yYn62YkVyC_k2dW-22w3SbyCM-hDXKNvQlntZzhw4MrlJqhrAXLfjGCR8qkJvOU6KLTz4cLiQizWp_Fw=w376' />

### 4. Main Pane and Hashtags

- Pixel perfect desktop and mobile

#### Destkop UI

<img src='https://lh3.googleusercontent.com/qwkODECKDvngf-i79qFqv83ecp5n2Bc0oYhJ2SWy1eaboJV8LE3GJTj-nr76GDRNwyKD0-Lob2K4r55SPHtIbbK3H3md-A_u1CoZ2aQ0cg7OTE55SaqrSblx_XZOJ-L4F5XuxsAKwQ=w443' />

#### Mobile UI

<img src='https://lh3.googleusercontent.com/wcVF6A927hu43l1qtovepnmX-q7eQLjqwDfFSKnhqyl9mssrHnGKfdF3DzFk-HwJfybf1YVpSLqfk5SaYV6qtIMeivjkDiNiXJZltYqu3543svDGmjOHVaMw8R8KqAawvgm9oREf6A=w310' />

<br>

