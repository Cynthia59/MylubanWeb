from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep


class login(Page):
    '''用户登录页面'''

    url = '/#/login'

    #登录输入控件
    login_username_loc = (By.XPATH, "//*[@placeholder='请输入鲁班通行证账号或手机号']")
    login_password_loc = (By.XPATH, "//*[@placeholder='请输入密码']")
    login_button_loc = (By.ID, "loginPer")
    
    # 登录用户名
    def login_username(self, username):
        self.fine_element(*self.login_username_loc).send_keys(username)
        
    # 登录密码
    def login_password(self, password):
        self.fine_element(*self.login_password_loc).send_keys(password)
        
    # 登录按钮
    def login_button(self):
        self.fine_element(*self.login_button_loc).click()
        
    # 定义统一登录入口
    def user_login(self, username="username", password="1111"):
        """获取的用户名密码登录"""
        self.open()
        sleep(1)
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(1)

    #登录验证控件
    user_pwd_empty_hint_loc = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[1]/form/div/div[4]/p[2]")
    user_pwd_error_hint_loc = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[1]/form/div/div[4]/p[1]")
    user_login_success_loc = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/ul/li[1]")

    # 用户名密码为空提示
    def user_pwd_empty_hint(self):
        return self.fine_element(*self.user_pwd_empty_hint_loc).text
    
    # 用户名密码错误提示
    def user_pwd_error_hint(self):
        return self.fine_element(*self.user_pwd_error_hint_loc).text
    
    # 登录成功用户名
    def user_login_success(self):
        return self.fine_element(*self.user_login_success_loc).text