#!/usr/bin/env python
# coding=utf-8
# Created by zhezhiyong@163.com on 2016/12/6.
from datetime import datetime

from flask import render_template, redirect, request, flash, url_for

from . import admin
from ..models import Post


@admin.route('/', methods=['GET', 'POST'])
@admin.route('/<int:page>', methods=['GET', 'POST'])
def index(page=None):
    if page is None:
        page = 1
    paginate = Post.objects.paginate(page=page, per_page=10)
    posts = paginate.items
    return render_template('admin.html', posts=posts, paginate=paginate)


@admin.route('/edit', methods=['GET', 'POST'])
def edit_new():
    return render_template('editor_new.html')


@admin.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    post = Post.objects.get_or_404(id=id)
    return render_template('editor_update.html', post=post)


@admin.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    Post.objects(id=id).delete()
    flash('a blog was successfully deleted')
    return redirect(url_for('.index'))


@admin.route('/update', methods=['GET', 'POST'])
def update_new():
    if request.form['type'] == 'new':
        if 'navigation' in request.form:
            if request.form['navigation'] == "yes":
                Post(title=request.form['title'], content=request.form['content'], navigation=1).save()
        else:
            Post(title=request.form['title'], content=request.form['content'], navigation=0).save()
    elif request.form['type'] == 'update':
        if 'navigation' in request.form:
            if request.form['navigation'] == "yes":
                Post.objects(id=request.form['id']).update(title=request.form['title'], content=request.form['content'],
                                                           navigation=1, modify_time=datetime.now)
        else:
            Post.objects(id=request.form['id']).update(title=request.form['title'], content=request.form['content'],
                                                       navigation=0, modify_time=datetime.now)
    flash('New blog was successfully updated')
    return redirect(url_for('.index'))
