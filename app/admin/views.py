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


@admin.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        post = Post(title='', content='', navigation=0)
        return render_template('edit.html', post=post)
    if request.method == 'POST':
        nav = 1 if 'navigation' in request.form and request.form['navigation'] == 'yes' else 0
        Post(title=request.form['title'], content=request.form['content'], navigation=nav).save()
        flash('New blog was successfully added')
        print url_for('.index')
        return redirect(url_for('.index'))


@admin.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'GET':
        post = Post.objects.get_or_404(id=id)
        return render_template('edit.html', post=post)
    if request.method == 'POST':
        nav = 1 if 'navigation' in request.form and request.form['navigation'] == 'yes'else 0
        Post.objects(id=request.form['id']).update(title=request.form['title'], content=request.form['content'],
                                                   navigation=nav, modify_time=datetime.now)
    flash('New blog was successfully updated')
    return redirect(url_for('.index'))


@admin.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    Post.objects(id=id).delete()
    flash('a blog was successfully deleted')
    return redirect(url_for('.index'))
