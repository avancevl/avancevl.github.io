---
layout: default
title:  網頁可靠性
description: DevOps & Site Reliability
locales:
    zh-tw:
        title: 網頁可靠性
        description: 我們如何監控並解決網頁的錯誤
    zh-cn:
        title: 网页可靠性
        description: 我们如何监控并解决网页的错误
    en:
        title: DevOps & Site Reliability
        description: "How we run DevOps."
---

<a name="zh-tw"></a>

* 生產監控和故障排除是DevOps / SRE的責任。
* DevOps負責將問題和錯誤上報給相關工程師。

# 工具

主要工具類別包括：

* **版本控制：**跟踪軟件版本的工具，無論是手動還是自動。這意味著對版本進行編號，並跟踪配置和存在的任何環境相關性，例如數據庫的類型，品牌和版本。操作系統詳細信息；甚至是所需的物理或虛擬服務器的類型。此類別與變更管理工具有關。
* **構建和部署：**用於在整個DevOps流程中自動構建和部署軟件的工具，包括持續開發和持續集成。
* **功能和非功能測試：**提供自動測試的工具，包括上面列出的最佳實踐。測試工具應提供集成的單元，性能和安全性測試服務。目標應該是端到端自動化。
* **供應和變更管理：**用於提供部署軟件所需平台的工具，以及監視和記錄配置，數據或軟件發生的任何變更的工具。這些工具確保無論發生什麼情況都可以使系統恢復穩定狀態。

# 最佳做法

## 1.測試自動化

為了編寫高質量的代碼，開發人員需要定期測試軟件。 DevOps允許進行早期測試，這使開發人員有機會在軟件開發過程中而非過程的後期識別和解決問題。

與手動測試相比，自動測試可以更快地執行SDLC（軟件開發生命週期）。使用回歸測試和負載測試，可以將測試自動化應用於數據庫和網絡更改，中間件配置以及代碼開發。

可以通過執行各種活動來完成測試自動化，例如識別測試場景和案例，選擇正確的自動化工具集，設置適當的測試環境，運行測試案例以及分析結果。

## 2.集成配置管理

配置和變更管理是操作的組成部分。配置管理涉及跨網絡，服務器，應用程序，存儲和其他託管服務進行的系統範圍配置的自動化，監視，管理和維護。

集成的配置管理使開發團隊具有更廣闊的視野。它允許在軟件開發過程中利用現有服務，而不用花費時間和精力從頭開始重新發明新服務。

## 3.集成變更管理

變更管理是一個過程，在其中更改和重新定義配置以滿足動態情況和新要求的條件。在配置管理過程中，如果需要進行任何更改，那麼更改管理就會進入畫面。運營團隊就變更可能在更大的範圍內暴露出哪些機會和後果以及可能影響到哪些其他系統提供意見。

## 4.持續集成

這是DevOps軟件開發實踐，開發團隊會定期更新存儲庫中的代碼更改，然後運行自動構建和測試。持續集成實踐使開發人員可以更快，更頻繁地進行集成。 CI工具可幫助他們檢測新代碼和現有代碼中的集成挑戰，並僅在早期階段解決它們。因此，CI改善了團隊之間的協作，並最終構建了高質量的軟件產品。

## 5.持續交付

持續交付是DevOps的一種實踐，其中新開發的代碼由開發人員更新，通過自動和手動測試在不同階段由QA團隊進行測試，一旦案例通過所有測試，便進入生產。它使開發團隊可以在短週期內更快，更頻繁地構建，測試和發布應用程序。

它可以幫助組織增加交付數量，減少人工工作，將生產過程中發生故障的風險降到最低等。

## 6.持續部署

部署過程包含各種子過程，例如代碼創建，測試，版本控制，部署，後部署等。在連續部署過程中，一旦代碼成功通過了QA中的所有測試用例，代碼就會自動部署到生產環境中。 ，UAT和其他環境。許多執行連續部署的工具從階段到生產都需要最少的人工干預。

## 7.應用程序監視

無論是將其部署在雲還是本地數據中心上，應用程序基礎結構監視對於優化應用程序性能都至關重要。如果在發布過程中有bug擊中了應用程序，那麼它將變成失敗。因此，對於開發團隊和運營團隊而言，考慮主動監視並檢查應用程序的性能非常重要。各種工具可用於應用程序監視，這些工具提供了許多與應用程序，基礎架構，銷售，圖形，分析等相關的指標。

## 8.自動化儀表板

通過自動儀表板利用DevOps智能。它將提供數據以及每項操作的詳細見解和報告，例如運行的測試數量，測試的持續時間，測試失敗和成功的數量。它允許查看對數據庫和服務器所做的配置更改以及在系統中進行的部署。

儀表板充當集中式樞紐，使運營團隊能夠獲得實時數據見解，從而幫助他們選擇正確的自動化工具測試集。此外，還有各種日誌，圖形和度量標準，使操作團隊可以全面了解系統中發生的更改。


<a name="zh-cn"></a>

* 生产监控和故障排除是DevOps / SRE的责任。
* DevOps负责将问题和错误上报给相关工程师。

# 工具

主要工具类别包括：

* **版本控制：**跟踪软件版本的工具，无论是手动还是自动。这意味着对版本进行编号，并跟踪配置和存在的任何环境相关性，例如数据库的类型，品牌和版本。操作系统详细信息；甚至是所需的物理或虚拟服务器的类型。此类别与变更管理工具有关。
* **构建和部署：**用于在整个DevOps流程中自动构建和部署软件的工具，包括持续开发和持续集成。
* **功能和非功能测试：**提供自动测试的工具，包括上面列出的最佳实践。测试工具应提供集成的单元，性能和安全性测试服务。目标应该是端到端自动化。
* **供应和变更管理：**用于提供部署软件所需平台的工具，以及监视和记录配置，数据或软件发生的任何变更的工具。这些工具确保无论发生什么情况都可以使系统恢复稳定状态。

# 最佳做法

## 1.测试自动化

为了编写高质量的代码，开发人员需要定期测试软件。 DevOps允许进行早期测试，这使开发人员有机会在软件开发过程中而非过程的后期识别和解决问题。

与手动测试相比，自动测试可以更快地执行SDLC（软件开发生命周期）。使用回归测试和负载测试，可以将测试自动化应用于数据库和网络更改，中间件配置以及代码开发。

可以通过执行各种活动来完成测试自动化，例如识别测试场景和案例，选择正确的自动化工具集，设置适当的测试环境，运行测试案例以及分析结果。

## 2.集成配置管理

配置和变更管理是操作的组成部分。配置管理涉及跨网络，服务器，应用程序，存储和其他托管服务进行的系统范围配置的自动化，监视，管理和维护。

集成的配置管理使开发团队具有更广阔的视野。它允许在软件开发过程中利用现有服务，而不用花费时间和精力从头开始重新发明新服务。

## 3.集成变更管理

变更管理是一个过程，在其中更改和重新定义配置以满足动态情况和新要求的条件。在配置管理过程中，如果需要进行任何更改，那么更改管理就会进入画面。运营团队就变更可能在更大的范围内暴露出哪些机会和后果以及可能影响到哪些其他系统提供意见。

## 4.持续集成

这是DevOps软件开发实践，开发团队会定期更新存储库中的代码更改，然后运行自动构建和测试。持续集成实践使开发人员可以更快，更频繁地进行集成。 CI工具可帮助他们检测新代码和现有代码中的集成挑战，并仅在早期阶段解决它们。因此，CI改善了团队之间的协作，并最终构建了高质量的软件产品。

## 5.持续交付

持续交付是DevOps的一种实践，其中新开发的代码由开发人员更新，通过自动和手动测试在不同阶段由QA团队进行测试，一旦案例通过所有测试，便进入生产。它使开发团队可以在短周期内更快，更频繁地构建，测试和发布应用程序。

它可以帮助组织增加交付数量，减少人工工作，将生产过程中发生故障的风险降到最低等。

## 6.持续部署

部署过程包含各种子过程，例如代码创建，测试，版本控制，部署，后部署等。在连续部署过程中，一旦代码成功通过了QA中的所有测试用例，代码就会自动部署到生产环境中。 ，UAT和其他环境。许多执行连续部署的工具从阶段到生产都需要最少的人工干预。

## 7.应用程序监视

无论是将其部署在云还是本地数据中心上，应用程序基础结构监视对于优化应用程序性能都至关重要。如果在发布过程中有bug击中了应用程序，那么它将变成失败。因此，对于开发团队和运营团队而言，考虑主动监视并检查应用程序的性能非常重要。各种工具可用于应用程序监视，这些工具提供了许多与应用程序，基础架构，销售，图形，分析等相关的指标。

## 8.自动化仪表板

通过自动仪表板利用DevOps智能。它将提供数据以及每项操作的详细见解和报告，例如运行的测试数量，测试的持续时间，测试失败和成功的数量。它允许查看对数据库和服务器所做的配置更改以及在系统中进行的部署。

仪表板充当集中式枢纽，使运营团队能够获得实时数据见解，从而帮助他们选择正确的自动化工具测试集。此外，还有各种日志，图形和度量标准，使操作团队可以全面了解系统中发生的更改。


<a name="en"></a>

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