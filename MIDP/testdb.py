# -*- coding: utf-8 -*-

from django.http import HttpResponse

from backend.models import *


# 数据库操作
def testdb(request):
    test = Student(id='1', name='test', password='123')
    test.save()
    return HttpResponse("<p>数据添加成功！</p>")