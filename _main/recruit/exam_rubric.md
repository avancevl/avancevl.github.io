---
layout: default
title: 測驗分數評估
description: Exam Rubric
locales:
    zh-tw:
        title: 測驗分數評估
        description: 測驗分數評估
    zh-cn:
        title: 測驗分數評估
        description: 測驗分數評估
    en:
        title: Exam Rubric
        description: "Know exactly where you stand."
---

<a name="zh-tw"></a>

[參考測驗指示]({{ site.baseurl }}/{{ page.lang }}/recruit/webdev.html){: .btn#page-btn}
[參考考試樣本]({{ site.baseurl }}/{{ page.lang }}/recruit/webdev_sample.html){: .btn#page-btn}

## 考試結果如何被評估
* 考試的目的是用實際面準確的測量實力，題目跟工作上的應用類似。
* 你的考試成就會決定你的職位與薪資範圍。
	* 越多可**完整使用的功能**，分數越高。

### 我們重視：
1. **速度.** 多快速能架構好有各功能的網頁？
1. **品質.** 其他工程師很容易瞭解並維修你寫的程式碼？

### 我們會看：
1. 你的 web URL。
	1. 網頁是否可以使用，功能規格是依照指示。
	1. 實際做出來的項目少，但品質好。
1. 你的 GitHub/GitLab **Git Commits**（以後申請工作可使用）
	1. 我們會以你的 GitHub/GitLab 上的 git commit 上傳程式碼時間來檢查考試期間內是否完成。
	1. 你的**第一個 commit** 應該在考試開始時。應該是幾乎空白，只有基本的程式碼，一些簡單網頁的架構設置。
	1. 你應該大概**每30分鐘 commit 一次**，總共大約5個 commits。
	1. 你在 2.5 小時裡，需要用你的 commits 來**顯示你的進度**。你最後的 commit 不應該包含全部或大部分的程式碼。

## 功能分數講解

* **滿分**是每項功能最多分。
	* 每題的滿分數都會直接寫在考卷上。測驗當天才會知道。
	* 越難越長的考題，滿分會越多。
* **分數百分比**是依照每項功能的實做品質。
	* 每個項目我們會個0%到100%的分數。
	* 0%是最低的分數, 100%是最高的分數。
* **總分 = (滿分) x (分數百分比)**
	* 我們把每項功能加起來達到**測驗總分數.**
* **測驗總分數** = 每項功能加起來
* **測驗總百分比 = (測驗總分數) / (測驗總滿分) * 100%**

```
// 每項功能
總分 = (滿分) x (分數百分比)

// 測驗總
測驗總分數 = 每項功能加起來(功能項目總分)
測驗總百分比 = (測驗總分數) / (測驗總滿分) * 100%

```

### 首席工程師 (90-100%)
* **完全無bug。**
	* 全部功能都完成，沒缺乏。
	* 全部edge case都完成。
* **UI/UX。**
	* UI長得像完成的產品，跟市面上的產品一樣。
	* 功能都非常容易用，不需看說明書。
	* 產品前端很漂亮，會是我們自己想用的。
	* Responsive Web Design
* **程式代碼品質。**
	* 代碼架構及風格都是很完美的範本。
	* 代碼架構及風格適合當作**其他工程師跟隨的範本。**
    * 代碼容易讀懂，維護。
    * Functions及variables取名一致又清楚
* **超越我們的技術**
	* 我們沒看過的很厲害的方式或技術

### 資深工程師 (70-90%)
* **完全無bug。**
	* 全部重要功能都完成。
	* 全部edge case都完成。
* **UI/UX。**
	* UI長得像完成的產品，跟市面上的產品差不多。
	* 功能都非常容易用，不需看說明書。
	* 產品前端功能性齊全，用者不需特別去了解。
	* Responsive Web Design。
* **程式代碼品質。**
	* 代碼組織和風格有些地方不一致。
	* 代碼不需是完美的例子，但品質夠格給其他工程師當範本。
	* 代碼容易讀懂，維護。
	* Functions及variables取名一致又清楚

### 初級工程師 (40-70%)
* **有些bug。**
	* 功能性都有了，但還是有些bug。
	* 有些edge case缺乏。
* **UI/UX.**
	* UI看起來功能性都有了，但上架之前還是需要修復一下。
	* 基本上功能都好用，但還是有些比較不易的地方。
* **程式代碼品質。**
	* 代碼的架構和風格還是有些不一致的地方。
	* 代碼不適合當作範本。
	* 代碼不容易讀懂，維護。
	* Functions及variables取名沒有一致或清楚。

### 實習生 (10-40%)
* **很多bug。**
	* 大部分功能還沒完成或非常多bug。
	* 大部分edge case都沒完成。
* **UI/UX。**
	* 不清楚功能在做什麼。
	* 不完整。
* **程式代碼品質。**
	* 代碼組織和風格有些地方不一致。
	* 代碼不適合當作範本。
	* 代碼不容易讀懂，維護。
	* Functions及variables取名沒有一致或清楚。

### 未完成 (0-10%)
* 網頁沒上架。
* 程式代碼沒上傳上GitHub/GitLab。

## 測驗分數如何對照工程職級

您的職級與薪資（E0-10）會大概以以下的表格決定，依照您的測驗分數決定。

| 測驗總分數 | 職級與薪資 |
| --- | --- |
| 90+% | 首席工程師 |
| 70-90% | 資深工程師 |
| 40-70% | 初級工程師 |
| 10-40% | 實習生 |
| 0-10% | 未完成 |

### 分數計算例子

[查看測驗計算例子]({{ site.baseurl }}/{{ page.lang }}/recruit/webdev_sample.html){: .btn#page-btn}

<a name="zh-cn"></a>

[参考测验指示]({{ site.baseurl }}/{{ page.lang }}/recruit/webdev.html){: .btn#page-btn}
[参考考试样本]({{ site.baseurl }}/{{ page.lang }}/recruit/webdev_sample.html){: .btn#page-btn}

## 考试结果如何被评估
* 考试的目的是用实际面准确的测量实力，题目跟工作上的应用类似。
* 你的考试成就会决定你的职位与薪资范围。
* 越多可**完整使用的功能**，分数越高。

### 我们重视：
1. **速度.** 多快速能架构好有各功能的网页？
1. **品质.** 其他工程师很容易了解并维修你写的程式码？

### 我们会看：
1. 你的 web URL。
	1. 网页是否可以使用，功能规格是依照指示。
	1. 实际做出来的项目少，但品质好。
1. 你的 GitHub/GitLab **Git Commits**（以后申请工作可使用）
	1. 我们会以你的 GitHub/GitLab 上的 git commit 上传程式码时间来检查考试期间内是否完成。
	1. 你的**第一个 commit** 应该在考试开始时。应该是几乎空白，只有基本的程式码，一些简单网页的架构设置。
	1. 你应该大概**每30分钟 commit 一次**，总共大约5个 commits。
	1. 你在 2.5 小时里，需要用你的 commits 来**显示你的进度**。你最后的 commit 不应该包含全部或大部分的程式码。

## 功能分数讲解

* **满分**是每项功能最多分。
	* 每题的满分数都会直接写在考卷上。测验当天才会知道。
	* 越难越长的考题，满分会越多。
* **分数百分比**是依照每项功能的实做品质。
	* 每个项目我们会个0%到100%的分数。
	* 0%是最低的分数, 100%是最高的分数。
* **总分 = (满分) x (分数百分比)**
	* 我们把每项功能加起来达到**测验总分数.**
* **测验总分数** = 每项功能加起来
* **测验总百分比 = (测验总分数) / (测验总满分) * 100%**

```
// 每项功能
总分 = (满分) x (分数百分比)

// 测验总
测验总分数 = 每项功能加起来(功能项目总分)
测验总百分比 = (测验总分数) / (测验总满分) * 100%

```

### 首席工程师 (90-100%)
* **完全无bug。**
	* 全部功能都完成，没缺乏。
	* 全部edge case都完成。
* **UI/UX。**
	* UI长得像完成的产品，跟市面上的产品一样。
	* 功能都非常容易用，不需看说明书。
	* 产品前端很漂亮，会是我们自己想用的。
	* Responsive Web Design
* **程式代码品质。**
	* 代码架构及风格都是很完美的范本。
	* 代码架构及风格适合当作**其他工程师跟随的范本。 **
    * 代码容易读懂，维护。
    * Functions及variables取名一致又清楚
* **超越我们的技术**
	* 我们没看过的很厉害的方式或技术

### 资深工程师 (70-90%)
* **完全无bug。**
	* 全部重要功能都完成。
	* 全部edge case都完成。
* **UI/UX。**
	* UI长得像完成的产品，跟市面上的产品差不多。
	* 功能都非常容易用，不需看说明书。
	* 产品前端功能性齐全，用者不需特别去了解。
	* Responsive Web Design。
* **程式代码品质。**
	* 代码组织和风格有些地方不一致。
	* 代码不需是完美的例子，但品质够格给其他工程师当范本。
	* 代码容易读懂，维护。
	* Functions及variables取名一致又清楚

### 初级工程师 (40-70%)
* **有些bug。**
	* 功能性都有了，但还是有些bug。
	* 有些edge case缺乏。
* **UI/UX.**
	* UI看起来功能性都有了，但上架之前还是需要修复一下。
	* 基本上功能都好用，但还是有些比较不易的地方。
* **程式代码品质。**
	* 代码的架构和风格还是有些不一致的地方。
	* 代码不适合当作范本。
	* 代码不容易读懂，维护。
	* Functions及variables取名没有一致或清楚。

### 实习生 (10-40%)
* **很多bug。**
	* 大部分功能还没完成或非常多bug。
	* 大部分edge case都没完成。
* **UI/UX。**
	* 不清楚功能在做什么。
	* 不完整。
* **程式代码品质。**
	* 代码组织和风格有些地方不一致。
	* 代码不适合当作范本。
	* 代码不容易读懂，维护。
	* Functions及variables取名没有一致或清楚。

### 未完成 (0-10%)
* 网页没上架。
* 程式代码没上传上GitHub/GitLab。

## 测验分数如何对照工程职级

您的职级与薪资（E0-10）会大概以以下的表格决定，依照您的测验分数决定。

| 测验总分数 | 职级与薪资 |
| --- | --- |
| 90+% | 首席工程师 |
| 70-90% | 资深工程师 |
| 40-70% | 初级工程师 |
| 10-40% | 实习生 |
| 0-10% | 未完成 |

### 分数计算例子

[查看测验计算例子]({{ site.baseurl }}/{{ page.lang }}/recruit/webdev_sample.html){: .btn#page-btn}

<a name="zh-en"></a>

[View Instructions]({{ site.baseurl }}/{{ page.lang }}/recruit/webdev.html){: .btn#page-btn}
[View Sample Exam]({{ site.baseurl }}/{{ page.lang }}/recruit/webdev_sample.html){: .btn#page-btn}

## How You Will Be Evaluated
* Our exam is designed to be an accurate reflection of the type of work you will be doing at our fast growing, lean startup.
* Your Engineer Level (E0-10) and therefore salary package will be decided by the completeness of your web app and the quality of your work.
	* The more functional features you are able to complete on our checklist, the higher your engineering/salary level.

### We value:
1. **Speed.** How quickly can you build a working app with a list of features?
1. **Code Quality.** How easy is it for other engineers to maintain your app?

### We will look at:
1. Your live web app with features as described by the exam, hosted on your own computer.
	1. **Functional and working.** We value functional, working prototypes, so make sure your site is live and running before you move onto additional features. Before your exam date to save time, we recommend setting a blank single page site on your development machine accessible on the web. 
	1. **Quality over quantity.** We would rather you focus on fewer features that are working and bug-free, rather than a bunch of broken, buggy features. 
1. Your code, hosted on Github. (This can serve as a portfolio for your future interviews and resume.)
1. Your **Git Commits**
	1. We use git commit times on your Github/GitLab to check that all of your exam work was completed **during your scheduled exam period**.
	1. Your first commit should be at the start of your exam time. Your **first commit** should only be an almost blank, basic, starter code to get a webpage up and running, likley with some simple pre-built framework setup.
	1. You should **commit every 30-minute**, with a total around 5 commits overall.
	1. Your commits should **show your progress** in the 2.5hr. Your final commit should not contain all or most of your work. 

## Feature Rubric

* **Maximum Points** is the maximum number of points each feature is worth.
	* This will be listed on the actual exam.
	* Correlated with the difficulty of the problem.
* **Score Percentage** of feature based on submission quality.
	* For each feature, we will assign a score from 0% to 100%.
	* 0% is lowest possible score, 100% is highest possible score.
* **Total Points = (Maximum Points) x (Score Percentage)**
	* We sum up the total points scored for each feature to get the **Exam Total Points.**
* **Exam Total Points** = sum up points scored on all features
* **Exam Total Score = (Exam Total Points) / (Exam Maximum Points) * 100%**

```
// Per Feature
Total Points = (Maximum Points) x (Score Percentage)

// Exam Total
Exam Total Points = Sum for all features(Total Points)
Exam Total Score = (Exam Total Points) / (Exam Maximum Points) * 100%

```

### Lead Engineer (90-100%)
* **Zero bugs.**
	* Complete features and options, nothing missing.
	* All edge cases taken into account.
* **UI/UX.**
	* UI looks like a real finished, production-ready product, as good as a real competitor.
	* Intuitive and easy to use. We should have to ask you how to use a product.
	* Product looks beautiful, something we would love to use ourselves.
	* Responsive Web Design
* **Code Quality.** Code organization and style is perfect example of quality code.
	* Code style and organization be used as ** example for other engineers to follow.**
    * Easier for other engineers to read, understand, and maintain.
    * Clear, consistent naming conventions for functions and variables.
* **Surprise Us.**
	* Some new method or way of doing something that we didn't know about before.

### Senior Engineer (70-90%)
* **No major bugs.**
	* All major functionality should be there.
	* All edge cases taken into account.
* **UI/UX.**
	* UI looks like a functional, working production-ready product. Close in quality to a real, competitor product.
	* Intuitive and easy to use.
	* Product looks functional. Does not have to be beautiful, but user has to "get" how to use it.
	* Responsive Web Design.
* **Code Quality.** Code organization and style has to be consistent and clean.
	* Does not have to be perfect example, but good enough for others to follow.
	* Easy for other engineers to read, understand, and maintain.
	* Clear, consistent naming conventions for functions and variables.

### Junior Engineer (40-70%)
* **Some bugs.**
	* All major functionality is there, but buggy.
	* Some edge cases missing.
* **UI/UX.**
	* UI looks functional, but needs some work before production.
	* Generally easy to use, some leeway allowed.
* **Code Quality.**
	* Code organization and sytle has inconsistencies.
	* Not good enough for others to follow.
	* Not easy to read, understand, or maintain.
	* Unclear, inconsistent naming conventions for functions and variables.

### Intern Engineer (10-40%)
* **Lots of bugs.**
	* Feature mostly incomplete or very buggy.
	* Most edge cases imcomplete.
* **UI/UX.**
	* Unclear what the function is.
	* Incomplete.
* **Code Quality.**
	* Code organization and sytle has inconsistencies.
	* Not good enough for others to follow.
	* Not easy to read, understand, or maintain.
	* Unclear, inconsistent naming conventions for functions and variables.

### No Attempt (0-10%)
* No working live website.
* Nothing committed to GitHub.

## Total Score Mapping to Engineer Level

Your Engineer Level (E0-10) and therefore salary package will be roughly be decided by this table, depending on where your score falls under.

| Total Exam Score | Hiring Engineer Level |
| --- | --- |
| 90+% | Lead Engineer |
| 70-90% | Senior Engineer |
| 40-70% | Junior Engineer |
| 10-40% | Intern Engineer |
| 0-10% | No Attempt |

### Example Calculations

[See Example Calculations]({{ site.baseurl }}/{{ page.lang }}/recruit/webdev_sample.html){: .btn#page-btn}


