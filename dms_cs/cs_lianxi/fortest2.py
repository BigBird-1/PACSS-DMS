import unittest


class ForTest2(unittest.TestCase):
    def setUp(self) -> None:
        print("用例初始化")

    def tearDown(self) -> None:
        print("用例清理")

    def test_3(self):
        print(333)

    def test_4(self):
        print(444)


# if __name__ == '__main__':
#     unittest.main()