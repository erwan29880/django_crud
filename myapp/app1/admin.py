from django.contrib import admin
from app1.models import Adresses, Genre


class AdressesAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'tel', 'genre')


admin.site.register(Adresses, AdressesAdmin)
admin.site.register(Genre)
