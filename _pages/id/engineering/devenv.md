---
layout: default
title: 開發環境
lang: id
description: 開發環境
---



# 作業系統

* Windows
* macOS
* Linux

<br>

# 設定開發環境

## 代碼格式輔助工具

[前往代碼格式規範及工具解說]({{ site.baseurl }}/{{ page.lang }}/engineering/code_styles.html)

<br>

---

<br>

## 輔助工具

#### Node.js及npm

* 下載[長期開發版本](https://nodejs.org/en/download/){:target="_blank"}
* 如何確認安裝成功，打開terminal或command prompt，`node -v` 顯示安裝版本

#### Babel

* Babel是個JavaScript compiler，提供backward compatible syntax的支持。
* 安裝 Babel
```
npm i @babel/core @babel/node @babel/preset-env @babel/preset-es2015 @babel/preset-react -D
npm i @babel/plugin-syntax-dynamic-import @babel/plugin-proposal-class-properties @babel/plugin-proposal-export-namespace-from @babel/plugin-proposal-throw-expressions -D
```
* 建立 `.babelrc` 
```
{
    "presets": [
      "@babel/env",
      "@babel/react",
    ],
    "plugins": [
      "@babel/plugin-syntax-dynamic-import",
      "@babel/plugin-proposal-class-properties",
      "@babel/plugin-proposal-export-namespace-from",
      "@babel/plugin-proposal-throw-expressions"
    ]
}
```

#### Webpack

* [了解Webpack](https://medium.com/the-self-taught-programmer/what-is-webpack-and-why-should-i-care-part-1-introduction-ca4da7d0d8dc){:target="_blank"}
* 安裝 Webpack
```
npm i webpack webpack-cli webpack-dev-middleware webpack-dev-server webpack-hot-middleware node-sass style-loader css-loader babel-loader mini-css-extract-plugin html-webpack-plugin -S
```

<br>

---

<br>

## 重要架構

#### React.js

* [開始了解React](https://reactjs.org/docs/getting-started.html){:target="_blank"}
* [建立React App指南](https://reactjs.org/docs/create-a-new-react-app.html){:target="_blank"}


#### Vue.js

* [開始了解Vue](https://vuejs.org/v2/guide/){:target="_blank"}