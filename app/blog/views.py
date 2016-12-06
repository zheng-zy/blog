#!/usr/bin/env python
# coding=utf-8
# Created by zhezhiyong@163.com on 2016/11/29.
from flask import render_template

from . import blog
from ..models import Post


@blog.route('/', methods=['GET', 'POST'])
@blog.route('/<int:page>', methods=['GET', 'POST'])
def index(page=None):
    if page is None:
        page = 1
    # post = Post(title="test", content="你好", navigation=1).save()
    for p in Post.objects:
        print p.title
    paginate = Post.objects.paginate(page=page, per_page=10)
    posts = paginate.items
    return render_template('index.html', posts=posts, paginate=paginate)


@blog.route('/blog/<id>', methods=['GET', 'POST'])
def post(id):
    post = Post.objects.get_or_404(id=id)
    posts = [post]
    return render_template('blog.html', posts=posts, )
