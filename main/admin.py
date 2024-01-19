from django.contrib import admin
from .models import Home, Demand, Skills, Geography

@admin.register(Home)
class HomePage(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Demand)
class HomePage(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Geography)
class HomePage(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Skills)
class HomePage(admin.ModelAdmin):
    list_display = ('title',)
