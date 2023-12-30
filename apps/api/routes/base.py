from django.contrib import admin
from django.urls import path
from ninja_extra import NinjaExtraAPI
from apps.api.routes import example_routes

api = NinjaExtraAPI()

api.add_router("/", example_routes.router)

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/", api.urls),
]
