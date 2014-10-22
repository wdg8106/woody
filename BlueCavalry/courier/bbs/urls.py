#coding: utf-8
from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
	url(r'^feedback/$',feedback_show),
    url(r'^postshow/$',feedback_post_show),
    url(r"^postpost/$",feedback_post),
	)