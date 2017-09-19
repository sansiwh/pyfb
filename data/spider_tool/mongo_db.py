#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : mongo_db.py.py
# @Author: sansi
# Python版本：3.6.5 
# @Date  : 2017/9/19

import pymongo
import datetime

def get_mondb():
    # 建立连接
    client = pymongo.MongoClient(host="47.52.91.134", port=27017)
    db = client['fbdata']
    #或者 db = client.example
    return db

def get_db_op():
    posts = get_mondb().test
    return posts

if __name__ == '__main__':
    #post = {"author": "Mike","text": "My first blog post!","tags": ["mongodb", "python", "pymongo"],"date": datetime.datetime.utcnow()}
    #post = {"author": "Mike", "text111": "222", "tags": ["333", "444", "555"],"date": datetime.datetime.utcnow()}
    #posts.insert(post)
    #print(posts.find_one({"text111": "222"}))
    for i in get_db_op().find({"author": "Mike"}):
        print(i)