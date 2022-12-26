<h3>Description</h3>
<b>Project goal:</b> to write and automate no less than 5 test-cases per team member ✅
  <h4>Tech Stack</h4>
  <ul>
    <li><a href="https://docs.python.org/3/library/unittest.html">Unit Testing Framework (unittest library)</a></li>
    <li><a href="https://selenium-python.readthedocs.io/getting-started.html">Selenium Web Driver (selenium library)</a></li>
    <li><a href="https://selenium-python.readthedocs.io/page-objects.html">Page Object Model as project structure</a></li>
    <li><a href="https://docs.qameta.io/allure/">Allure Framework (allure-pytest library)</a></li>
  </ul>
<hr>
<h3>Tests Execution</h3>
<span>:warning: To run the project first make sure you have python installed in your system if not please install python</span>
<ol>
  <li>Clone the repository to your local machine</li>
  <li>Create venv with the command <sub>python -m venv venv</sub> and activate it</li>
  <li>Install all the necessary packages with the command <sub>pip install -r requirements.txt</sub></li>
  <li>Run all tests with <sub>python -m unittest</sub> or particular with <sub>python -m unittest [test_suite].[test]</sub></li>
  <li>Alternatively run all tests with <sub>pytest [test_suite]</sub> or particular with <sub>pytest [test_suite]/[test].py</sub></li>
</ol>
<hr>
<h3>Allure Reports</h3>
<ol>
  <li>Install allure library with the command <sub>pip install allure-pytest</sub></li>
  <li>Install JDK and add it to the <a href="https://www.youtube.com/watch?v=104dNWmM6Rs">Path</a></li>
  <li>Install <a href="https://scoop.sh/">scoop</a> via PowerShell</li>
  <li>Install Alure command line with <sub>scoop install allure</sub> command in PowerShell</li>
  <li>Create a directory for reports with the command <sub>pytest --alluredir [dir]</sub></li>
  <li>Run tests to generate reports with <sub>python -m pytest [full path to file]  --alluredir [dir]</sub></li>
  <li>View reports with <sub>allure serve [full path to dir]</sub></li>
</ol>
