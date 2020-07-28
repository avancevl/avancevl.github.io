---
layout: default
title: 生產架構
lang: my
description: 生產架構
---



| 第一階段雲端服務 | Firebase, ZEIT |

# 架構設計目標

* 最低的開發時間成本。
	* 工程師開發時間就是金錢，省時間就是省錢。
	* 初期開發成本，複雜度。
	* 維護成本，複雜度。
	* 成長擴充成本，複雜度。
* 最低的運行成本。
	* 低流量成本。
	* 高流量成本。

<br>

# 開發架構順序

> **如何用最低成本最快速度開發上線初期產品MVP？**

<br>

## 第一階段：Database-as-a-Service + Lambda Compute Service

> **MVP Stack**

### Database-as-a-Service

* 不需架設資料庫及維護。
* 不需架設server, linux。
* 不需請DevOps或SRE維護平台。
* 專注在code上面就夠。

| 服務 | 優點 | 缺點 | 決定 |
| --- | --- | --- | --- |
| Google Firebase | 最多人用 |  | 考慮 |
| AWS Amplify | AWS環境，流量多時便宜 | | 考慮 |

#### Firebase

* [Introduction to Firebase](https://hackernoon.com/introduction-to-firebase-218a23186cd7){:target="_blank"}
* [Progressive Web Apps](https://firebase.google.com/docs/projects/pwa){:target="_blank"}
* [FireShip.io](https://fireship.io/){:target="_blank"}
* Json的No-SQL資料庫，如果需要SQL資料庫就麻煩了
* OAuth已經內建
* 有內建Analytics, Chat

#### AWS Amplify

* [Introduction to Amplify](https://aws.amazon.com/amplify/){:target="_blank"}


### Static Hosting

#### ZEIT

* 上線Next.js最快速最簡單的雲端服務
* 已經幫使用者實作Server Side Render
* [ZEIT](https://zeit.co/){:target="_blank"}


### Lambda Compute Service

* 最基礎的初期產品可能連商業邏輯都不需要。
* 需要一開始就把商業邏輯分開也是一種成本。
* 但之後因為商業邏輯已分開了，比較容易叩沖及減低成本。
* 不需架設server, linux。
* 不需請DevOps或SRE維護平台。
* 專注在code上面就夠。

| 服務 | 優點 | 缺點 | 決定 |
| --- | --- | --- | --- |
| Google Coud Functions | 跟Firebase結合容易 |  | 考慮 |
| AWS Lambda | AWS環境，流量多時便宜 | | 考慮 |
| Google App Engine | 流量多時便宜 | | 考慮 |
| Azure Functions | 流量多時便宜 | | 考慮 |

### Analytics

1. Stickiness KPI - 客戶使用者retention
1. Virality KPI - 客戶使用者compound effect
1. Paid KPI - 客戶使用者付費意願

* Google Analytics
* Firebase

<br>

## 第二階段：Platform-as-a-Service

> **如何開始容納高流量**

* 資料庫需要自己架設及維護。
* 可以使用比較完整的架構（Django, Rails）。
* 商業邏輯不需要分開到Lambda Compute服務（這有好壞）。
* 不需架設server, linux。
* 不需請DevOps或SRE維護平台。
* 如果網頁程式掛掉，服務會直接從新開始，不需有人監視。

| 服務 | 優點 | 缺點 | 決定 |
| --- | --- | --- | --- |
| Heroku | 最早開發的，一開始免費 | 流量多時很快就很貴 | 不用 |
| AWS Elastic Beanstalk | AWS環境，流量多時便宜 | | 考慮 |
| Google App Engine | 流量多時便宜 | | 考慮 |
| Azure App Platform | 流量多時便宜 | | 考慮 |

#### Heroku

* [How Heroku Works](https://devcenter.heroku.com/articles/how-heroku-works){:target="_blank"}
* 工程師文件資料多，產品成熟。

<br>

## 第三階段：Infrastructure-as-a-Service

* 除了買電腦其他基本上全部要自己做。
* 高流量時最便宜方案。
* 需要請DevOps或SRE監視系統，增加成本。

| 服務 | 優點 | 缺點 | 決定 |
| --- | --- | --- | --- |
| AWS EC2 | | | 考慮 |
| Google Cloud Compute Engine | | | 考慮 |
| Azure Cloud | | | 考慮 |
| DigitalOceans | | | 考慮 |
| Linode | | | 考慮 |

<br>

# 歡迎建議

如果有其他對生產架構看法或建議，請由[git issue]({{ site.github.repository_url }}/issues/new)分享，謝謝！