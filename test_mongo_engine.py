#!/usr/bin/env python
# coding=utf-8
# Created by zhezhiyong@163.com on 2016/12/6.

from mongoengine import *

connect('test_blog')


class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)


if __name__ == "__main__":
    # for i in xrange(100):
    #     ross = User(email='ross@example.com'+str(i), first_name='Ross'+str(i), last_name='Lawley'+str(i)).save()

    for u in User.objects:
        print u.email
    pass
