# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import random
from django.views import View

# Create your views here.
def home(request):
    num = random.randint(0, 1000000)
    some_list = [num, random.randint(0, 1000000), random.randint(0, 1000000)]
    context = {
        "html_var": "Some Data",
        "num": num,
        "some_list": some_list

    }
    return render(request, "home.html", context)

def about(request):
    return render(request, "about.html", {})


def contact(request):
    return render(request, "contact.html", {})


class ContactView(View):

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "contact.html", context)
