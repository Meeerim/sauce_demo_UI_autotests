## UI Autotests project for SwagLabs. saucedemo.com
An example of a clothing store maintained by people from SauceLab.
This site is suitable for multi-page test scenarios, category filtering, and shipping cart testing.
### <img width="5%" title="SwagLabs" src="images/sauce.png"> 


### Tools and a technologies used
<p  align="center">
<code><img width="5%" title="Python" src="images/python.png"></code>
<code><img width="5%" title="Pycharm" src="images/pycharm.png"></code>
<code><img width="5%" title="Pytest" src="images/pytest.png"></code>
<code><img width="5%" title="Selene" src="images/selene.png"></code>
<code><img width="5%" title="Selenium" src="images/selenium.png"></code>
<code><img width="5%" title="Allure Report" src="images/allure_report.png"></code>
<code><img width="5%" title="Allure TestOps" src="images/allure_testops.png"></code>
<code><img width="5%" title="Jenkins" src="images/jenkins.png"></code>
<code><img width="5%" title="Selenoid" src="images/selenoid.png"></code>
<code><img width="5%" title="Telegram Bot" src="images/tg.png"></code>
<code><img width="5%" title="GitHub" src="images/github.png"></code>
</p>
<br> 

### Specific scenarios that were checked
* Successful Cart Checkout with Valid User details
* Unsuccessful Login with Incorrect Password
* Successful Login of User with valid credentials
* Verify that users can proceed to the checkout page from the cart page
* Verify that users can remove items from the cart and the cart updates accordingly
* Verify that users can add items to the cart and the cart updates accordingly
<br>

<!-- Jenkins -->

### <img width="3%" title="Jenkins" src="images/jenkins.png"> Running tests from Jenkins
### [Job](https://jenkins.autotests.cloud/job/meerim_final_diplom_project_web/)
##### Main page of the build:
![This is an image](images/screenshots/jenkins.png)
##### After the build is done the test results are available in Allure Report and Allure TestOps


<!-- Allure report -->

### <img width="3%" title="Allure Report" src="images/allure_report.png"> Allure report
##### From main page of Allure report can see  :

>- <code><strong>*ALLURE REPORT*</strong></code> -date and time of the test, overall number of launched tests,
>- <code><strong>*TREND*</strong></code> - trend of running tests for all runs
>- <code><strong>*SUITES*</strong></code> - distribution of tests by suites
>- <code><strong>*CATEGORIES*</strong></code> - distribution of unsuccessful tests by defect types

![This is an image](images/screenshots/allure_testops_dashboard.png)


##### On the page the list of the tests grouped by suites with status shown for each test.
![This is an image](images/screenshots/allure_report_suites.png)

#### For each tests attachments of test results attached.Such as screenshots, page source, browser logs and video 

### Video result of one of the tests
<img src="images/screenshots/video.gif" alt="video test" border="0" />


<!-- Allure TestOps -->

### <img width="3%" title="Allure TestOps" src="images/allure_testops.png"> Allure TestOps Integration
### [Dashboard](https://allure.autotests.cloud/project/3584/dashboards)
##### Results are uploaded there and the automated test-cases can be automatically updated accordingly to the recent changes in the code.
![This is an image](images/screenshots/allure_testops_dashboard.png)

Allure TestOps allows you to run automated tests and see the result of their execution. 
In this case, you can choose exactly what tests to run. 
They also include all members of the council who can use tests for their own needs.
Test-cases in the project are imported and constantly updated from the code,
so there is no need in complex process of synchronization manual test-cases and autotests.

![This is an image](images/screenshots/allure-suites.png)


<!-- Telegram -->

### <img width="3%" title="Telegram" src="images/tg.png"> Telegram Notifications
##### Telegram bot sends a brief report to a specified telegram chat by results of each build.

![This is an image](images/screenshots/tg_bot.png)



