
### 安装依赖
sudo pip install django django-celery
sudo pip install "celery[redis]"
pip install -r requirements.txt


### 配置
./manage.py migrate
./manage.py createsuperuser


### 运行
./manage.py runserver 0.0.0.0:8000
./manage.py celery beat --loglevel=INFO    # 添加新任务后需重启beat
./manage.py celery worker --loglevel=INFO  


### 监控
pip install flower
celery flower --broker=redis://localhost:6379/0