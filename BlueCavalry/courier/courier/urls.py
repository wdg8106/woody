# coding: utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^backend/', include('backend.urls')),        # 后台
    # url(r'^express/', include('express.urls')),        # 寄件与取件
    url(r'^express/',include('express.urls')),
    url(r'^bbs/',include('bbs.urls'))
)
