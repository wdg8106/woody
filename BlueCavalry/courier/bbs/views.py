#coding: utf8
# Create your views here.
from backend.models import FeedbackForm,Feedback
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from django.http import HttpResponse

def feedback_post(request):
	if request.method == "POST":
		form = FeedbackForm(request.POST, request.FILES)
		if form.is_valid():
			clean = form.cleaned_data
			title    = clean['subject']
			contents  = clean['contents']
			feedback = Feedback(subject = title,contents = contents)
		else:
			return HttpResponseRedirect("/bbs/feedback/")
		feedback.save()
		return HttpResponseRedirect("/bbs/feedback/")
	else:
		return HttpResponseRedirect("/bbs/feedback/")


# 显示反馈内容
def feedback_post_show(request):
	name ="feed_title"
	return render_to_response("feed_post.html", {"name":name,},context_instance=RequestContext(request))
	
def feedback_show(request):
	feedback = Feedback.objects.all()
	return render_to_response('feed_list_page.html',{'feedback':feedback,})
	