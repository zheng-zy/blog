#!/usr/bin/env python
# coding=utf-8
# Created by zhezhiyong@163.com on 2016/11/29.
from flask import Blueprint

blog = Blueprint('blog', __name__)

from . import views
