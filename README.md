## 简介
任务调度，通过后台动态配置cron风格的执行任务。

### 项目依赖
- redis: key-value存储
- sqlite3: 本地数据存储
- celery: 分布式任务作业
  - celery[redis]: 使用redis作为broker
- django: Web Framework
  - django-celery: celery web管理
  - dj-static: 生产环境self静态文件

### 安装依赖
```shell
pip install -r requirements.txt
```

### 配置
```shell
./manage.py migrate          # 同步数据库
./manage.py createsuperuser  # 创建管理员
./manage.py collectstatic    # 收集静态文件
```

### 修改redis地址
修改./scheduler/settings.py文件中BROKER_URL、CELERY_RESULT_BACKEND选项

### 运行
```shell
./manage.py runserver 0.0.0.0:8000         # 管理后台
./manage.py celery beat --loglevel=INFO    # 触发作业
./manage.py celery worker --loglevel=INFO  # 执行作业（添加新代码时需重启）
```

### 监控 [Optional]
```shell
pip install flower
celery flower --address 0.0.0.0 --broker=redis://localhost:6379/0 --broker_api=redis://localhost:6379/0
```

### 其他
监听模块变化: worker 使用autoreload启动，自动加载新添加的代码（实验性功能）[官方文档](http://docs.celeryproject.org/en/3.1/userguide/workers.html#autoreloading)