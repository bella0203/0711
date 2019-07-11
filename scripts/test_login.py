from time import sleep

import pytest
import sys
import os
sys.path.append(os.getcwd())




from tool.get_log import GetLog
from tool.read_txt import read_txt
from page.page_login import PageLogin
from tool.get_driver import GetDriver

log = GetLog().get_log()
def get_data():
    arrs = []
    for arr in read_txt():
        arrs.append(tuple(arr.strip().split(",")))
    return arrs[1::]


class TestLogin:
    # 初始化
    def setup_class(self):
        # 获取driver
        self.driver = GetDriver().get_driver()
        # 实例化PageLogin
        self.login = PageLogin(self.driver)
        # 点击登录连接
        self.login.page_click_login_link()

    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver().quit_driver()

    # 测试方法
    @pytest.mark.parametrize("username,pwd,code,expect_result, success", get_data())
    def test_login(self, username, pwd, code, expect_result,success):
        # 调用业务登录方法
        self.login.page_login(username, pwd, code)
        # 判断 正向
        if success == "true":
            try:
                # 断言 昵称
                assert expect_result == self.login.page_get_nickname()
            except Exception as e:
                # 截图 日志
                self.login.base_get_img()
                log.error(e)
                # 注意：一定要抛出异常
                raise
            finally:
                # 安全退出
                self.login.page_click_logout()
                sleep(3)
                # 点击登录连接
                self.login.page_click_login_link()
        # 否则 逆向
        else:
            try:
                # 断言 异常提示信息
                assert expect_result == self.login.page_get_err_info()
                # 点击 异常提示信息确定按钮
                self.login.page_click_err_ok_btn()
            except Exception as e:
                # 截图 日志
                self.login.base_get_img()
