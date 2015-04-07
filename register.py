#!/usr/bin/python

import MySQLdb

def register(username , password):
    db = MySQLdb.connect("localhost" , "root" , "1995" , "bling_blog")
    cursor = db.cursor()
    try:
        cursor.execute("insert into username_passwords values('%s','%s')"%(username , password))
        db.commit()
    except:
        db.rollback()
    return
