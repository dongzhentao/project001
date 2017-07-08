from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'login/$', views.user_login),
    url(r'register/$', views.user_register),
    url(r'zhuce/$', views.zhuce),
    url(r'zhuce_yz/$', views.zhuce_yz),
    url(r'login_pwd_yz/$', views.login_pwd_yz),
    url(r'login_yz/$', views.login_yz),
    url(r'user_site/$', views.user_site),
    url(r'ushou_zhece/$', views.ushou_zhece),
    url(r'user_order/$', views.user_order),
    url(r'user_center/$', views.user_center),
    url(r'quit/$', views.quit)

]