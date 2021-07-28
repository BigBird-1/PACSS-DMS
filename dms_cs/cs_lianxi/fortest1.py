import unittest


class ForTest1(unittest.TestCase):
    def setUp(self) -> None:
        print("用例初始化")

    def tearDown(self) -> None:
        print("用例清理")

    def test_1(self):
        print(111)

    def test_2(self):
        print(222)


# if __name__ == '__main__':
    #  unittest.main()

