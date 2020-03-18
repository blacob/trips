import os
import pytest

pytest_plugins = ['pytester']

result = os.system('python3 root.py input.txt')
print(result)

# @pytest.fixture
# def run(testdir):
#     def do_run(*args):
#         args = ["pyconv"]  list(args)
#         return testdir._run(*args)
#     return do_run
#
# def test_trips(tmpdir, run):
#     input = tmpdir.join("input.txt")
#     content
#
#     #with input.open("wb") as f:
#
#     result = run(tmpdir)
#    a
