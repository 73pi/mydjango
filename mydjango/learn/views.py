# -*- coding: utf-8 -*-#

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse


# ^first/
def index(request):
    return HttpResponse(u"欢迎来到我的django学习  welcome my first response!")


# ^add/$
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))


# ^new_add/(\d+)/(\d+)/$
def add2(requset, a, b):
    c = int(a)+int(b)
    return HttpResponse(str(c))


# ^first_template/
def frist_template(requset):
    return render(requset, 'home.html')


# ^add/(\d+)/(\d+)/$
def old_too_new_url(request, a, b):
    # 实现templates中的home.html的<a>URL是旧的也可以跳转到对应name的url
    # reverse接收url中的name作为第一个参数，我们在代码中就可以通过reverse()来获取对应的网址
    # 只要对应的url的name不改，就不用改代码中的网址。
    return HttpResponseRedirect(reverse('add2', args=(a, b)))


# ^template_adv/
def template_adv(request):
    arg = {}
    arg['string'] = "这是字符串展示！"
    arg['List'] = ["列表展示1", "列表展示2", "列表展示3", "列表展示4"]
    arg['info_dict'] = {'site': 'django', 'content': '学习'}
    return render(request, 'template-adv.html', arg)

# 表单
# r'^form/'
def form(request):
    return render(request, 'form.html')
