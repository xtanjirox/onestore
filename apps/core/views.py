from . import base_views as base
from . import models, tables
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


class ExampleListView(base.BaseListView):
    model = models.ExampleModel
    table_class = tables.ExampleTable
    table_pagination = False
    filter_class = None
    segment = 'example'
    create_url = reverse_lazy('size-create')


class ExampleCreateView(generic.CreateView, base.FormViewMixin):
    model = models.ExampleModel
    template_name = 'includes/create.html'
    fields = '__all__'
    segment = 'example'
