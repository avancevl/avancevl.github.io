---
layout: default
title: Breaking Changes
lang: vi
description: How to notify breaking changes.
---



## Principles

1. Unit Test, Regression Test can never catch all bugs.
1. Merge, Pull Request are time consuming in terms of engineering hours. Likewise, cannot guarantee no breaking changes。

## Breaking Changes

* Database schema changes
* Another engineer's code
* Code that another engineer depends on.

## Notifying of Break Changes

Please notify everyone in the `#0-scrum` channel:

> 1. What you changed
> 2. Commit version
> 3. Commit time
> 4. Things that could be effected
> 5. If some does indeed break, what to try or look for in order to fix the change.