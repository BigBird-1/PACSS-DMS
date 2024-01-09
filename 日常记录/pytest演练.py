import pytest


# 关于fixture函数的定义
@pytest.fixture
def first():
    print("测试用例执行前的操作")


# 使用fixture函数的测试用例
def test_1(first):
    print("执行测试用例")


# ----------------------------------------------------------------------------------------------------------------------
# Fixture名字作为测试用例的参数
@pytest.fixture
def first_entry():
    return "a"


@pytest.fixture
def order(first_entry):
    return [first_entry]


def test_2(order):
    order.append("b")
    assert order == ["a", "b"]


# ----------------------------------------------------------------------------------------------------------------------
# 使用@pytest.mark.usefixtures('fixture')装饰器,有返回值的获取不到
@pytest.fixture
def my_fruit():
    print("执行用例前的操作：登录")


@pytest.mark.usefixtures("my_fruit")
def test_3():
    print("执行测试用例")


# 使用autouse参数 指定fixture的参数autouse=True这样模块内的每个测试用例会自动调用fixture。有返回值的获取不到
@pytest.fixture(autouse=True)
def my_au():
    print("用户登录")


def test_4():
    print("hello world")


@pytest.fixture
def make_customer_record():
    def _make_customer_record(name):
        return {"name": name, "orders": []}

    return _make_customer_record  # 注意此处不加(),非函数调用


def test_5(make_customer_record):
    customer_1 = make_customer_record("Lisa")
    print(customer_1)
    assert customer_1 == {"name": "Lisa", "orders": []}


if __name__ == '__main__':
    pytest.main(['pytest演练.py::test_5', '-s', '-q'])
