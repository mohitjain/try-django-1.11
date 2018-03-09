# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
import random
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView
from .models import RestaurantLocation
from .forms import RestaurantCreateForm


def restaurant_createview(request):
    form = RestaurantCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        obj = RestaurantLocation.objects.create(
                name     = form.cleaned_data.get('name'),
                location = form.cleaned_data.get('location'),
                category = form.cleaned_data.get('category')

            )
        return HttpResponseRedirect("/restaurants/")
    if form.errors:
        errors = form.errors

    template_name = 'restaurants/form.html'
    context = {"form": form, "errors": errors}
    return render(request, template_name, context)

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
