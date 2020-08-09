---
layout: default
title: 程式代碼規範
lang: ind
description: 規範與設計指引
---



# 程式代碼規範的重要性

* **會加強工程師品質。**習慣寫好程式格式，規範一致會讓你變成更好的軟體工程師。
* **當程式代碼容易閱讀開發時間會自然縮短。**比較容易讀懂程式在做什麼。
* **提高程式效能。**JavaScript有時後是個蠻奇怪的語言。代碼格式一致會讓效能提高。

<br>

# 代碼格式自動檢查工具

| 工具 | 用途 |
| --- | --- |
| Prettier | 完全幫你把代碼formatting弄一致 |
| ESLint | 代碼品質，自動找bug |
| Linting rule sets, plugins, and extensions | 決定代碼規範 |
| Git hooks | 自動化程式規範 |

## 第一步驟：和解Prettier和自動代碼格式

[Prettier GitHub Repo & Docs](https://github.com/prettier/prettier){:target="_blank"}

Prettier會依照指定的規範把你的代碼全部從新整合。當你安裝後就不用在考慮代碼規範了。安裝在package.json裡所以不用一直提醒團員安裝。

### 安裝
```
yarn add prettier --dev
```
建議針對專案安裝，不要安裝到全系統。

### 使用

用這行代碼來整合你的代碼格式。
```
prettier --single-quote --write "src/**/*.js"
```

## 第二步驟：使用Husky加Lint-Staged來自動化Prettier的Git Hooks

[**Husky**](https://github.com/typicode/husky){:target="_blank"}用來吧githooks簡化，在代碼加入version control之前跑個subroutine。

[**Lint-Staged**](https://github.com/okonet/lint-staged){:target="_blank"}及Husky需要一起用。 會只跑在‘staged’或‘added’的Git branch。這樣prettier就不用每次跑你整個專案的代碼，只需要跑有更改過或新加的檔案。

### 安裝
```
yarn add husky lint-staged --dev
```

加precommit script到你的package.json。
```
"scripts": {
    "precommit": "lint-staged"
},
```
要確保lint-stage script也加入你的package.json。
```
{
  "scripts": {
    "precommit": "lint-staged"
  },
  "lint-staged": {
    "*.js": [
      "prettier --write",
      "git add"
    ]
  }
}
```

## 第三步驟：ESLint代碼警察

Linting是可以結合任何程式語言的小工具。可以避免工程師團隊行程不好的習慣。ESLint是個很有彈性客製化的JavaScript工具，跟其他工具結合通常蠻容易。

### 安裝

建議針對專案安裝，不要安裝到全系統。
```
yarn add eslint --dev
```

把ESLint結合到你的code editor，VC Code用者下載[ESLint Extension](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint){:target="_blank"}.

建立‘.eslintrc.json’來控制ESLint的設定。
```
// run this command in the terminal:
./node_modules/.bin/eslint --init
// Or you can just add a .eslintrc.json to your project
//Note: you may also want to add a .eslintignore . It works just like a .gitignore
```

第三方直接跟ESLint建立好的代碼格式：
* [Airbnb Sytle Guide](https://github.com/airbnb/javascript){:target="_blank"}


## 第四步驟：ESLint和React.js的結合

Facebook有為React專門設立一些設定ESLint的功能[create-react-app](https://github.com/facebook/create-react-app/tree/master/packages/eslint-config-react-app){:target="_blank"}。這個工具只會設定代碼規範。

### 安裝
```
yarn add --dev eslint-config-react-app babel-eslint eslint-plugin-flowtype eslint-plugin-import eslint-plugin-jsx-a11y eslint-plugin-react
```
如果想知道每個規範的纖細資料，可以問Google。

把plugin和rules加入`.eslintrc.json`
```
{
  "extends": ["react-app", "plugin:jsx-a11y/recommended"],
  "plugins": ["jsx-a11y"]
}
```

## 第五步驟：ESLint和Prettier的結合

因為格式規範會從ESLint及Prettier出來，我們需要確定沒有conflict。因為我們用Airbnb的規範，有conflict的可能性更高。

eslint-config-prettier: 幫忙把全部可能跟prettier衝突的格式規範找出來。
```
yarn add eslint-config-prettier --dev
```

把plugin和rules加入.eslintrc:
```
{
  "extends": [
    "prettier",
    "prettier/flowtype",  // if you are using flow
    "prettier/react"
  ]
}
```

需要更纖細的指示請參考[eslint-config-prettier](https://github.com/prettier/eslint-config-prettier){:target="_blank"}。

## 第六步驟： 其他安裝

安裝prettier ESLint plugin來看代碼裡的formatting errors。

eslint-plugin-prettier可以讓你在code editor裡直接看的你的formatting errors。在碰到git之前就知道formatting error。
```
yarn add eslint-plugin-prettier --dev
```
把plugin和rules加入.eslintrc:
```
// .eslinrc.json
{
  "plugins": [
    "prettier"
  ],
  "rules": {
    "prettier/prettier": "error"
  }
}
```
需要更纖細的指示請參考[eslint-plugin-prettie](https://github.com/prettier/eslint-plugin-prettier){:target="_blank"}。

### 其他輔助Prettier的小程式

* [prettier-eslint:](https://github.com/prettier/prettier-eslint){:target="_blank"} formats code according to your ESLint rules. Use the eslint — fix instead. Prettier improves this functionality with this tool.
* [prettier-standard:](https://github.com/sheerun/prettier-standard){:target="_blank"} formats code using standard rules. Some people like standard. This helps prettier integrate with it.

<br>

# 格式規範 Style Guides

## 基礎格式

| JavaScript | [Airbnb Sytle Guide](https://github.com/airbnb/javascript){:target="_blank"} |
| C++ | [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html){:target="_blank"} |
| Python | [Google Python Style Guide](http://google.github.io/styleguide/pyguide.html){:target="_blank"} |


## 例外格式

* tab一定要用space取代。