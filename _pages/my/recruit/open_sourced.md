---
layout: default
title: Open Source Contributions
lang: my
description: See what Jekyl can do.
---



## Call for Features

Contribute to our efforts to open source the way our company is run by implementing cool Jekyll features below.

* Get noticed by our HR and expedite your interview process.
* Contribute to the open-sourced [Jekyll community](https://jekyllrb.com/){:target="_blank"}.
* Build up your GitHub portfolio and presence.
* Get recognized with a shout out.

<br>

[Fork GitHub](https://github.com/avancevl/avl.github.io){: .btn#page-btn}{:target="_blank"}.

### Feature 1. Fix Chinese Translation and Typos

Chinese is our second language, so naturally there are going to be a lot of typos, mis-translations. We are committed to a bilingual environment, so we are grateful for any contributions on this front.

### Feature 2. Where Am I?

We would like to have a little navigation bar at the top of each page to show where the current user is in the navigation tree, similar to the screenshot below.

> You are here: **徵才 Recruiting** > **職缺 Open Positions** > *全端軟體工程師 Full Stack Developer*

The navigation bar should make it easy to navigate one level up and down the tree.

### Feature 3. Easy Management and Toggling between Multiple Pages

In order to stay true to our commitment as a English-Chinese bilingual company, we need to have both English and Chinese versions of our GitHub pages. Currently, we are splitting the English and Chinese texts into separate sections on the same marketdown page. Ideally, we can modify Jekyll to support:

1. Easy toggling between Chinese and English versions of the same page.
1. Easy management of markdown, HTML files in a clear directory structure so that we do not have to effectively maintain two versions of the same site.

### Feature 4. List Child Pages

Sometimes, for a given page, you just want to be able to list the child pages in the markdown file without expliciting spelling out the URL.

* This can be implemented in HTML-Liquid.
* If we add a new child page to the navigation tree, we should not have to update teh HTML-Liquid in the markdown.

> 職缺 Open Positions
> * 全端軟體工程師 Full Stack Developer
> * 前端軟體工程師 Front End Developer
> * 後端軟體工程師 Back End Developer

### Feature 5. Hide Child Pages in Navigation

Our site map navigation tree is getting longer and longer. We would like all sub-trees to be collapsed / hidden, except for the current page. For the current page, displaying child pages is OK.

> * 介紹 Introduction
> * 公司理念 Principles
> * 人資管理 People
> * 徵才 Recruiting
> 	* 職缺 Open Positions
> 	* 面試過程 Interview Process
> 	* 在家線上考試 Take-Home Exam
> 	* **開源貢獻 Open Source Contribution**
> * 工程流程 Engineering

### Feature 6. Search Bar

As our open-sourced documents get more and more, we need a search bar to help employees and potential candidates navigate this morass of documents.

* Should support both Chinese and English search terms.
* Client only, server-less.

### Feature 7. Left-Sided/Sticky Navigation Tree

Currently, the navigation tree is at the bottom of our pages. Some of these are long and require much scrolling to reach the tree. It would be helpful to have the navigation tree to the left hand side of the pages. It should also not scroll with the page: it should persist (sticky) onto the left side.

<br>

## How to Contribute

1. Fork our repo [here](https://github.com/avancevl/avancevl.github.io){:target="_blank"}.
1. Submit pull request.
1. Approve and merged within 1 week.

<br>

## Special Thanks

Shout out and thanks to our GitHub contributors:
* [0t2 (Jesse)](https://github.com/0t2){:target="_blank"}
* [da21510](https://github.com/da21510){:target="_blank"}

<br>
