[//]:由于他要一步步深入概念，导致节奏拖拉，不能一下子给读者反馈，我很不喜欢这样的写法，
# Selenium 简单使用
## pip安装

    pip install selenium

## 下载浏览器驱动
Selenium 需要通过浏览器驱动来控制浏览器。
不同的浏览器需要不同的驱动，以下是常见浏览器的驱动下载地址：
<!--作者写的时候，不考虑不会翻墙的读者吗？不知道为什么许多作者默认使用谷歌浏览器，也许谷歌浏览器是最好浏览器，但是国外作者就算了，国内作者也完全一点不考虑国内小白读者的感受-->

* Chrome: ChromeDriver，ChromeDriver 的说明参见：
* Firefox: GeckoDriver
* Edge: EdgeDriver
下载适合你浏览器版本的驱动，并将其路径添加到系统的环境变量中，或者将驱动文件放在 Python 脚本所在的目录下。

## 简单使用 Selenium

### 一个简单的基本流程
安装好 Selenium 和浏览器驱动后，我们就可以开始编写自动化脚本了。
以下是一个简单的示例，展示如何使用 Selenium 打开一个网页并获取页面标题。
<!--我想先整理出一个框架，再来详细说明-->
- 导入selenium、除了导入驱动外、还有导入webdriver其他库
- 配置service、配置驱动文件路径
- get()，响应网站、
- 等待
- 元素定位
- 元素操作
- 关闭浏览器

1、导入 Selenium
首先，我们需要在 Python 脚本中导入 Selenium 的 webdriver 模块：

    from selenium import webdriver
2、启动浏览器
接下来，我们需要启动一个浏览器实例，本系列会以 Edge 为例。#由于国内网络原因，我们采用edge

    driver = webdriver.Edge(executable_path='/path/to/msedgedriver')#文件路径
选择浏览器并初始化 WebDriver：

    实例
    from selenium import webdriver

    # 使用 Chrome 浏览器
    driver = webdriver.Edge(executable_path='/path/to/edgedriver')

    # 或者使用 Firefox 浏览器
    # driver = webdriver.Firefox(executable_path='/path/to/geckodriver')

    # 或者使用 谷歌 浏览器
    # driver = webdriver.Chrome(executable_path='path/to/chromedriver')
从 Selenium 4 开始，在浏览器驱动的管理方式上发生了变化：Selenium 4 尝试自动检测系统中安装的浏览器版本，并下载相应的驱动程序，这意味着用户不再需要手动下载和设置驱动程序路径，除非他们需要特定版本的驱动程序。

实例
    from selenium import webdriver

    driver = webdriver.Edge()  # 如果使用其他浏览器，如 Firefox，需要相应修改
当国内的网络环境，自动检测下载驱动需要不一样的网络环境，所以建议手动下载驱动，然后指定驱动路径。
#因为他采用的是谷歌浏览器，个人感觉不需要service对象设置就很好了。

在 Selenium 4 中，不再直接在 webdriver.Chrome 中设置驱动程序路径，而是通过引入 Service 对象来设置。这样可以避免弃用警告，并确保驱动程序的正确加载。#他这里采取Service对象来设置，他说是为了避免弃用警告，弃用警告那是什么东西？
例如：
实例

    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService

    service = ChromeService(executable_path="PATH_TO_DRIVER")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
如果你将 chromedriver 放在了系统路径中，或者将其放在了 Python 脚本所在的目录下，可以省略 executable_path 参数：

  
3、打开网页
使用 get 方法打开一个网页：

    driver.get('https://www.baidu.com')
4、获取页面标题
我们可以使用 title 属性来获取当前页面的标题：

    print(driver.title)
5、关闭浏览器
完成操作后，记得关闭浏览器：

    driver.quit()
6、完整示例
将以上步骤组合起来，完整的代码如下：

实例
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService

    # 设置正确的驱动路径
    service = ChromeService(executable_path="/RUNOOB/Downloads/chromedriver-mac-arm64/chromedriver")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)


    # 打开一个网站
    driver.get("https://www.baidu.com")

    # 获取页面标题
    print(driver.title)

    # 关闭浏览器
    driver.quit()
以上代码执行成功后，会打开浏览器，并打开网页，如下所示：

完成后，会输出网页标题：

    百度一下，你就知道

### 常见操作

除了打开网页和获取标题，Selenium 还支持许多其他操作。以下是一些常见的操作示例：

1、查找元素
可以使用 find_element 方法来查找页面上的元素。例如，查找一个输入框并输入文本：
实例

    input_element = driver.find_element('name', 'q')
    input_element.send_keys('Selenium')

2、点击按钮
可以使用 click 方法来点击按钮：
实例

    button_element = driver.find_element('name', 'btnK')
    button_element.click()

3、等待页面加载
有时页面元素不会立即加载完成，我们可以使用 WebDriverWait 来等待元素出现：

实例

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.NAME, 'q')))

* 使用 window.stop() 强制停止页面加载
有时候一个网页加载太慢，会导致异常出现，为了能够顺利抓取数据，可以让页面加载几秒后再通过执行 JavaScript 代码 window.stop()，强制停止页面加载。

实例
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

1、设置正确的驱动路径
service = ChromeService(executable_path="/RUNOOB/Downloads/chromedriver-mac-arm64/chromedriver")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

2、打开一个网站
driver.get("https://www.baidu.com")

3、 等待页面加载完成
time.sleep(2)  # 可以根据需要调整等待时间

4、强制停止页面加载
driver.execute_script("window.stop();")
5、 获取页面标题
print(driver.title)

6、 关闭浏览器
driver.quit()