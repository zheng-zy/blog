#!/usr/bin/env python
# coding=utf-8
# Created by zhezhiyong@163.com on 2016/12/6.
from flask import Blueprint

admin = Blueprint('admin', __name__)

from . import views
