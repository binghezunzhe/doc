# in test_fancy.py
from nose2.tools import params


@params("Sir Bedevere", "Miss Islington", "Duck")
def test_is_knight(value):
    assert value.startswith('Sir')


"""
运行命令：
nose2 -v --pretty-assert
预期输出：
test_fancy.test_is_knight:1
'Sir Bedevere' ... ok
test_fancy.test_is_knight:2
'Miss Islington' ... FAIL
test_fancy.test_is_knight:3
'Duck' ... FAIL

======================================================================
FAIL: test_fancy.test_is_knight:2
'Miss Islington'
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/mnt/ebs/home/sirosen/tmp/test_fancy.py", line 6, in test_is_knight
    assert value.startswith('Sir')
AssertionError

>>> assert value.startswith('Sir')

values:
    value = 'Miss Islington'
    value.startswith = <built-in method startswith of str object at 0x7f3c3172f430>
======================================================================
FAIL: test_fancy.test_is_knight:3
'Duck'
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/mnt/ebs/home/sirosen/tmp/test_fancy.py", line 6, in test_is_knight
    assert value.startswith('Sir')
AssertionError

>>> assert value.startswith('Sir')

values:
    value = 'Duck'
    value.startswith = <built-in method startswith of str object at 0x7f3c3172d490>
----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=2)
"""
