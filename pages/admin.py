from django.contrib import admin

from pages.models import ScrollModel


@admin.register(ScrollModel)
class ScrollModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    search_fields = ('name',)
    list_filter = ('created_at',)
