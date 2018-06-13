from selenium import webdriver
import os, shutil

# 截图函数
def insert_img(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('/testcase')[0]
    file_path = base + "/report/image/" + file_name + ".png"
    driver.get_screenshot_as_file(file_path)

# 查找最新的测试报告
def latest_report():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('/testcase')[0]
    result_dir = base + "/report"
    lists = os.listdir(result_dir)
    # 重新按时间对目录下的文件进行排序
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn))
    print('最新的文件为： ' + lists[-1])
    file = os.path.join(result_dir, lists[-1]).replace('\\','/')
    print(file)
    return file

#复制最新的测试报告
def copy_latest_report():
    old = latest_report()
    new = old.split('/20')[0] + '/new_report.html'
    shutil.copyfile(old, new)
    print('copy done!')

    
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    insert_img(driver, 'baidu')
    driver.quit()
    copy_latest_report()