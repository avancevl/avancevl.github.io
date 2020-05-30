---
layout: default
title: SSR前端架構
lang: zh-tw
description: SSR前端架構
---



| Server Side Rendering架構 | **Next.js** |

<br>

# CSR和SSR前端架構比較

## Client Side Rendering (CSR)

<img src='https://lh3.googleusercontent.com/SLKkSaDSKfz7RwZEVz2WUkqYQ9mnRof7McaY57Mf8JpgDODMgEAA3JCkoHbC1JoTDa3MtBGKmIIEdiaENoEpSSp1L7GBfeR0ARQC3Zm5SbEoGbT_GIvn6t_UsH-T5jKEWGgLbzEWfg=w800' />

* Google和Facebook News Feed看到的網頁完全沒有內容，只有JavaScript檔案

```html

<!DOCTYPE html>
<html>
  <head>
    <title>My SPA APP Title</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="text/javascript" src="/bundle.js"></script>
  </body>
</html>
```

<br>

## Server Side Rendering (SSR)

<img src='https://lh3.googleusercontent.com/PqfLbRvYuFY5I26xjPHlWEusCJZ6FWKoHdJpJLqQUgH2upEKNlBphTxmzCNoaBcgCa0ZJQ1pANQ0LwUGoEOj3cSvHKDKcVD7SvPL57qK4twnGvKk5IxGeUFLBR1nyt79tB7PWscWXw=w800' />

<br>

## Prerendering (Static Sites)

* `react-snap`
* `react-static`
* `gatsby`
* [`rendertron`](https://github.com/GoogleChrome/rendertron){:target="_blank"}
* `puppetron`
* `pupperender`

<br>

# SSR如何在React.js架構實作

## React - Server Side Rendering (SSR)

<img src='https://lh3.googleusercontent.com/uutZ0xtPwsF1qO1gzf2X497gaVLEMhfIeOJl9YsLkVhdZKE9KKG_UnwC77VJc_2nMc2rfwEvLsTPh7Jnk8In_vB_s7NldulHCw3u9bzshB59ypxNq5E8MxZr7upTNqtPAjX8pdJ9Pg=w800' />

### 技術考量於目標

1. 第一次網頁下載速度要快，CSR會有延遲
1. 為了SEO考量，網頁資料需要能被Google Crawler/Indexer容易找到，資料不能藏在JavaScript裡
1. 當網頁被分享到social media時（Facebook, LinkedIn news feeds)，HTML需要直接有網頁的內容，不然會沒有preview
1. 應用SSR程式複雜度不能太嚴重，維持開發程式的簡易及速度

### 線上資源

* [React DOM Server](https://reactjs.org/docs/react-dom-server.html){:target="_blank"}
* [JavaScrip SEO: SSR vs CSR](https://medium.com/@benjburkholder/javascript-seo-server-side-rendering-vs-client-side-rendering-bc06b8ca2383){:target="_blank"}
* [SSR with React](https://medium.com/@swazza85/ssr-with-react-9cb197cfe380){:target="_blank"}
* [Server Side Rendering with React](https://flaviocopes.com/react-server-side-rendering/){:target="_blank"}
* [Server Side Rendering with React, Redux, and React-Router](https://itnext.io/server-side-rendering-with-react-redux-and-react-router-fa5b67d4965e){:target="_blank"}

<br>

## React - Next.js

* 建議使用[create-next-app](https://github.com/zeit/create-next-app){:target="_blank"}來建立新的app


### 線上資源

* [Next.js](https://nextjs.org/){:target="_blank"}
	* The React Framework for Sender-Rendered Apps
	* SEO-Friendly Sites
	* PWA
* [Next.js - React Server-side Rendering Done Right](https://medium.com/better-programming/next-js-react-server-side-rendering-done-right-f9700078a3b6){:target="_blank"}
* [Create Next App](https://github.com/zeit/create-next-app){:target="_blank"}


#### Next.js如何結合Express.js

* [Buildilng a server-rendered React app with Next.js and Express.js](https://blog.logrocket.com/how-to-build-a-server-rendered-react-app-with-next-express-d5a389e7ab2f/){:target="_blank"}


#### Next.js如何結合Firebase Cloud Functions

* [Next.js on Cloud Functions for Firebase with Firebase Hosting](https://codeburst.io/next-js-on-cloud-functions-for-firebase-with-firebase-hosting-7911465298f2){:target="_blank"}
* [Next-routers with Firebase Hosting on Cloud Functions](https://codeburst.io/next-routes-with-firebase-hosting-on-cloud-functions-e7c78308a24d){:target="_blank"}
* [NextJS with Firebase Cloud Functions](https://stackoverflow.com/questions/45185452/nextjs-with-firebase-cloud-functions){:target="_blank"}


#### Redux如何資源Server Side Render

* [Server Side Rendering with Redux](https://redux.js.org/recipes/server-rendering/){:target="_blank"}