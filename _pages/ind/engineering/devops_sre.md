---
layout: default
title: DevOps & Site Reliability
lang: ind
description: How we run DevOps.
---



* Production monitoring and troubleshooting is the responsibility of DevOps / SRE.
* DevOps is responsible for escalating issues and bugs to the relevant engineer.

# Tools

The major tool categories include: 

* **Version control:** Tools that track software versions as they are released, whether manually or automatically. This means numbering versions, as well as tracking the configuration and any environmental dependencies that are present, such as the type, brand, and version of the database; the operating system details; and even the type of physical or virtual server that’s needed. This category is related to change management tools.
* **Build and deploy:** Tools that automate the building and deployment of software throughout the DevOps process, including continuous development and continuous integration.
* **Functional and non-functional testing:** Tools that provide automated testing, including best practices listed above. Testing tools should provide integrated unit, performance, and security testing services. The objective should be end-to-end automation.
* **Provisioning and change management:** Tools to provision the platforms needed for deployment of the software, as well as monitor and log any changes occurring to the configuration, the data, or the software. These tools ensure that you can get the system back to a stable state, no matter what occurs. 

# Best Practices

## 1. Test Automation
In order to compose quality code, developers need to test the software regularly. DevOps allows for early testing that gives developers an opportunity to identify and resolve the issue during software development rather than later in the process.

Automated testings allow for quicker execution of SDLC (Software Development Life Cycle) in comparison to manual testings. Test automation can be applied to the database and networking changes, middleware configurations, and code development using regression testing and load testing.

Test automation can be accomplished by performing varied activities such as identifying test scenarios and cases, choosing the right set of tools for automation, setting up an appropriate test environment, running test cases and analyzing results.  

## 2. Integrated Configuration Management
Configuration and change management are integral parts of the operations. Configuration management is about automation, monitoring, management and maintenance of system-wide configurations that take place across networks, servers, application, storage, and other managed services.

Integrated configuration management enables the development teams with a bigger picture. It allows to utilize the existing services during the software development rather than investing time and efforts in reinventing the new services from scratch.

## 3. Integrated Change Management
Change management is a process in which configurations are changed and redefined to meet the conditions of dynamic circumstances and new requirements. During the configuration management, if any changes are required then change management comes into the picture. The operations teams provide their inputs on what opportunities and consequences the change might expose at the wider level and what other systems could be impacted.  

## 4. Continuous Integration
It is a DevOps software development practice where the development team regularly updates the code changes in the repository after which the automated builds and tests run. Continuous Integration practices allow developers to carry out integrations sooner and frequently. Whereas CI tools help them to detect the integration challenges in new and existing code and solve them at the earlier phase only. Thus, CI improves collaborations amongst the teams and ultimately builds a high-quality software product.

## 5. Continuous Delivery
Continuous Delivery is a DevOps practice where the newly developed code is updated by developers, get tested by the QA team at the different stages by applying both automated and manual testings, and once the case passes all the testings, it gets into the production. It allows the development team to build, test and release the application faster and frequently, in short cycles.

It helps organizations to increase the number of deliveries, reduce manual works, minimize the risk of failure during production, and more.

## 6. Continuous Deployment
The deployment process contains varied sub-processes such as code creation, testing, versioning, deployment, post-deployment, etc. In the continuous deployment process, the code is automatically deployed in the production environment once it successfully passes all the test cases in QA, UAT, and other environments. A lot of tools available that perform continuous deployment start from staging to production with minimum human intervention.  

## 7. Application Monitoring
App infrastructure monitoring is very crucial to optimize the application performance, whether it is deployed on the cloud or local data center. If a bug hits the application during the release process, then it will be turned into the failure. So, it is very important for the development teams and operations teams to consider proactive monitoring and check the performance of the application. Various tools are available for application monitoring that offer a lot of metrics related to applications, infrastructure, sales, graphs, analytics, etc.

## 8. Automated Dashboards
Leverage the DevOps intelligence with the automated dashboard. It will provide the data along with detailed insights and reports of every operation such as the number of tests run, tests’ durations, the number of failure and success in testing. It allows to review configuration changes made to the database and server and deployments that have taken place across the system.  

The dashboard acts as a centralized hub that enables the operations team with real-time data insights which help them in selecting the right set of automation tools testings. Moreover, there are varied logs, graphs, and metrics that enable operations teams with a holistic view of changes happening in the system.