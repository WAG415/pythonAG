#/user/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'aiguo Wang'

import asyncio, logging

import aiomysql

def log(sql,args=()):
    logging.info('SQL: %s' % sql)

'''创建连接池'''
#创建一个全局的连接池,每个http请求都可以从连接池中直接获取数据库连接.使用连接池的好处是不必频繁地打开和关闭数据库连接,而是能复用就尽量复用
@asyncio.coroutine
def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global  __pool
    __pool = yield from aiomysql.create_pool(
        host = kw.get('host','localhost'),
        port = kw.get('port',3306),
        user = kw['user'],
        passsword = kw['password'],
        db = kw.get('charset','utf8'),
        autocommit = kw.get('autocommit',True),
        maxsize = kw.get('maxsize',10),
        ninsize = kw.get('minsize',1),
        loop = loop
    )

'''select'''
@asyncio.coroutine
def select(sql, args, size=None):
    log(sql, args)
    global __pool
    with (yield from __pool) as conn:
        cur = yield from conn.cursor(aiomysql.DictCursor)
        yield from cur.execute(sql.replace('?', '%s'), args or ())
        if size:
            rs = yield from cur.fetchmany(size)
        else:
            rs = yield from cur.fetchall()
        yield from cur.close()
        logging.info('rows returned: %s' % len(rs))
        return rs

'''Insert,Update,Delete'''
@asyncio.coroutine
def execute(sql, args):
    log(sql)
    with (yield from __pool) as conn:
        try:
            cur = yield from conn.cursor()
            yield from cur.execute(sql.replace('?','%s'),args)
            affected = cur.rowcount
            yield from cur.close()
        except BaseException as e:
            raise
        return affected

'''ORM'''
#设计orm需要从上层调用者角度来设计
def creat_args_string(num):
    L = []
    for n in range(num):
        L.append('?')
    return ', '.join(L)
class Field(object):
    def __init__(self, name, column_type, primary_key, default):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default
    def __str__(self):
        return '<%s, %s:%s' % (self.__class__.__name__, self.column_type, self.name)

class ModelMetaclass(type):
    pass
'''定义model'''
#定义所有orm映射的基类model
class Model(dict, metaclass=ModelMetaclass):
    pass

f



