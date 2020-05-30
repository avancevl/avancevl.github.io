---
layout: default
title: 資料庫架構
lang: zh-tw
description: 資料庫架構
---



| Database-as-a-Service架構 | **Cloud Firestore** |

## Firebase - Cloud Firestore

### 比較好的讀取資料

儘管實時數據庫只是一棵巨大的JSON樹，但Cloud Firestore的結構更為合理。您的所有數據均由文檔（基本上是鍵值存儲）和集合（即文檔的集合）組成。文檔還將經常指向子集合，這些子集合包含其他文檔，它們本身也可以包含其他文檔，依此類推。

### 比較有結構的資料

這種結構化數據可以通過兩種方式幫助您。首先，所有查詢都是淺層的，這意味著您可以在不獲取其下所有數據的情況下請求文檔。這意味著您可以以對您更有意義的方式分層存儲數據，而不必擔心使數據庫變淺。其次，您擁有更強大的查詢。例如，您現在可以跨多個字段進行查詢，而不必創建那些組合（和去規範化）數據庫其他部分數據的“組合”字段。在某些情況下，Cloud Firestore只會直接運行這些查詢，而在其他情況下，它將為您自動創建和維護索引。

### 比較強的擴充性能

Cloud Firestore的擴展能力將優於實時數據庫。重要的是要注意您的查詢擴展到結果集的大小，而不是數據集的大小。因此，無論您的數據集有多大，搜索都將保持快速。

### 比較容易手動取資料

像實時數據庫一樣，您可以在Cloud Firestore中設置偵聽器以實時流式傳輸更改。但是，如果您不希望這種行為，而只希望進行簡單的“獲取我的數據”調用，則Cloud Firestore也可以做到這一點，並且它是作為主要用例內置的。 （它們比實時數據庫領域的一次調用要好得多）

### 資源多地區

基本上，這意味著更高的可靠性，因為您的數據可以在多個數據中心中一次共享。但是您仍然具有很強的一致性，這意味著您始終可以進行查詢，並可以確保獲得最新版本的數據。

### 不同的計價方式

實時數據庫主要根據存儲或網絡帶寬收費，而Cloud Firestore主要根據您執行的操作數量收費。這會好還是壞？這取決於您的應用程序。

對於新聞應用，回合製多人遊戲或您自己的Stack Overflow版本而言，Cloud Firestore從定價角度看可能會非常優惠。對於像實時小組繪圖應用程序這樣的應用程序，您需要將多個更新每秒發送給多個人，它可能會比實時數據庫昂貴。

### 線上資源

* [Cloud Firestore Data Model](https://firebase.google.com/docs/firestore/data-model){:target="_blank"}

<br>

## Firebase - Realtime Database

1. 整個“對於經常更新的應用程序來說，它可能會便宜一些”
1. 它已經存在很長時間了，並且已經過數千個應用程序的實戰測試（Cloud Firestore仍處於Beta版）
1. 它具有更好的延遲，並且當您需要實時性低且可靠的東西時，實時數據庫可能會更好。

<br>

## 線上資源

* [SO: What's the difference between Cloud Firestore and the Firebase Realtime Database?](https://stackoverflow.com/questions/46549766/whats-the-difference-between-cloud-firestore-and-the-firebase-realtime-database){:target="_blank"}
* [Realtime Database vs. Cloud Firestore — Which Database is Suitable for your Mobile App](https://medium.com/datadriveninvestor/realtime-database-vs-cloud-firestore-which-database-is-suitable-for-your-mobile-app-87e11b56f50f){:target="_blank"}
* [Firebase Cloud Firestore v/s Firebase Realtime Database](https://medium.com/@beingrahul/firebase-cloud-firestore-v-s-firebase-realtime-database-931d4265d4b0){:target="_blank"}
* [Choose a Database: Cloud Firestore or Realtime Database](https://firebase.google.com/docs/database/rtdb-vs-firestore){:target="_blank"}