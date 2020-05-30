---
layout: default
title: 數學公式前端
lang: zh-cn
description: 數學公式前端
---



| 數學公式前端 | Katex |

<br>

## Latex

```
% \f is defined as f(#1) using the macro
\f{x} = \int_{-\infty}^\infty
    \hat \f\xi\,e^{2 \pi i \xi x}
    \,d\xi
```

<img src='https://lh3.googleusercontent.com/L_hYOV5IsdxHfoIzB9zfqLJMkw0AeAQoe-BLrqRAI2dUp5QpQxwDIDXR7n_l8bVWmL1TMQp7daHRbVwN3cQXCNxJZtXJYpqafjPGMCTAwj5PSyLXdqT43u7Xm8HcynRnDu4qPubVhQ=w400' />

## Katex

* 用latex表達數學公式
* 資源server side rendering或generate HTML
* To generate HTML on the server or to generate an HTML string of the rendered math, you can use 

```javascript
katex.renderToString:

var html = katex.renderToString("c = \\pm\\sqrt{a^2 + b^2}", {
    throwOnError: false
});
// '<span class="katex">...</span>'
```

* [Katex](https://katex.org/){:target="_blank"}
* [Katex Docs](https://katex.org/docs/api.html){:target="_blank"}


## MathJax

* 可以用latex表達數學公式
* 使用custom JavaScript，實作AMP比較困難
* The AMP pages only allow third-party JavaScript but only in sandboxed iframes. By restricting them to iframes, they can’t block the execution of the main page. Even if they trigger multiple style re-calculations, their tiny iframes have very little DOM.
* [MathJax Docs](http://docs.mathjax.org/en/latest/){:target="_blank"}
* [SO: AMP support for Latex Maths](https://stackoverflow.com/questions/41095862/accelerated-mobile-pages-support-for-latex-maths){:target="_blank"}
* [How can we implement MathJax in AMP website](https://support.google.com/webmasters/thread/2334051?hl=en){:target="_blank"}
* [SO: How  can we implement MathJax in AMP website](https://stackoverflow.com/questions/55137996/how-can-we-implement-mathjax-in-amp-website){:target="_blank"}
* [Add support for MathML](https://github.com/ampproject/amphtml/issues/12800){:target="_blank"}


## MathML

* 無法用latex表達數學公式
* 列示XML的markup language，不適合人去直接讀寫
* [Mathematical Markup Language](https://www.w3.org/Math/whatIsMathML.html){:target="_blank"}
* [`github: mathml.js`](https://github.com/ampproject/amphtml/blob/master/3p/mathml.js){:target="_blank"}
* [`amp-mathml`](https://amp.dev/documentation/components/amp-mathml/?referrer=ampproject.org){:target="_blank"}