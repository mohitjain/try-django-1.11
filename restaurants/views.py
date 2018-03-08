# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
import random
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView
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

    def get_context_data(self, *args, **kwargs):
        print self.kwargs
        context = super(RestuarantListView, self).get_context_data(*args, **kwargs)
        print context
        return context

class RestuarantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()

    def get_context_data(self, *args, **kwargs):
        print self.kwargs
        context = super(RestuarantDetailView, self).get_context_data(*args, **kwargs)
        print context
        return context

    # def get_object(self, *args, **kwargs):
    #     rest_id =  self.kwargs.get('rest_id')
    #     obj = get_object_or_404(RestaurantLocation, id=rest_id)
    #     return obj
