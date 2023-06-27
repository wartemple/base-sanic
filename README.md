# 目录解释
| docker-compose.yml    docker-compose部署文件
| application           项目代码
    | core              逻辑代码目录（算法代码，逻辑代码写在这）
        | common        通用代码（常用工具包，日志控制器）
    | logs              日志目录
    | web               网络访问代码目录（接口定义、入参验证、出参拼接、监听器、中间件）
        | blueprints    蓝图目录（定义接口组织结构）
            | view.py   定义模块接口前缀，default: api/v1
            | example   样例接口目录===》 fork项目后，参照该样例进行编写接口，实现完自己的业务接口后，删除该目录
        | middleware    中间件目录，包含样例
        | listeners.py  监听器样例
        | server.py     服务启动入口文件，配置服务上下文，启动worker数，


# 服务初始化
## 第一步,初始化自身业务代码:
操作样例：编写一个ner识别接口

1. 复制example目录， 重命名为ner
2. 在主蓝图文件里，加上新增蓝图
进入/application/web/blueprints/view.py, 输入以下代码
```
from .ner.view import bp as ner_bp

bp = Blueprint.group(ner_bp, url_prefix='api/v1', name="ner")

```
3. 实现ner的接口
进入/application/web/blueprints/ner/view.py
将文件内容修改为
```
from sanic import Blueprint, json
from sanic.log import logger

bp = Blueprint("Ner", url_prefix="/ner")

@bp.post('/parse')
def parse_ner(request):
    # do something
    return json({"messages": "success"})
```
## 第二步，删除多余代码
删除/application/web/blueprints/example文件夹

## 第三步，启动服务
进入/application
启动 start.sh

## 第四步访问，自定义接口
http://localhost:7777/api/v1/ner/parse