from django import forms
from . import models


class ExampleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['size'].widget.attrs['class'] = 'form-select multiple-remove choices__input'

    class Meta:
        model = models.ExampleModel
        fields = '__all__'
