# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import friend_request, friend_bond

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

@login_required
def reqst(request):
	try:
		to = int(request.POST["to"])
	except :
		return HttpResponse("invalid input")
	new,created =friend_request.objects.get_or_create(sender_id=request.user.id,receiver_id=to)
	if created :
		new.save()
	else:
		new.delete()
	return HttpResponse("done")

@login_required
def respond(request):
	try:
		_from = int(request.POST["from"])
		_res  = request.POST["response"]
	except :
		return HttpResponse("invalid input")
	try:
		req = friend_request.objects.get(sender_id=_from,receiver_id=request.user.id)
	except :
		return HttpResponse("fail")

	if _res == "accept":
		req._accept()
	else:
		req._reject()
	return HttpResponse("finish")


@login_required
def update(request):
	try:
		_from = int(request.POST["from"])
	except Exception as e:
		return HttpResponse("invalid input")
	result , d =r_friends(request.user.id,_from)
	if not result:
		return HttpResponse("fail")

	d.delete()

	return HttpResponse("finish")

def r_friends(frome,to):
	try:
		a= friend_bond.objects.get(sender_id=frome,receiver_id=to)
		return [True,a]
	except :
		try:
			a= friend_bond.objects.get(sender_id=to,receiver_id=frome)
			return [True,a]
		except:
			return [False,None]




