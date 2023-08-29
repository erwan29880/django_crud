from django.contrib import admin
from django.urls import path
from app1 import views as v1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gens/', v1.gens, name="gens-liste"),
    path('gens/<int:id>/', v1.gens_detail, name="gens-detail"),
    path('gens/add/', v1.gens_create, name='gens-create'),
    path('gens/change/<int:id>/', v1.gens_change, name='gens-change'),
    path('gens/delete/<int:id>/', v1.gens_delete, name='gens-delete'),
]
