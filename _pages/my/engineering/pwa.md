---
layout: default
title: PWA前端架構
lang: my
description: PWA前端架構
---



# PWA主要概念理想

1. 資源下線offline模式
	1. static site assets會自動被cache，下一次開起就超快
	1. 遠離wifi時app還是可以使用
1. 開起時顯示splash screen
1. 支援push notifications
1. 網頁可以在手機首頁home screen下載一個app icon
1. 網頁設計基本上會長的像手機app一樣

<br>

# PWA如何在React.js架構實作

### Service Workers

* Service workers (client-side proxies that pre-cache key resources) enable PWAs to load instantly and provide an instant, reliable experience for users, regardless of the network state
* This is a browser capability to provide an intermediate layer between the Web App and the network, which runs in the background (even when the application is closed). This “network” layer is capable of listening and sending requests, notifications or even capturing connectivity changes
* 實作PWA是靠web browser內建在背景跑的一個程式
* React已經內建好browser的service worker功能，請看`src/servicewWorker.js`。只需要呼叫`serviceWorker.register();`就搞定了

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

ReactDOM.render(<App />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.register();
```

### 線上資源

* [Workbox](https://developers.google.com/web/tools/workbox){:target="_blank"}
	* JavaScript libraries for adding offline support to web apps
* [Lighthouse](https://developers.google.com/web/tools/lighthouse/){:target="_blank"}
	* 確認網頁的確是符合PWA的規則
	* Lighthouse is an open-source, automated tool for improving the quality of web pages. You can run it against any web page, public or requiring authentication. It has audits for performance, accessibility, progressive web apps, SEO and more.
* [Convert React App into a PWA](https://dev.to/phonerefer/convert-react-app-into-a-progressive-web-app-pwa-b0f){:target="_blank"}
* [From create-react-app to PWA](https://blog.logrocket.com/from-create-react-app-to-pwa/){:target="_blank"}
* [Build a Realtime PWA with React](https://medium.com/better-programming/build-a-realtime-pwa-with-react-99e7b0fd3270){:target="_blank"}
* [GitHub: Create React App](https://github.com/facebook/create-react-app){:target="_blank"}