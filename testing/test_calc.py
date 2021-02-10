"""
补全计算器（加减乘除）的测试用例，编写用例顺序：加-除-减-乘
创建 fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
将 fixture 方法存放在 conftest.py ，设置 scope=module
控制测试用例顺序按照【加-减-乘-除】这个顺序执行
结合 allure 生成本地测试报告
"""

import pytest
import yaml

from homework.python_code.calc import Calculator


class TestDemo():
    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    with open("./datas/calc.yaml") as f:
        s = yaml.safe_load(f)
        data_add = s['add']
        data_div = s['div']
        data_sub = s['sub']
        data_mul = s['mul']

        add_datas = data_add['datas']
        add_myids = data_add['myid']

        div_datas = data_div['datas']
        div_myids = data_div['myid']

        sub_datas = data_sub['datas']
        sub_myids = data_sub['myid']

        mul_datas = data_mul['datas']
        mul_myids = data_mul['myid']

    @pytest.mark.parametrize("a,b,expect", add_datas, ids=add_myids)
    # 加法
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        if isinstance(result, float):
            # isinstance() 函数来判断一个对象是否是一个已知的类型
            result = round(result, 2)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", div_datas, ids=div_myids)
    # 除法
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        if isinstance(result, float):
            # isinstance() 函数来判断一个对象是否是一个已知的类型
            result = round(result, 2)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", sub_datas, ids=sub_myids)
    # 减法
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        if isinstance(result, float):
            # isinstance() 函数来判断一个对象是否是一个已知的类型
            result = round(result, 2)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", mul_datas, ids=mul_myids)
    # 乘法
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)
        if isinstance(result, float):
            # isinstance() 函数来判断一个对象是否是一个已知的类型
            result = round(result, 2)
        assert result == expect
