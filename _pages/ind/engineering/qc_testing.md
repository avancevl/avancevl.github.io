---
layout: default
title: Quality Control & Testing
lang: ind
description: How we do QC and testing.
---



## General Principles

* Testing should be done by a different person than the one who wrote the code.
* Therefore, testing is the responsiblity of QC / QA Engineers, and not the developers.
* QC Engineers will write automated tests that run after each pull request into the main branch.

<br>
<br>

## Test Pyramid

[**Martin Fowler**](https://martinfowler.com/bliki/TestPyramid.html){:target="_blank"}

> The test pyramid is a way of thinking about different kinds of automated tests should be used to create a balanced portfolio. Its essential point is that you should have many more low-level **UnitTests** than high level **BroadStackTests** running through a GUI.
>
> For much of my career test automation meant tests that drove an application through its user-interface. Such tools would often provide the facility to record an interaction with the application and then allow you to play back that interaction, checking that the application returned the same results. Such an approach works well initially. It's easy to record tests, and the tests can be recorded by people with no knowledge of programming.
> 
> But this kind of approach quickly runs into trouble, becoming an **ice-cream cone**. Testing through the UI like this is slow, increasing build times. Often it requires installed licences for the test automation software, which means it can only be done on particular machines. Usually these cannot easily be run in a "headless" mode, monitored by scripts to put in a proper deployment pipeline.

### Unit Tests

Unit tests are the category of tests that have wider acceptance regarding the naming and what they mean. They are the tests that accompany the source code and have direct access to it. Usually they are executed with an **Unit framework** or similar library. These tests work directly on the source code and have full view of everything. A single class/method/function is tested (or whatever is the smallest possible working unit for that particular business feature) and anything else is mocked/stubbed.

### Integration Tests

Integration tests (also called service tests, or even component tests) focus on a whole component. A component can be a set of classes/methods/functions, a module, a subsystem or even the application itself. They examine the component by passing input data and examinining the output data it produces. Usually some kind of deployment/bootstrap/setup is required first. External systems can be mocked completely, replaced (e.g. using an in-memory database instead of a real one), or the real external dependency might be used depending on the business case. Compared to unit tests they may require more specialized tools either for preparing the test environment, or for interacting/verifying it.

The second category suffers from a blurry definition and most naming controversies regarding testing start here. The “scope” for integration tests is also highly controversial and especially the nature of access to the application (black or white box testing and whether mocking is allowed or not).

As a basic rule of thumb if

* a test uses a database
* a test uses the network to call another component/application
* a test uses an external system (e.g. a queue or a mail server)
* a test reads/writes files or performs other I/O
* a test does not rely on the source code but instead it uses the deployed binary of the app

…then it is an integration test and not a unit test.

With the naming out of the way, we can dive into the list. The order of anti-patterns roughly follows their appearance in the wild. Frequent problems are gathered in the top positions.

### End-to-End (E2E) Tests

Even with both unit tests and integration tests, you probably still will want a small number of end-to-end tests to verify the system as a whole. To find the right balance between all three test types, the best visual aid to use is the testing pyramid.

The bulk of your tests are unit tests at the bottom of the pyramid. As you move up the pyramid, your tests gets larger, but at the same time the number of tests (the width of your pyramid) gets smaller.

As a good first guess, Google often suggests a 70/20/10 split: 70% unit tests, 20% integration tests, and 10% end-to-end tests. The exact mix will be different for each team, but in general, it should retain that pyramid shape. Try to avoid these anti-patterns:

* **Inverted pyramid/ice cream cone.** The team relies primarily on end-to-end tests, using few integration tests and even fewer unit tests. 
* **Hourglass.** The team starts with a lot of unit tests, then uses end-to-end tests where integration tests should be used. The hourglass has many unit tests at the bottom and many end-to-end tests at the top, but few integration tests in the middle.

Just like a regular pyramid tends to be the most stable structure in real life, the testing pyramid also tends to be the most stable testing strategy.

<br>
<br>

## Software Testing Anti-pattern

Read this excellent resource on [**Testing Anti-Patterns**](http://blog.codepipes.com/testing/software-testing-antipatterns.html){:target="_blank"} first.

1. Having unit tests without integration tests
1. Having integration tests without unit tests
1. Having the wrong kind of tests
1. Testing the wrong functionality
1. Testing internal implementation
1. Paying excessive attention to test coverage
1. Having flaky or slow tests
1. Running tests manually
1. Treating test code as a second class citizen
1. Not converting production bugs to tests
1. Treating Test Driven Design (TDD) as a religion
1. Writing tests without reading documentation first
1. Giving testing a bad reputation out of ignorance