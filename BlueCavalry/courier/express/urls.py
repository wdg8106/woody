#coding: utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('express.views',
	url(r'^receive/$', 'receive', name='receive'),    # 我要收件
	url(r'^send/$', 'send', name='send'),    # 我要发件
	url(r'^weixinServer/','check_sign'),     #服务器的验证函数
	#url(r'^creatmenu/','creatmenu'),         #创建自定义菜单
)