![](https://github.com/serverlessplus/py/raw/master/serverless%2B.png)

# Serverless + Python

## 简介

`serverlessplus` 是一个简单易用的工具，它可以帮助你将现有的 `django` / `flask` 等框架构建的应用借助 [API 网关](https://cloud.tencent.com/product/apigateway) 迁移到 [腾讯云无服务云函数](https://cloud.tencent.com/product/scf)（Tencent Cloud Serverless Cloud Function）上。

## 开始使用

```shell
$ python3 -m pip install serverlessplus
```

假设有如下 `flask` 应用：
```python
# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello world'
```

添加 `index.py` 作为服务的入口文件, 内容如下：
```python
# encoding: utf8
from serverlessplus import create_environ, create_app, get_response, wrap_response

# specify entrypoint, `${file_name}:${callable_object}`
APP = 'app:app'
app = create_app(APP)

def main_handler(event, context):
    environ = create_environ(event, context)
    response = get_response(app, environ)
    return wrap_response(response, {'binary_mime_types': ['image/png']})
```

## 示例

- [flask 示例](https://github.com/serverlessplus/flask-example)
- [django 示例](https://github.com/serverlessplus/django-example)

## 支持的框架

`serverlessplus` 被设计为通过 `WSGI` 与框架进行交互. 理论上, 只要框架支持 `WSGI`, 就可以使用 `serverlessplus`

## 路线图

- 更多 Web 框架的支持与测试

`serverlessplus` 处于活跃开发中，`API` 可能在未来的版本中发生变更，我们十分欢迎来自社区的贡献，你可以通过 pull request 或者 issue 来参与。
