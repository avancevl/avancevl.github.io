---
layout: default
title: 問題追中
lang: zh-cn
description: 問題追中
---



## JIRA 问题（Issue）

* JIRA专案管理系统里最小单位。
* 我们公司规定，每个JIRA问题有三个必添栏位：

1. 故事分数（Story Points）
1. 优先权 (Priority)
1. 时间估计（Time Estimate）

<img src='https://lh3.googleusercontent.com/7w7NZu3F5zVrzixjhx5qYeVU54nQERp7WiAMECaQoyQJ3zCQgciMy8vrtX1RKH_zPpZCJeiejvLOmeZc161BVPtd6k3pQI64EBvIrA2dvoyOm39Zh52C0B0OB9R5k8ihuqWm7fZnEw=w800' />


### 故事分数（Story Points）：KPI分数（KPI Points）

* 公司跟其他主要不一样的地方是，我们Story Points不是在估计问题的难度或时间，而是问题对于团队KPI的共享。
* 我们希望避免的事团队JIRA问题一大堆，完成很多，大家很忙，但是其实问题对团队达到KPI没有什么影响力或共享。
* 这种故事分数的分配是**影响力追中（Impact-Focused Tracking）**，分数是跟问题的重要性，影响力，KPI有直接的关联性。

| 故事分数（Story Points）| 人事KPI | 初期产品KPI | 使用KPI | 营收KPI |
| --- | --- | --- | --- | --- | --- |
| 1 | 1位面试者 | 100申请者 | 100位使用者 | 美金 $1K MRR |
| 2 | 10位面试者 | 1K申请者 | 1K位使用者 | 美金 $10K MRR |
| 3 | 100位面试者| 10K申请者 | 10K使用者 | 美金 $100K MRR |

### 优先权 (Priority)：期限或挡住

| 优先权 (Priority) | 意思 |
| --- | --- |
| Highest | 最后期限这个Sprint要到期 |
| High | 这个问题会挡住其他这个Sprint的问题 |
| Medium | 这个问题会挡住下个Sprint的问题 |
| Low | 两周后再讨论的问题 |
| Lowest | 一月再讨论的问题 |

### 时间估计（Time Estimate）

大概估计时间为：

* 一天工作时间是8小时
* 半天工作时间是4小时
* **一个Issue最多时间限制2小时**，再长的Issue请分成更细的Issue。