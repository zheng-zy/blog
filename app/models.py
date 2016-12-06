#!/usr/bin/env python
# coding=utf-8
# Created by zhezhiyong@163.com on 2016/11/29.

from datetime import datetime

from . import db


class User(db.Document):
    name = db.StringField(required=True, max_length=64)
    password = db.StringField(max_length=256)
    email = db.StringField(max_length=64)
    description = db.StringField(max_length=1024)

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    # TypeError: ObjectId('552f41e56a85f00dd043406b') is not JSON serializable
    def get_id(self):
        return str(self.id)

    def __unicode__(self):
        return self.name


post_status = ((0, 'draft'), (1, 'published'))


class Post(db.Document):
    title = db.StringField(required=True, max_length=64)
    content = db.StringField(required=True)
    navigation = db.IntField(required=True, default=0)
    create_time = db.DateTimeField(default=datetime.now)
    modify_time = db.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return self.title

    meta = {
        'ordering': ['-create_time']
    }


if __name__ == "__main__":
    pass
