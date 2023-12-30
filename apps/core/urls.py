from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.home, name='home'),

    path('size/', views.ExampleListView.as_view(), name='example_view-list'),
    path('size/create/', views.ExampleCreateView.as_view(), name='example_view-create'),

]
