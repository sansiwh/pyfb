#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : mongo_db.py.py
# @Author: sansi
# Python版本：3.6.5 
# @Date  : 2017/9/19

import pymongo
import datetime
from bson.objectid import ObjectId

def get_mondb():
    # 建立连接
    client = pymongo.MongoClient(host="47.52.91.134", port=27017)
    db = client['fbdata']
    #或者 db = client.example
    return db

if __name__ == '__main__':
    #单条
    #post = {"author": "Mike","text": "My first blog post!","tags": ["mongodb", "python", "pymongo"],"date": datetime.datetime.utcnow()}
    #post = {"author": "Mike", "text111": "222", "tags": ["333", "444", "555"],"date": datetime.datetime.utcnow()}
    #posts.insert(post)
    #print(posts.find_one({"text111": "222"}))

    #多条
    # post = [{"author": "chen", "text": "1", "tags": ["mongodb", "python", "pymongo"],
    #         "date": datetime.datetime.utcnow()},{"author": "chen", "text": "2", "tags": ["mongodb", "python", "pymongo"],
    #         "date": datetime.datetime.utcnow()},{"author": "chen", "text": "2", "tags": ["mongodb", "python", "pymongo"],
    #         "date": datetime.datetime.utcnow()}]
    # get_mondb().match_result.insert_many(post)

    #修改
    #get_mondb().match_result.update({"_id": ObjectId("59c0fc4a0f7a7529386b3bae")}, {"$set": {"text": "ccc"}})

    #删除
    #get_db_op().remove()
    #get_db_op().remove({"text": "ccc"})
    for i in get_mondb().match_result.find({"author": "chen"}):
        print(i)