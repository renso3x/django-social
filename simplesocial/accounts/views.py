# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import UserCreateForm

class Signup(CreateView):
	form_class = UserCreateForm
	success_url = reverse_lazy('login')
	template_name = 'accounts/signup.html'
