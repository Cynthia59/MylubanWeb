#encoding: utf-8
"""
@project = MylubanWeb
@file = run_test
@function = 
@author = Cindy
@create_time = 2018/6/12 9:19
@python_version = 3.x
"""

import unittest, os, time, sys
from HTMLTestRunner import HTMLTestRunner
sys.path.append("./testcase")
sys.path.append("./report")

# 指定测试用例为当前文件夹下的testcase目录
test_dir = './testcase'
# discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    filename = './report/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='myluban web test', description='用例执行情况：')
    # runner.run(discover)
    fp.close()

