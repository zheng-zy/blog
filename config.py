#!/usr/bin/env python
# coding=utf-8
# Created by zhezhiyong@163.com on 2016/11/29.

import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    BLOG_NAME = u"蓝色天空"
    MONGODB_SETTINGS = {'DB': 'db_blog'}

    def __init__(self):
        pass

    @staticmethod
    def init_app(app):
        pass


class TestConfig(Config):
    WTF_CSRF_ENABLED = False
    TEST = True


class DevConfig(Config):
    DEBUG = True


config = {
    'dev': DevConfig,
    'test': TestConfig,
    'default': DevConfig
}
