#!/user/bin/env python3

'把web app需要的3个表用model表示出来'

import time, uuid


from orm import Model,StringField,BooleanField,FloatField,TextField

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)
# a =next_id()
# print(a)

class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)

class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image= StringField(ddl='varchar(50)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)

class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id,ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)

#在编写ORM时，给一个Field增加一个default参数可以让ORM自己填入缺省值，非常方便。并且，缺省值可以作为函数对象传入，在调用save()时自动计算。



import lxf,asyncio,sys
@asyncio.coroutine
def test():
    yield from lxf.create_pool(user='www-data',password='www-data',database='awesome', host="43.240.138.12")
    u = User(name='Test',email='test@example.com',passwd='1234567890',image='about:blank')
    # u = User()
    yield from u.save()

async def printa():
    vl = await test()
    for i in vl:
        print(i)
#
# if __name = '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.wait([test(loop)]))
#     loop.close()
#     if loop.close():
#         sys.exit(0)
loop = asyncio.get_event_loop()
loop.run_until_complete(printa())
loop.close()

# for x in test():
#     pass