#!/usr/bin/env python
# coding=utf-8
# Created by zhezhiyong@163.com on 2016/12/6.
from flask import render_template, request

from . import admin
from ..models import Post


@admin.route('/', methods=['GET', 'POST'])
@admin.route('/<int:page>', methods=['GET', 'POST'])
def index(page=None):
    if page is None:
        page = 1
    for p in Post.objects:
        print p.title
    paginate = Post.objects.paginate(page=page, per_page=10)
    posts = paginate.items
    return render_template('admin.html', posts=posts, paginate=paginate)


@admin.route('/edit', methods=['GET', 'POST'])
def edit_new():
    return render_template('editor_new.html')


@admin.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    if id:
        return id
    return render_template('editor_new.html')


@admin.route('/delete', methods=['GET', 'POST'])
@admin.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    return id


@admin.route('/update', methods=['GET', 'POST'])
def update_new():
    form = request.form
    print request.form
    return 'hhh'


@admin.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    return id
