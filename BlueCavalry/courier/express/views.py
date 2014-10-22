#coding: utf-8
from django.shortcuts import render,redirect,render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context,Template,RequestContext
from django import forms
from backend.models import *
import hashlib
import sys
import string
import urllib2


# ======================================
# 	名字：前台手机界面以及相应的表单处理
#   功能：发件
#   人员：梁银乔
#   日期：2014.10.10
#   修改：woody
#   修改日期：2014.10.14
# --------------------------------------
def send(request):
	print "haha"
	if request.method=="POST":
		receive_count = Receive_user.objects.all().count()
		print receive_count
		send_count = Send_user.objects.all().count()
		print send_count
		count = send_count + receive_count
		if count > 500:
			print "超过了"
			return HttpResponse("今天订单已满！")
		else:
			form = sendForm(request.POST,request.FILES)
			if form.is_valid():
				res=form.save()
				print "hehe"
				return HttpResponseRedirect("/backend/sendList")
			else:
				return render_to_response('send.html',{'form':form,})
	else:
		
		return render_to_response('send.html',{'form':sendForm(),})
	
#====================================
#    功能：收件
#    人员：woody
#    日期：2014.10.14
#====================================
def receive(request):
	if request.method=="POST":
		receive_count = Receive_user.objects.all().count()
		print receive_count
		send_count = Send_user.objects.all().count()
		print send_count
		count = send_count + receive_count
		if count > 500:
			print "超过了"
			return HttpResponse("今天订单已满！")
		else:
			form = receiveForm(request.POST,request.FILES)
			if form.is_valid():
				res = form.save()
				return HttpResponseRedirect("/backend/receiveList")
			else:
				return render_to_response('receive.html',{'form':form})
	else:
		return render_to_response('receive.html',{'form':receiveForm(),})

#=========================================
#    功能：微信开发者url验证
#    人员：woody
#    日期:2014.8.21
#-----------------------------------------
def check_sign(request):
	TOKEN = u"qingqibing"
	signature  = request.GET.get('signature',"")
	timestamp = request.GET.get('timestamp',"")
	nonce = request.GET.get('nonce',"")
	echostr = request.GET.get('echostr')
	# token = request.GET.get('TOKEN',"")
	token = TOKEN
	source = ''.join(sorted([timestamp,nonce,token]))
	sign = hashlib.sha1(source).hexdigest()
	status = False
	result = ''
	if sign == signature:
		status = True
		result = echostr
	return HttpResponse(echostr)

#============================================
#    功能：自定义按钮界面接口
#    人员：woody
#    日期：2014.10.21
#---------------------------------------------
def creat_menu(request):
	accesstoken = u"XOwGv9r0jQI6OpwHDWWuGi7U4PxoPHsXDDIDETVL8ZwFN7OrQ7_HCi0jhw2bNCRSCxE9VB4wT6S56VrbyfJnCw"
	body = {"button":[
			{
			"type":"view",
			"name":"青骑上阵",
			"url":"http://pkusz.szzbmy.com/wei_site/"
			},			

			{
			"name":"取件寄件",
			"sub_button":
			[
			{	
			    "type":"view",
			    "name":"生活指南",
			    "url":"http://pkusz.szzbmy.com/life/index/"
			},
			{
			    "type":"click",
			    "name":"点击有惊喜",
			    "key":"GET_COUPON"
			}
			]
			},			

			{
			"name":"骑兵卫民",
			"sub_button":
			[
			{ 
			    "type":"view",
			    "name":"投诉建议",
			    "url":"http://pkusz.szzbmy.com/feedback/"
			}
			]			

			}
			]}
	url = u"https://api.weixin.qq.com/cgi-bin/menu/create?access_token="+accesstoken
	print url
	# urlData = urllib2.urlencode(body)
	urlData = body
	print urlData
	req = urllib2.Request(url = url, data = urlData)
	if req == "":
		print fail

	# print req
	return HttpResponse(req)