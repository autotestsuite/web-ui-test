# web ui test

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Run](#run)
- [Report](#report)
- [Details](#details)
- [More Examples](#more-examples)
- [Requirements](#requirements)
- [TODO](#todo)

## Overview

web ui 自动化测试项目，使用 selene + pytest + allure

**注：selene 是一个基于 selenium 二次封装的开源库*

pyproject.toml 文件中包含该项目的基本信息：
```toml
[tool.poetry]
name = "web-ui-test"
version = "0.1.0"
description = "python + pytest + selene + allure web tests project"
authors = ["g_xin <g_xin@outlook.com>"]
readme = "README.md"
packages = [{include = "web-ui-test"}]
```

## Installation

Given installed
- python = "~3.10"
- allure

使用 git clone 此项目
```shell
git clone https://github.com/autotestsuite/web-ui-test.git
```
or
```shell
git clone git@github.com:autotestsuite/web-ui-test.git
```

确保 pip 已是最新版本
```shell
python -m pip install --upgrade pip
```

安装项目所需的依赖包
```shell
pip install -r requirements.txt
```

## Usage

Quick Start

```python
from selene import browser, by, be, have

browser.open('https://google.com/ncr')
browser.element(by.name('q')).should(be.blank).type('selenium').press_enter()
```

or

```python
from selene import browser, by, be, have
from selene.support.shared import config
from selene.support.shared.jquery_style import s, ss


config.browser_name = 'firefox'
config.base_url = 'https://google.com'
config.timeout = 2
# config.* = ...

browser.open('/ncr')
s(by.name('q')).should(be.blank).type('selenium').press_enter()
ss('#rso>div').should(have.size_greater_than(5)).first.should(have.text('Selenium automates browsers'))
```

## Run

使用 pytest 提供的方式执行单条用例，支持使用命令行模式执行和 main.py 文件执行

pytest.ini 文件中可配置 pytest 配置项：
```ini
[pytest]
addopts = -vsq -p no:warnings
markers =
    release: suite of release tests
    smoke: suite of smoke tests
    in_progress: indicate that test implementation is not finished yet
```

## Report

使用 allure 报告进行结果展示，可在 ./reports 中进行查看

TBD

## Details

在 ./config.local.env 或者 ./config.prod.env 中进行运行环境的配置
```ini
;浏览器名称
browser_name=chrome

;浏览器版本号
browser_version=85.0

;基础url
base_url=https://www.google.com

;全局超时时间
timeout=5.0

;浏览器尺寸
maximize_window=False
window_width=1920
window_height=1080

;无头浏览器/无痕浏览器设置
headless=False
incognito=True

;远程Driver配置
remote_url=http://127.0.0.1:4444/wd/hub
remote_enableVNC=True
remote_enableVideo=False
remote_enableLog=False

;失败用例截图
save_page_source_on_failure=False
```

**注：config.local.env 建议设为本地的运行环境，config.prod.env 设为 release 运行环境*

## More Examples

TBD

## Requirements

项目依赖的三方库及版本信息：

pypi style:
```ini
allure-pytest==2.13.1
pytest==7.2.2
pytest-html==3.2.0
pytest-rerunfailures==11.1.2
pytest-ordering==0.6
pytest-xdist==3.2.1
selene==2.0.0b17
pydantic==1.10.7
requests==2.28.2
loguru==0.6.0
ddddocr==1.4.7
sphinx==6.1.3
sphinx-rtd-theme==1.2.0
```
poetry style:
```toml
[tool.poetry.dependencies]
python = "~3.10"
requests = "^2.28.2"
selene = {version = "^2.0.0b17", allow-prereleases = true}
allure-pytest = "^2.13.1"
ddddocr = "^1.4.7"
loguru = "^0.6.0"
pytest = "^7.2.2"
pytest-html = "^3.2.0"
pytest-rerunfailures = "^11.1.2"
pytest-ordering = "^0.6"
pytest-xdist = "^3.2.1"
pydantic = "^1.10.6"
sphinx = "^6.1.3"
sphinx-rtd-theme = "^1.2.0"
```

## TODO

- 编写通用 Assert 类，抛出TimeoutException异常
- 增加 docs 目录，增加 pages 说明文档
- 增加 @given / @when / @then 用例注解
- web ui 框架增加接口测试部分的功能