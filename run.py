import pytest

if __name__ == '__main__':
    pytest.main(['-v', '-s', '--alluredir', './report/allure', 'testcase/'])