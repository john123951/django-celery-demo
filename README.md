
### 安装依赖




### 配置
./manage.py migrate
./manage.py createsuperuser

### 运行
./manage.py runserver 0.0.0.0:8000
./manage.py celery beat --loglevel=INFO    # 添加新任务后需重启beat
./manage.py celery worker --loglevel=INFO  