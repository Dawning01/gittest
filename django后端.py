django-admin startobjects mysite4
cd mysite4


 python3 manage.py startapp bookstore#---1



#另外一个   mysql -uroot -p123456
create database mysite4 default charset utf8#------2


# pycham setting 改 INSTALLED_APPS 注册app
# MIDDLEWARE  csrf 注释掉
# DATABASES 数据库
# default
# ENGINE
# NAME
# User
# PASSWORD
# HOST
# POET

# zh-Hans
# ASia/Shanghai

python3 manage.py  runserver#-------1


# pycham mysite4 models.py
#   创建class XX（models.Model)

# -------------3
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py shell
from bookstore.models import Book
# from 模块 import 类型
Book.objects.create( )


