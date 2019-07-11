from selenium.webdriver.common.by import By
"""服务器地址"""
url = "http://localhost"
"""以下配置数据为登录配置数据"""
# 点击登录连接
login_link = By.LINK_TEXT, "登录"
# 用户名
login_username = By.CSS_SELECTOR, "#username"
# 密码
login_pwd = By.CSS_SELECTOR, "#password"
# 验证码
login_verify_code =By.CSS_SELECTOR, "#verify_code"
# 登录按钮
login_btn = By.CSS_SELECTOR, ".J-login-submit"
# 异常提示信息
login_err_info = By.CSS_SELECTOR, ".layui-layer-content"
# 异常提示框确定
login_err_btn = By.CSS_SELECTOR, ".layui-layer-btn0"
# 获取昵称
login_nickname = By.CSS_SELECTOR, ".userinfo"
# 安全退出
login_logout = By.LINK_TEXT, "安全退出"