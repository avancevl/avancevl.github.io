# AVL Handbook | All Remote Startup Accelerator

> https://avancevl.github.io/

<br>

# About Us

## A Different Breed of Startup Incubator

We incubate, accelerate, and implement ideas that our team create internally.

## Work From Home

We're a 100% remote company. Work from anywhere in the world.

## Radical Transparency 

We believe in radical transparency, where the best ideas win. As such, how we run the company is [open sourced to the world](https://github.com/avancevl/avancevl.github.io). In this central repository, you will find all the information you need to understand what it is like to work here. All the information available to our employees is also available to you. We encourage you to learn more about us here at this depository. 

## Work with the best people

We want to work with talented individuals and are **always actively hiring**.

[Explore opportunities](https://avancevl.github.io/recruit/recruit.html)

## Open Feedback

We welcome feedback.
* Please make a [pull request](https://github.com/avancevl/avancevl.github.io/pull/new/master) to suggest improvements or add clarification.
* Please create a [issue](https://github.com/avancevl/avancevl.github.io/issues/new) to ask questions.

## Community

Help us support the open source, startup, developer communites in Taiwan by following:

* [Startup Jobs Taiwan :rocket:](https://021tw.github.io/)
* [Full Stack Developers Taiwan :star:](https://stacktw.github.io/)

<br>

# How To Build

1. Install Homebrew
    1. `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`
1. Install the latest version of Python3.
    1. `brew install python`
1. Install `pip`.
    1. `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
    1. `python3 get-pip.py`
1. Install Python packages.
    1. `pip install beautifulsoup4`
    1. `pip install python-frontmatter`
1. Edit markdown files in `_main` folder, **DO NOT** edit files in `_page` folder.
1. Run `python3 i18n.py` to generate language specific markdown files in `_page` folder.
1. Commit and push to deploy to [avancevl.github.io](https://avancevl.github.io)