#coding: utf-8
from django import forms

class ChangepwdForm(forms.Form):
	oldpasswnd = forms.CharField(
		required = True,
		label = u"原始密码",
		error_messages = {'required':u'请输入原始密码'},
		widget = forms.PasswordInput(
			attrs={'placeholder':u'原密码',}))

	newpassword1 = forms.CharField(
		required = True,
		label = u'新的密码',
		error_messages={'required':u'请输入新密码'},
		widget = forms.PasswordInput(
			attrs={'placeholder':u'新密码',}),)

	newpassword2 = forms.CharField(
		required = True,
		label = u'确认密码',
		error_messages={'required':u'请再次输入密码'},
		widget = forms.PasswordInput(
			attrs={'placeholder':u'确认密码',}),)

	def clean(self):
		if not self.is_valid():
			raise forms.ValidationError(u'所有项都为必填项')
		elif self.cleaned_data['newpassword1']<>self.cleaned_data['newpassword2']:
			raise forms.ValidationError(u'两次输入不一样')
		else:
			cleaned_data = super(ChangepwdForm,self).clean()
			return cleaned_data

