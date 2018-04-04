# coding=utf-8
import time
import unittest

import HTMLTestRunner
import SendEmail_html_file

# 用例目录
test_suite_dir = r'H:\test_project\\'
# test_suite_dir=r'/opt/openapi/'  #145部署环境
# 报告目录
Report_dir = r'H:\test_project\report\\'


# Report_dir=r'/opt/openapi/Report/'  #145部署环境
def creatsuite():
    testunit = unittest.TestSuite()
    # 定义测试文件查找的目录
    test_dir = test_suite_dir
    # 定义 discover 方法的参数
    package_tests = unittest.defaultTestLoader.discover(test_dir,
                                                        pattern='Test*.py',
                                                        top_level_dir=None)
    # package_tests=TestLoader.discover(start_dir=test_dir, pattern='Test*.py')
    # discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in package_tests:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit


alltestnames = creatsuite()

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    test_report = Report_dir
    filename = test_report + now + 'result.html'
    print filename
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'chenyz测试报告',
        description=u'测试用例执行结果'
    )

    runner.run(alltestnames)
    fp.close()
    new_report = SendEmail_html_file.new_report(test_report)
    SendEmail_html_file.send_file(new_report)  # 发送测试报告