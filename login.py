#!/usr/bin/python

import MySQLdb
def login(username , password):
    #return 1:success
    #return 0:failed
    db = MySQLdb.connect("localhost","root" , "1995" , "bling_blog")
    cursor = db.cursor()
    sql = "select username , password from username_passwords where username = '%s'and password = '%s'" % (username,password)
    try:
        if cursor.execute(sql) == 0:
            print"login failed\n"
            return 0;
    except:
        print"error"
    return 1;
    db.close()
        

