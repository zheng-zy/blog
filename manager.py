#!/usr/bin/env python
# coding=utf-8
# Created by zhezhiyong@163.com on 2016/11/29.

import os

from flask_script import Manager, Server

from app import create_app
from app.models import Post

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.context_processor
def inject_nav():
    posts = Post.objects(navigation=1)
    result = []
    for row in posts:
        result.append([row.id, row.title])
    return {'navs': result, 'blogname': app.config['BLOG_NAME']}


manager = Manager(app)
manager.add_command('runserver', Server(host='127.0.0.1', port=6666, use_debugger=True, use_reloader=True))

if __name__ == "__main__":
    app.run()
