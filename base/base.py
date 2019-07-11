from selenium.webdriver.support.wait import WebDriverWait

from tool.get_log import GetLog

log = GetLog().get_log()

class Base:
    # 初始化
    def __init__(self, driver):
        self.driver = driver
        log.info("正在获取driver对象：{}".format(driver))

    # 查找 封装
    def base_find(self, loc, timeout=30, poll=0.5):
        log.info("正在查找 {} 元素".format(loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击 封装
    def base_click(self, loc):
        self.base_find(loc).click()

    # 输入 封装
    def base_input(self, loc, value):
        # 获取元素
        el = self.base_find(loc)
        # 清空
        el.clear()
        # 输入
        el.send_keys(value)

    # 截图
    def base_get_img(self):
        self.driver.get_screenshot_as_file("./image/fial.png")

    # 获取文本信息
    def base_get_text(self, loc):
        return self.base_find(loc).text
