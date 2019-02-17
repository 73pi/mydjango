# -*- coding: utf-8 -*-#

from django.db import models


# 数据库表的创建
# python manage.py makemigrations
# python manage.py migrate
# cli>>>from learn.models import People
# 写入数据：cli>>> People.objects.create(name="hahah", age=24)
class People(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    # cli>>> People.objects.get(name="hahah")
    def __unicode__(self):
        # python3: def __str__(self):
        return self.name


"""创建对象：
1.People.objects.create(name=name,age=age)
2.p = People（name="WZ", age=23)
  p.save()
3.p = People(name="TWZ")
  p.age = 23
  p.save()
4.People.objects.get_or_create(name="WZT", age=23)
"""
"""获取对象：
1.People.objects.all()
2.People.objects.all()[:10] 不支持负索引，切片可以节约内存
3.People.objects.get(name=name)
存在数据：People.objects.all().exists()
排序数据：People.objects.all().order_by('age') #-age为倒序
链式查询：People.objects.filter(name__contains="abc").exclude(age=23)
"""
"""删除对象
1.People.objects.filter(name__contains="abc").delete() 删除名称中包含 "abc"的人
2.People.objects.all().delete() # 删除所有People记录
"""
"""更新对象
1.People.objects.filter(name__contains="abc").update(name='xxx')
2.p = People.objects.get(name="hahah")
  p.name = 'bbbbbb'
  p.save()
"""