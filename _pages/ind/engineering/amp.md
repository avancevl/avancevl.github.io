---
layout: default
title: AMP前端架構
lang: ind
description: AMP前端架構
---



## AMP主要概念理想

* **AMP HTML:** 簡化版的HTML讓網頁更快的呈現出來。
* **AMP Cache:** Google和Bing會先cache好AMP在他們的伺服器上，讓尋找結果更快顯示。
* 在手機環境page load速度會提高
* Google SEO排名會提高

<br>

## 支持AMP的React.js架構

| 架構 | HTML建立時刻 | 需要server? | 適合使用網頁 |
| --- | --- | --- | --- |
| Next.js | Real Time | 需要 | 比較複雜或多網頁時 |
| Gatsby.js | Build Time | 不需 | 比較小的網頁，blogs |

<br>

## 如何在Next.js架構裡實作AMP

* 雖然Next.js是個React.js的架構，當你用AMP時你的網頁就不可能是client side React了，因為兩個網頁的理念是完全衝突的。
* 當你用Next.js來顯示AMP網頁，Next.js已經比較像server side templating engine，而不是React前端component了。
* Next.js提供兩種建立AMP網頁的方式。

### Hybrid AMP

`pages/home.js`

```javascript
import { useAmp } from 'next/amp'

export const config = {
  amp: 'hybrid'
}

export default () => {
  const isAmp = useAmp()
  return (
    <div>
      <p>{isAmp ? 'Not AMP Home Page' : 'Home Page'}</p>
    </div>
   )
}
```

### AMP-only

`pages/index.js`

```javascript
import Nav from '../components/nav'
import { useAmp } from 'next/amp'

export const config = {
  amp: true
}
```

### 線上資源

* [Create AMP Pages](https://nextjs.org/learn/excel/amp){:target="_blank"}
* [How to use AMP in Next.js](https://web.dev/how-to-use-amp-in-nextjs/){:target="_blank"}
* [What is Next.js and how you can build an AMP page with it?](https://dev.to/quickly_react/what-is-next-js-and-how-you-can-build-an-amp-page-with-it-4g12){:target="_blank"}
* [Gatsby vs Next.JS](https://dev.to/jameesy/gatsby-vs-next-js-what-why-and-when-4al5){:target="_blank"}

<br>

## AMP及CSS的一些結合問題

* CSS imports is non-standard behavior in AMP,
* Linking external CSS files is not even supported in AMP, they'd have to be inlined.
* AMP has restrictions on the amount of CSS that can be sent which are very restrictive so CSS imports will send too much CSS in general.

### Styled-JSX Webpack Loader

* [`github: styled-jsx`](https://github.com/zeit/styled-jsx#nextjs){:target="_blank"}
* We bundle styled-jsx to provide support for isolated scoped CSS. 
* The aim is to support "shadow CSS" similar to Web Components, which unfortunately do not support server-rendering and are JS-only.
* You can use the `styled-jsx` Webpack loader to import external CSS in AMP mode for now.
* You just have to be careful to not go over the 50,000 bytes limit for styles in AMP.

```javascript
function HelloWorld() {
  return (
    <div>
      Hello world
      <p>scoped!</p>
      <style jsx>{`
        p {
          color: blue;
        }
        div {
          background: red;
        }
        @media (max-width: 600px) {
          div {
            background: blue;
          }
        }
      `}</style>
      <style global jsx>{`
        body {
          background: black;
        }
      `}</style>
    </div>
  )
}

export default HelloWorld
```

### CSS-in-JS

* It's possible to use any existing CSS-in-JS solution. The simplest one is inline styles:

```javascript
function HiThere() {
  return <p style={{ color: 'red' }}>hi there</p>
}

export default HiThere
```

* To use more sophisticated CSS-in-JS solutions, you typically have to implement style flushing for server-side rendering. We enable this by allowing you to define your own custom `<Document>` component that wraps each page.

### Importing CSS / Sass / Less / Stylus files

* To support importing .css, .scss, .less or .styl files you can use these modules, which configure sensible defaults for server rendered applications.
	* `@zeit/next-css`
	* `@zeit/next-sass`
	* `@zeit/next-less`
	* `@zeit/next-stylus`

### 線上資源

* [github: AMP: styles missing when importing standard css files in a project using styled components](https://github.com/zeit/next.js/issues/7121){:target="_blank"}
* [zeit: Built-In CSS Support](https://nextjs.org/docs/basic-features/built-in-css-support){:target="_blank"}
* [`github: withAmpSass`](https://gist.github.com/blech75/b9238c5569e03a637c9cd21d596e80f0){:target="_blank"}