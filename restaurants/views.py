# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import random
from django.views import View
from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        print(context)

        num = random.randint(0, 1000000)
        some_list = [num, random.randint(0, 1000000), random.randint(0, 1000000)]
        context = {
         "html_var": "Some Data",
         "num": num,
         "some_list": some_list
        }
        return context
