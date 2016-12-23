#!/usr/bin/env python3

__author__ = 'Aiguo Wang'

'url handlers'

import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get,post

from models import User,Comment,Blog,next_id

#测试
# @get('/')
# async def index(request):
#     users = await User.findAll()
#     return {
#         '__template__':'test.html',
#         'users':users
#     }

#blogs
@get('/')
def index(request):
    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    blogs = [
        Blog(id='1', name='Test Blog', summary=summary,created_at=time.time()-120),
        Blog(id='2', name='Something New', summary=summary, created_at=time.time()-3600),
        Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time()-7200),
        Blog(id='4', name='Study Python', summary='python is the best oc in all the lanuage', created_at=10000)
    ]
    return {
        '__template__':'blogs.html',
        'blogs':blogs
    }

@get('/api/users')
@asyncio.coroutine
def api_get_users(*,page='1'):
    users = yield from User.findAll(orderBy='created_at desc')
    users = [
        User(id='1', admin='wang', name='aiguo'),
        User(id='2', admin='wang2', email='505263623@qq.com'),
        User(id='3', admin='wang3', creat_at=321456789)
    ]
    for u in  users:
        u.passwd = '******'
    return dict(users=users)

@get('/test')
def test():
    return {
        '__template__':'test.html'
    }
