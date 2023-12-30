import django_tables2 as tables
from . import models

DETAIL_BUTTON_TEMPLATE = """
        <a href="{{record.get_absolute_url}}" class="btn btn-outline-primary"><i class='fas fa-pencil-alt'></i></a>
"""


class ExampleTable(tables.Table):
    detail = tables.TemplateColumn(DETAIL_BUTTON_TEMPLATE)

    class Meta:
        orderable = False
        model = models.ExampleModel
        fields = ('id', 'detail')
        attrs = {"class": "table", "id": "table2"}
