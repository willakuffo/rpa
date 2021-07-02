# RPA  - robotic process automation - Python - Selenium

## Task: Google form fill automation
This task invloves automating the process of filling a google form using python selenium's webdriver. The form given requires exactly one response from each respondent
therefore, a google sign in into a gmail account is required.

![image](https://user-images.githubusercontent.com/47186373/124250701-a6d8ff80-db14-11eb-92b3-5b842005a931.png)



### Clone repository
~~~console
git clone https://github.com/willakuffo/rpa
~~~

### Install Dependencies

* ### [Chrome webdriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

Utilizing Google Chrome, download [webdriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) for google chrome


* ### [Selenium](https://pypi.org/project/selenium/)
Python language bindings for Selenium WebDriver.

The selenium package is used to automate web browser interaction from Python.
```
pip install selenium
```

* ### [Undetected-Chromedriver](https://pypi.org/project/undetected-chromedriver/)
Optimized Selenium Chromedriver patch which does not trigger anti-bot services like Distill Network / Imperva / DataDome / Botprotect.io Automatically downloads the driver binary and patches it. 

```
pip install undetected-chromedriver
```

This is required because selenium's default webdriver is not able to bypass Google's antibot services during sign in which is also required before the form can be filled.
Therefore do

```python
import undetected_chromedriver.v2 as uc
driver = uc.Chrome(executable_path = google-chrome-webdriver-executable-path)
```
which is able to bypass google's antibot services and bring up the password page
![image](https://user-images.githubusercontent.com/47186373/124255539-cd4d6980-db19-11eb-9b1c-11d64adb747c.png)

instead of

```python
from selenium import webdriver
driver = webdriver.Chrome(executable_path = google-chrome-webdriver-executable-path)
```

![image](https://user-images.githubusercontent.com/47186373/124257224-b27bf480-db1b-11eb-8871-838366f6e063.png)




### change dir 
```
cd rpa
```

### run `formfill.py` in terminal
~~~
python formfill.py
~~~
![image](https://user-images.githubusercontent.com/47186373/124242496-5198f000-db0c-11eb-94bb-5c6a505304b9.png)
* Enter gmail email address and password for Google sign in requirement. This is to ensure that exactly one response is obtained 
 from each person by linking account to person.
* At this point, your chrome browser should be open and waiting
* Press Enter and observe automation
 


https://user-images.githubusercontent.com/47186373/124245279-60cd6d00-db0f-11eb-8052-57ad2ea0865e.mp4




