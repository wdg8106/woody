#coding: utf-8
from django.shortcuts import render,redirect,render_to_response,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from models import *
from forms import ChangepwdForm
from django.core.paginator import Paginator,InvalidPage,EmptyPage


# return HttpResponse("0")

# ======================================
#   功能：管理员登录界面
#   人员：黄晓佳
#   日期：2014.10.10
# --------------------------------------
def login(request):
	return render(request, "login.html")

# ======================================
#   功能：登录表单提交验证
#   人员：黄晓佳
#   日期：2014.10.11
# --------------------------------------
@csrf_exempt
def login_handle(request):
	# 登录错误用户提示
	login_error = False

	# 请求方法判断
	if request.method != 'POST':
		login_error = u'请求方法不合法，请重试'
		return render_to_response("login.html", {'login_error':login_error})

	# 验证账号
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username = username, password = password)
	print password

	# 如果验证失败
	if user is None:
		login_error = u'账号或密码错误，请重试'
		return render(request, "login.html", {'login_error':login_error})

	# 验证成功
	auth_login(request, user)
	return HttpResponseRedirect("/backend/sendList/")

# ======================================
#   功能：修改密码表单提交验证
#   人员：黄晓佳
#   日期：2014.10.11
#   修改：woody
#   日期：2014.10。17
# --------------------------------------
def changePwd_handle(request):
	if request.method=="GET":
		form = ChangepwdForm()
		return render_to_response('changepwd.html',{'form':form,})
	else:
		form = ChangepwdForm(request.POST)
		if form.is_valid():
			username = request.user.username
			print username
			oldpassword = request.POST['oldpasswnd']
			print oldpassword
			user = authenticate(username = username, password = oldpassword)
			print user
			if user is not None :
				print "right"
				newpassword = request.POST.get('newpassword1','')
				user.set_password(newpassword)
				user.save()
				return HttpResponseRedirect("/backend/sendList")
			else:
				print "wrong"
				return render_to_response('changepwd.html',{'form':form,'oldpassword_is_wrong':True})
		else:
			return render_to_response('changepwd.html',{'form':form,})
	# return HttpResponse("0")

# ======================================
#   功能：退出登录
#   人员：黄晓佳
#   日期：2014.10.11
# --------------------------------------
def logout(request):
	auth_logout(request)
	return HttpResponseRedirect("/backend/login/")

# ======================================
#   功能：寄件列表页面
#   人员：黄晓佳
#   日期：2014.10.11
# --------------------------------------
def sendList(request):
	# 若没登录
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/backend/login/")
	sendlist = Send_user.objects.all()
	after_range_num = 5
	befor_range_num = 4
	try:
		page = int(request.GET.get("page",1))
		if page < 1:
			page =1
	except ValueError:
		page = 1
	paginator = Paginator(sendlist,10)
	try:
		res_list = paginator.page(page)
	except(EmptyPage,InvalidPage):
		res_list = paginator.page(paginator.num_pages)
	if page >= after_range_num:
		page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
	else:
		page_range = paginator.page_range[0:int(page)+befor_range_num]
	return render_to_response("index.html", {'title': "寄件",'namelist':res_list,'page_range':page_range})

# ======================================
#   功能：收件列表页面
#   人员：黄晓佳
#   日期：2014.10.11
# --------------------------------------
def receiveList(request):
	# 若没登录
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/backend/login/")
	receivelist = Receive_user.objects.all() 
	after_range_num = 5
	befor_range_num = 4
	try:
		page = int(request.GET.get("page",1))
		if page < 1:
			page = 1
	except ValueError:
		page = 1;
	paginator = Paginator(receivelist,10)
	try:
		res_list = paginator.page(page)
	except(EmptyPage,InvalidPage):
		res_list = paginator.page(paginator.num_pages)
	if page >= after_range_num:
		page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
	else:
		page_range = paginator.page_range[0:int(page)+befor_range_num]
	return render_to_response("indexReceive.html", {'title': "收件",'namelist':res_list,'page_range':page_range})

#===========================================
#    功能：显示把用户反馈
#    人员：woody
#    日期：2014.10.22
#===========================================
def FeedbackList(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/backend/login/")
	feedbacklist = Feedback.objects.all()
	return render_to_response('feedbacklist.html',{'namelist':feedbacklist,'title':"反馈"})

# def reply(request,id):
# 	if not request.user.is_authenticated():
# 		return HttpResponseRedirect("/backend/login/")
# 	res = get_object_or_404(Feedback,pk=int(id))
# 	res.content





#============================
#  功能：删除发件人
#  人员：woody
#  日期：2014.10.13
#-----------------------------
def deleteSender(request,id):
	res = get_object_or_404(Send_user,pk=int(id))
	res.delete()
	print "hehe"
	return HttpResponseRedirect("/backend/sendList")

#============================
#   功能：删除收件人
#   人员：woody
#   日期：2014.10.13
def deleteReceiver(request,id):
	res = get_object_or_404(Receive_user,pk=int(id))
	res.delete()
	return HttpResponseRedirect("/backend/receiveList")

#============================
#   功能:显示发件详情
#   人员：woody
#   日期：2014.10.13

def showSender(request,id):
	info = get_object_or_404(Send_user,pk=int(id))
	print "haha"
	return render_to_response('showSender.html',{'title': "寄件",'info':info,})

#=============================
#   功能：显示收件详情
#   人员：woody
#   日期：2014.10.13
#------------------------------

def showReceiver(request,id):
	info = get_object_or_404(Receive_user,pk=int(id))
	return render_to_response('showReceiver.html',{'title': "收件",'info':info,})

#=============================
#   功能：修改send状态
#   人员：woody
#   日期：2014.14
#-----------------------------
def modifySend(request,id):
	send = get_object_or_404(Send_user,pk=int(id))
	print "send"
	send.end_flag = True
	send.save()
	return HttpResponseRedirect("/backend/sendList")

#==============================
#   功能：需改receive状态
#   人员：woody
#   日期：2014.10.14
#------------------------------
def modifyReceive(request,id):
	receive = get_object_or_404(Receive_user,pk=int(id))
	print "receive"
	receive.end_flag = True
	receive.save()
	return HttpResponseRedirect("/backend/receiveList")

def count(request):
	receive_count = Receive_user.objects.all().count()
	print receive_count
	send_count = Send_user.objects.all().count()
	print send_count
	count = send_count + receive_count
	if count > 500:
		print "超过了"
	else:
		pass
	return HttpResponseRedirect("/backend/receiveList")





