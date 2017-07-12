# coding:utf-8
from django.core.paginator import Paginator
from django.shortcuts import render
from models import *
from haystack.generic_views import SearchView


def index(request):
    # 查询商品种类
    t1 = TypeInfo.objects.all()
    # 设置容器,用来添加查询到的数据
    goodslist = []
    for t in t1:
        print(t.ttitle)
        # 查询最新的商品,取4个
        new_list = t.goodsinfo_set.order_by('-id')[0:4]
        # 查询最火的商品,取4个
        hot_list = t.goodsinfo_set.order_by('gclick')[0:3]
        goodslist.append({'type': t, 'new_list': new_list, 'hot_list': hot_list})

    context = {'title': '首页', 'goodslist': goodslist}
    return render(request, 'goods/index.html', context)


def goodslist(request, id, pagenum):
    goodstype = TypeInfo.objects.get(id=id)

    n = request.GET.get('a', '')
    if n == '':
        list = goodstype.goodsinfo_set.order_by('-id')
    elif n == '1':
        list = goodstype.goodsinfo_set.order_by("-gprice")
    elif n == '2':
        list = goodstype.goodsinfo_set.order_by("gprice")
    elif n == '3':
        list = goodstype.goodsinfo_set.order_by('-gclick')

    newgoods = list[0:2]
    page = Paginator(list, 15)
    pageinfo = page.page(pagenum)
    page_max = page.page_range

    pnum = pageinfo.number
    # 用来记录总页数
    l = len(page_max)
    # 判断页码与当前页码的关系
    if l <= 5:
        pagelist = page_max
    elif l - pnum < 5:
        pagelist = [l - 4, l - 3, l - 2, l - 1, l - 0]
    else:
        if pnum < 3:
            pagelist = [1, 2, 3, 4, 5]
        else:
            pagelist = [pnum - 2, pnum - 1, pnum, pnum + 1, pnum + 2]
            # print(pnum) 测试专用
            # print pagelist  测试专用
    context = {'title': '商品列表',
               'type': goodstype,
               'pageinfo': pageinfo,
               'pagelist': pagelist,
               'newgoods': newgoods,
               'pnum': pnum,
               'len': l,
               'a': n
               }
    return render(request, 'goods/list.html', context)


def goodsinfo(request, id):
    goods = GoodsInfo.objects.get(id=id)
    # 记录点击量
    goods.gclick += 1
    goods.save()

    goodstype = goods.gtype
    newgoods = goodstype.goodsinfo_set.order_by('-id')[0:2]
    context = {"title": '商品信息',
               'type': goodstype,
               'goods': goods,
               'newgoods': newgoods
               }
    respons = render(request, 'goods/detail.html', context)

    # 设置容器,存储最近浏览信息的id
    history = request.COOKIES.get("history", '').split(",")
    if len(history) >= 6:
        history.pop()
    else:
        if id not in history:
            history.insert(0, id)
        else:
            history.remove(id)
            history.insert(0, id)

    respons.set_cookie("history", ','.join(history), max_age=60 * 60 * 24 * 7)

    return respons


class MySearchView(SearchView):
    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        page = context.get('page_obj')
        l = page.paginator.num_pages
        pnum = page.number

        print(page)
        if l < 5:
            pagelist = page.paginator.page_range

        elif l - pnum < 5:
            pagelist = [l - 4, l - 3, l - 2, l - 1, l - 0]
        else:
            if pnum < 3:
                pagelist = [1, 2, 3, 4, 5]
            else:
                pagelist = [pnum - 2, pnum - 1, pnum, pnum + 1, pnum + 2]

        context["title"] = '查询信息'
        context["pagelist"] = pagelist
        context["pnum"] = pnum
        context["len"] = l
        context["page"] = page


        print context
        return context
