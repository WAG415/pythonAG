#user/bin/env/python3
#-*- coding:utf-8 -*-

'ORM 测试'
#orm test



from lxf import Model,StringField,IntegerField

class User(Model):
    __table__ = 'users'
    id = IntegerField(primary_key=True)
    name = StringField()

#创建实例:
user = User(id=123, name='Michael')
#存入数据库:
print(user)
print(user.id)
print(user.name)
print(user)


