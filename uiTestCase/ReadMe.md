
- 框架组成：python + selenium + pytest + allure + yaml
- 设计模式：
  - 关键字驱动
  - pom: 页面对象模型
- 项目结构：
  - 工具层：base/
  - 页面层：page/
  - 用例层：test_cases/
  - 数据驱动：data_driver/
  - 数据层：data/
  - 根目录：
    - requirements.txt: 环境安装依赖
      - selenium: Web UI自动化测试库
      - pytest: Python第三方单元测试库
      - pytest-rerunfailures: Pytest扩展插件，实现测试用例失败重跑
      - allure-pytest: allure第三方测试库
      - pyyaml: 读写yaml文件的第三方库
      - openpyxl: 读写Excel文件的第三方库
      - 安装方式: pip install -r requirements.txt
    - conftest.py: 前置登录操作，每次执行一个py文件都会自动执行一次
    - run.py: 执行整个项目的入口
      

