---
layout: default
title: 前端架構
lang: my
description: 前端核心能力
---



| 前端畫面架構 | **React.js** |
| 前端Server Side Rendering架構 | **Next.js** |
| 手機前端畫面架構 | **ReactNative** |
| 前端持續性資料架構 | **Redux** |
| 前端表格架構 | **Chart.js** |

<br>

# 前端畫面架構

## React.js及Vue.js的共同優點

其實選擇使用Vue.js或是React.js不是那麼容易。

### 1. 虛擬DOM Virtual DOM

當有需要更新畫面，只需更新一部分。這會省時間和提高效率。

### 2. 另件組合前端開發 Component-based UI Development

把前端切成可以重複使用的components，提高開發前端的效能和數度。

### 3. 針對前端 Front-end Focused

這些架構會要求開發者一開始就把前後端分離。

<br>

## React.js前端架構

### 優點

1. 比較多工程師有經驗
1. 很多第三方的package可以直接拿來套用
1. Facebook和其他很大的公司有在支持
1. ReactiveNative可以很快的開發iOS和Android的app

### 缺點

1. 比Vue.js還難學
1. 只用JSX，對大部分工程師比HTML templates還難上手

### 線上資源

* [`github: React Starter Kit for Firebase`](https://github.com/kriasoft/react-firebase-starter){:target="_blank"}
* [**React Rainbow**](https://react-rainbow.web.app/){:target="_blank"}

<br>

## Vue.js前端架構

### 優點

1. 上手很快，新手比較容易學習
1. 文件（中文）寫的不錯
1. 架構比較簡單輕便
1. 不需要用JSX，支持傳統HTML templates

### 缺點

1. 缺乏類似ReactNative手機架構

<br>

## 主要考量因數

1. ReactiveNative可以很快的開發iOS和Android的app

<br>

# 前端持續性資料架構

## Redux的意義

1. 跟React架構的結合非常密切
1. 前端一定會需要維護持續性資料
1. 一開始持續性資料就放在很清楚切割的Redux模組
1. 商業邏輯可以放在Redux模組裡
1. 一開始可能會有些開發成本，但之後程式比較好整理
1. 純畫面模組也比較好測試Unit Test

<br>

# 前端持續性資料架構

## 線上資源

* [React UI components collection](https://react-rainbow.web.app/){:target="_blank"}
* [JavaScript Graphics](https://www.chartjs.org/){:target="_blank"}
* [Font Scripts](https://developers.google.com/fonts/docs/developer_api){:target="_blank"}
* [Polyfill](https://github.com/financial-times/polyfill-service){:target="_blank"}