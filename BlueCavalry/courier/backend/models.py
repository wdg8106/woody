#coding: utf-8
from django.db import models
from django.forms import ModelForm,forms
from django import forms


addr_choices = (
    ('北京','北京'),
    ('上海','上海'),
    ('天津','天津'),
    ('重庆','重庆'),
    ('黑龙江','黑龙江'),
    ('吉林','吉林'),
    ('辽宁','辽宁'),
    ('河北','河北'),
    ('河南','河南'),
    ('山东','山东'),
    ('山西','山西'),
    ('安徽','安徽'),
    ('江西','江西'),
    ('江苏','江苏'),
    ('浙江','浙江'),
    ('福建','福建'),
    ('台湾','台湾'),
    ('广东','广东'),
    ('湖南','湖南'),
    ('湖北','湖北'),
    ('海南','海南'),
    ('云南','云南'),
    ('贵州','贵州'),
    ('四川','四川'),
    ('青海','青海'),
    ('甘肃','甘肃'),
    ('陕西','陕西'),
	)

company_choices =(
	('申通','申通'),
	('圆通','圆通'),
	('汇通','汇通'),
	('中通','中通'),
	('韵达','韵达'),
	('顺丰','顺丰'),
	)

time_choices=(
	('6:00~9:00','6:00~9:00'),
	('9:00~12:00','9:00~12:00'),
	('12:00~15:00','12:00~15:00'),
	('15:00~18:00','15:00~18:00'),
	('18:00~21:00','18:00~21:00'),
	)
weight_choices=(
	('1kg','1kg'),
	('2kg','2kg'),
	('3kg','3kg'),
	('4kg','4kg'),
	('5kg','5kg'),
	('10kg','10kg'),
	('>10kg','>10kg'),
	)

value_choices=(
	('10元','10元'),
	('20元','20元'),
	('30元','30元'),
	('40元','40元'),
	('50元','50元'),
	('>50元','>50元'),
	)
# ------------------------------
#  寄件人信息表 Send_user
#  name         : 寄件人姓名
#  phone        : 寄件人姓名
#  addr         : 取件地址
#  time         : 取件时间
#  send_addr    : 邮寄地址
#  description  : 备注
#  value_area   : 收件人地区
#  value_weight : 快件重量
#  value_price  : 价格预估
#  detatime     : 下单时间
#  end_flag     : 是否完结
#  company      :选择的快递公司
# ------------------------------
class Send_user(models.Model):
	name         = models.CharField(max_length=20)
	phone        = models.CharField(max_length=20)
	addr         = models.CharField(max_length=100)
	time         = models.CharField(max_length=20,choices =time_choices)
	send_addr    = models.CharField(max_length=100)
	description  = models.CharField(max_length=140)
	value_area   = models.CharField(max_length=100,choices =addr_choices )
	value_weight = models.CharField(max_length=20,choices=weight_choices)
	value_price  = models.CharField(max_length=20,choices=value_choices)
	datetime     = models.DateTimeField(auto_now_add=True)
	end_flag     = models.BooleanField(default = False)
	company      = models.CharField(max_length=30,choices=company_choices)

class sendForm(ModelForm):
	class Meta:
		model = Send_user

# ------------------------------
#  收件人信息表 Receive_user
#  name         : 收件人姓名
#  phone        : 收件人电话
#  fetch_addr   : 取件地址
#  send_addr    : 送件地址
#  send_time    : 送件时间
#  description  : 备注
#  detatime     : 下单时间
#  end_flag     : 是否完结
# ------------------------------
class Receive_user(models.Model):
	name        = models.CharField(max_length=20)
	phone       = models.CharField(max_length=20)
	fetch_addr  = models.CharField(max_length=100)
	send_addr   = models.CharField(max_length=100)
	send_time   = models.CharField(max_length=20,choices=time_choices)
	description = models.CharField(max_length=140)
	datetime    = models.DateTimeField(auto_now_add=True)
	end_flag    = models.BooleanField(default = False)

class receiveForm(ModelForm):
	class Meta:
		model = Receive_user

# Create your models here.
class FeedbackForm(forms.Form):
	subject = forms.CharField(max_length = 64)
	contents = forms.CharField(widget = forms.Textarea)

class Feedback(models.Model):
	subject    = models.CharField(max_length = 128)
	contents   = models.TextField()
	datetime   = models.DateTimeField(auto_now_add = True)
	is_public  = models.BooleanField(default = True)
	reply      = models.TextField(null=True,blank=True)
	reply_time = models.DateTimeField(null=True,blank=True)

