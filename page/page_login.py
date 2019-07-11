import page
from base.base import Base


class PageLogin(Base):
    # 点击登录连接
    def page_click_login_link(self):
        self.base_click(page.login_link)

    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # 输入验证码
    def page_input_verify_code(self, code):
        self.base_input(page.login_verify_code, code)

    # 点击登录按钮
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    # 获取 异常提示信息
    def page_get_err_info(self):
        return self.base_get_text(page.login_err_info)

    # 点击 异常提示框 确定按钮
    def page_click_err_ok_btn(self):
        self.base_click(page.login_err_btn)

    # 获取登录后的昵称
    def page_get_nickname(self):
        return self.base_get_text(page.login_nickname)

    # 点击安全退出
    def page_click_logout(self):
        self.base_click(page.login_logout)

    # 组合业务方法
    def page_login(self, username, pwd, code):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_input_verify_code(code)
        self.page_click_login_btn()
