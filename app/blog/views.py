#!/usr/bin/env python
# coding=utf-8
# Created by zhezhiyong@163.com on 2016/11/29.
import markdown2
from flask import render_template

from . import blog
from ..models import Post


@blog.route('/', methods=['GET', 'POST'])
@blog.route('/<int:page>', methods=['GET', 'POST'])
def index(page=None):
    if page is None:
        page = 1
    paginate = Post.objects(navigation=0).paginate(page=page, per_page=10)
    posts = paginate.items
    for post in posts:
        post.content = markdown2.markdown(post.content,
                                          extras=["code-friendly", "code-color", "cuddled-lists", "tables", "footnotes",
                                                  "pyshell", "toc"])
    return render_template('index.html', posts=posts, paginate=paginate)


@blog.route('/blog/<id>', methods=['GET', 'POST'])
def post(id):
    post = Post.objects.get_or_404(id=id)
    post.content = markdown2.markdown(post.content,
                                      extras=["code-friendly", "code-color", "cuddled-lists", "tables", "footnotes",
                                              "pyshell", "toc"])
    posts = [post]
    return render_template('blog.html', posts=posts, )
