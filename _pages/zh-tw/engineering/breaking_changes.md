---
layout: default
title: 破壞性更改
lang: zh-tw
description: 破壞性更改
---



## 原則

1. Unit Test, Regression Test成本非常高也很難完整，一定會有漏掉的地方。
1. Merge, Pull Request工程師時間成本很高，也一樣無法保證沒有breaking changes。

## 破壞性更改

* 資料庫格式變動
* 改到別人寫的代碼
* 改到別人寫的程式會依賴的代碼

## 告知破壞性更改流程

在Slack channel `#0-scrum` 請跟大家告知：

> 1. 你改了什麼
> 2. 如果有的話，更改的commit hash
> 3. 改動時間
> 4. 可能會影響或破壞的東西
> 5. 如果真的有東西壞掉，去研究查看哪個檔案

