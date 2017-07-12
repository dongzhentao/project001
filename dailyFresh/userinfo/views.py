# coding:utf-8
from django.shortcuts import render, redirect
from models import *
from hashlib import sha1
from django.http import JsonResponse, HttpResponse
from goods.models import GoodsInfo
from middleware import *


#  定义登录状态装饰器
def logined(func):
    def logining(request, *args, **kwargs):
        login_ed = request.session.get('login_ed')
        # print login_ed  测试用
        if login_ed:
            return func(request, *args, **kwargs)
        else:
            return redirect('/user/login/')

    return logining


# 登录页面
def user_login(request):
    return render(request, 'userinfo/login.html', {'title': '登录'})


# 注册页面
def user_register(request):
    return render(request, 'userinfo/register.html', {'title': '用户注册'})


# 注册
def zhuce(request):
    post = request.POST
    uname = post.get('uname')
    upwd = post.get('upwd')
    umail = post.get('umail')
    # 密码加密
    s1 = sha1()
    s1.update(upwd)
    upwd_sha1 = s1.hexdigest()

    # 创建模型类实例
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd_sha1
    user.umail = umail

    # save()必须用实例对象提交
    user.save()

    return redirect('/user/login/')


# 同名验证
def zhuce_yz(request):
    name = request.GET.get('name')
    count = UserInfo.objects.filter(uname=name).count()
    return JsonResponse({'count': count})


# 登录验证
def login_yz(request):
    name = request.GET.get('name')
    count = UserInfo.objects.filter(uname=name).count()
    return JsonResponse({'count': count})


def login_pwd_yz(request):
    name = request.POST.get('uname')
    pwd = request.POST.get('upwd')
    info = UserInfo.objects.filter(uname=name)
    # 将传过来的密码进行加密运算
    s1 = sha1()
    s1.update(pwd)
    pwd_sha1 = s1.hexdigest()
    # 加密后的密码进行比较
    if pwd_sha1 == info[0].upwd:
        request.session['login_ed'] = True
        request.session['name'] = name
        # 登录成功以后返回的页面,后期需要改
        url = request.session.get('url.path', '')
        # if url is not None:
        #     response = redirect(url)
        # else:
        response = redirect('user/user_center/')

        response.set_cookie('name', name)
        return response
    else:
        return render(request, 'userinfo/login.html', {'name': name, 'context': '0'})


# 个人中心之收货人管理
@logined
def user_site(request):
    name = request.COOKIES['name']
    user = UserInfo.objects.get(uname=name)
    shous = user.ushou_set.all().count()
    if shous == 0:
        context = None
    else:
        shous = user.ushou_set.all()
        context = shous

    return render(request, 'userinfo/user_center_site.html', {'context': context, 'name': name, 'title': '个人中心'})


# 全部订单
@logined
def user_order(request):
    name = request.session.get('name')
    return render(request,'userinfo/user_center_order.html',{'name': name, 'title': '个人中心'})


# 个人中心
@logined
def user_center(request):
    name = request.session.get('name')
    history = request.COOKIES['history'].split(',')
    goods = []
    for id in history:
        history_goods = GoodsInfo.objects.get(id=id)
        goods.append(history_goods)
    context = {'name': name, 'title': '个人中心','goods':goods}

    print history
    return render(request, 'userinfo/user_center_info.html',context)




def ushou_zhece(request):
    post = request.POST
    shouname = post.get('name')
    shouaddress = post.get('address')
    shoupost = post.get('youbian')
    shouphone = post.get('phone')
    name = request.COOKIES['name']
    user = UserInfo.objects.get(uname=name)
    shouer = Ushou()
    shouer.shouname = shouname
    shouer.shouaddress = shouaddress
    shouer.shoupost = shoupost
    shouer.shouphone = shouphone
    shouer.shouinfo = user
    shouer.save()
    return redirect('/user/user_site/')


# 退出设置

def quit(request):
    request.session.flush()
    return redirect('/user/login/')
