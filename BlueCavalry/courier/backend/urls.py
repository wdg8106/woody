#coding: utf-8
from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('backend.views',
	url(r'^login/$', 'login'),                # 登录
	url(r'^logout/$', 'logout',name='logout'),              # 退出登录
	url(r'^changePwd_handle/$',changePwd_handle,name='changePwd_handle'),
	url(r'^sendList/$', 'sendList',name='sendlist'),          # 寄件列表页面
	url(r'^receiveList/$', 'receiveList',name='receivelist'),    # 收件列表页面
	url(r'^login_handle/$', 'login_handle'),  # 登录表单提交验证
	url(r'^deleteSender-(?P<id>\d+)/$',deleteSender,name='deleteSender'), #删除send
	url(r'^deleteReceiver-(?P<id>\d+)/$',deleteReceiver,name='deleteReceiver'), #删除receive
	url(r'^showSender-(?P<id>\d+)/$',showSender,name='showSender'),   #展示send详情
	url(r'^showReceiver-(?P<id>\d+)/$',showReceiver,name='showReceiver'), #展示receive详情
	url(r'^modifySend-(?P<id>\d+)/$',modifySend,name='modifySend'),    #修改send
	url(r'^modifyReceive-(?P<id>\d+)/$',modifyReceive,name='modifyReceive'), #修改receive
	url(r'^count/$',count,name='count'),
	url(r'^FeedbackList/$',FeedbackList,name='FeedbackList'),
)