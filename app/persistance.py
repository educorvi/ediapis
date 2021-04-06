import urllib.parse
from pymongo import MongoClient
from bson.objectid import ObjectId
from .private import MONGOUSR, MONGOPW

username = urllib.parse.quote_plus(MONGOUSR)
password = urllib.parse.quote_plus(MONGOPW)

mongoclient = MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password))

def writeDocToDatabase(formdata):
    db = mongoclient.five_rules
    posts = db.posts
    post_id = posts.insert_one(formdata).inserted_id
    retid = 'edi%s' % str(post_id)
    return retid

def readDocFromDatabase(dbid):
    objid = dbid.split('edi')
    if len(objid) == 2:
        get_id = ObjectId(objid[1])
    else:
        get_id = ObjectId(objid)
    db = mongoclient.five_rules
    posts = db.posts
    document = posts.find_one({'_id':get_id})
    return document
