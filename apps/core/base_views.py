from django_tables2 import SingleTableView
from . import forms
from django.views import generic
from django.forms import modelform_factory


class BaseListView(SingleTableView):
    template_name = "includes/list.html"
    segment = None
    filter_class = None
    create_url = None
    show_only_filtered = False

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.filter = None

    def get_queryset(self):
        if self.filter_class:
            self.filter = self.filter_class(self.request.GET, queryset=super().get_queryset())
            if self.show_only_filtered and not self.request.GET:
                return self.model.objects.none()
            return self.filter.qs
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.filter_class:
            form = forms.FilterForm(self.filter.form)
            context.update({
                'filter': self.filter,
                'helper': form.helper,
                'create_url': self.create_url
            })
        else:
            context.update({
                'create_url': self.create_url
            })
        context.update({
            'segment': self.segment
        })
        return context


class FormViewMixin(generic.FormView):
    widgets = {}
    exclude = None

    def get_form(self, form_class=None):
        if self.form_class is None:
            form_class = modelform_factory(self.model, fields=self.fields, exclude=self.exclude, widgets=self.widgets)
        form = super().get_form(form_class=form_class)
        form.helper = forms.FormHelper()
        form.helper.form_tag = False
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'segment': self.segment
        })
        return context
