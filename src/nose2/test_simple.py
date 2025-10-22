# in test_simple.py
# 参考：https://docs.nose2.io/en/latest/
import unittest


class TestStrings(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("spam".upper(), "SPAM")


"""
运行命令：
nose2 -v
预期输出：
test_upper (test_simple.TestStrings) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
"""
