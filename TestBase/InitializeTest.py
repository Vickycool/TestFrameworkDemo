from appium import webdriver


def init_driver():
    desired_capabilities = {}
    desired_capabilities['platformName'] = 'Android'
    desired_capabilities['platformVersion'] = '5.1'
    desired_capabilities['deviceName'] = '192.168.56.101:5555'
    desired_capabilities['noReset'] = 'true'
    # app的信息
    desired_capabilities['appPackage'] = 'com.android.contacts'
    desired_capabilities['appActivity'] = '.activities.PeopleActivity'
    # 中文输入允许
    desired_capabilities['unicodeKeyboard'] = True
    desired_capabilities['resetKeyboard'] = True
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_capabilities)
    return driver

