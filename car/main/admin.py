from django.contrib import admin
from .models import Marka, Model, Category, Car, Comment


admin.site.register(Marka)
admin.site.register(Model)
if not admin.site.is_registered(Category):
    admin.site.register(Category)
admin.site.register(Car)
admin.site.register(Comment)
