from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.loginPage import login


class loginTest(myunit.MyTest):
    """myluban登录测试"""
    def user_login_verify(self, username="", password=""):
        login(self.driver).user_login(username, password)

    def test_login1(self):
        """用户名、密码为空登录"""
        self.user_login_verify()
        po = login(self.driver)
        self.assertEqual(po.user_pwd_empty_hint(), "提示：请输入鲁班通行证账号或密码")
        function.insert_img(self.driver, "user_pwd_empty")

    def test_login2(self):
        """用户名正确、密码为空登录"""
        self.user_login_verify(username="pytest")
        po = login(self.driver)
        self.assertEqual(po.user_pwd_empty_hint(), "提示：请输入鲁班通行证账号或密码")
        function.insert_img(self.driver, "pwd_empty")

    def test_login3(self):
        """用户名为空、密码正确登录"""
        self.user_login_verify(password="abc123456")
        po = login(self.driver)
        self.assertEqual(po.user_pwd_empty_hint(), "提示：请输入鲁班通行证账号或密码")
        function.insert_img(self.driver, "user_empty")

    def test_login4(self):
        """用户名与密码不匹配"""
        character = random.choice('zyxwvutsrqponmlkjihgfedcba')
        username = "cynthia" + character
        self.user_login_verify(username=username, password="cynthia123456")
        po = login(self.driver)
        self.assertEqual(po.user_pwd_error_hint(), "提示：账户名或者密码错误!")
        function.insert_img(self.driver, "user_pwd_error")

    def test_login5(self):
        """用户名、密码正确"""
        self.user_login_verify(username="cynthia", password="cynthia123456")
        sleep(2)
        po = login(self.driver)
        self.assertEqual(po.user_login_success(), "桌面")
        function.insert_img(self.driver, "user_pwd_true")
        
if __name__ == "__main__":
    unittest.main()