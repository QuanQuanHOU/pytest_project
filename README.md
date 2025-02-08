## 1. 环境准备

确保你已经安装了以下软件和库：

- Python 3.x：推荐使用Python 3.6及以上版本。
- Java JDK：用于Android开发。
- Android SDK：用于Android设备的调试。
- Node.js：用于运行Appium服务器。
- Appium：自动化测试工具。
- Appium-Python-Client：Python客户端库，用于与Appium服务器通信。
- pytest：Python的测试框架，用于编写和运行测试用例。
- allure-pytest：用于生成美观的测试报告。

## 2. 安装Python依赖

在命令行中运行以下命令，安装必要的Python库：

```sh
pip install pytest
pip3 install allure-pytest
pip install Appium-Python-Client
pip3 install PyYAML
```

## 3. 测试工程目录结构

创建一个合理的目录结构，方便管理和维护测试用例。例如：

```sh
pytest_project/
├── app/
│   └── your_app.apk  # 被测试的APP
├── common/
│   ├── base_page.py    # 封装通用操作
│   └── utils.py        # 通用工具函数
├── config/
│   └── config.yml      # 配置文件
├── conftest.py         # pytest 全局夹子
├── pytest.ini          # pytest配置文件
├── requirements.txt    # 依赖文件
├── run.py              # 运行测试用例的入口
└── testcase/
    ├── test_suites1.py   # 测试套件1
    └── test_suites2.py    # 测试套件2
```

## 4.运行测试用例

在run.py中编写运行测试用例的入口并运行run.py

## 5.生成测试报告

安装allure，解压cli并配置环境变量https://github.com/allure-framework/allure2/releases

生成静态报告并查看

```sh
allure generate ./report/allure -o ./report/html --clean
allure open ./report/html
```

运行测试用例后，使用Allure生成测试报告：

```sh
allure serve report/allure
```

每次运行测试用例生成allure结果都清除之前的结果

```sh
pytest --alluredir=./report/allure --clean-alluredir
allure generate ./report/allure -o ./report/html --clean
```

测试运行完后生成测试报告并且保留历史数据的脚本

```sh
#!/bin/bash
# 清理旧的历史数据，保留最新的20份
cd allure-results/history
ls -t | tail -n +21 | xargs rm -rf
cd -

# 复制历史数据到新的结果目录
cp -r allure-report/history allure-results/history

# 运行测试并生成结果
pytest --alluredir=./allure-results

# 生成新的报告
allure generate ./allure-results -o ./allure-report --clean
```