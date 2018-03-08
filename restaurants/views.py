# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.db.models import Q
import random
from django.views import View
from django.views.generic import ListView, TemplateView
from .models import RestaurantLocation


class RestuarantListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset
