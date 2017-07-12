from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^search/$', views.MySearchView.as_view()),
    url(r'^goodsinfo/(\d+)$', views.goodsinfo),
    url(r'^goodslist/(?P<id>\d+?)_(?P<pagenum>\d+)/$', views.goodslist),
    url(r'', views.index),

]