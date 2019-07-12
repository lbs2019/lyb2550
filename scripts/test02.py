import pytest
import allure



class Test01():
    @allure.step(title = '我是测试步骤001')
    def test001(self):
        print("test01被执行")

    def test002(self):
        allure.attach("描述: ", "失败原因")
        print("test002被执行")


    def test03(self):
        with open("../image/fail.png", "rb") as f:
            allure.attach("失败原因: ",f.read(),allure.attach_type.PNG)