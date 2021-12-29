from django.contrib import admin

from .models import News


@admin.register(News)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ('subject',)
    list_display = ('date', 'subject',)
    list_filter = ('date',)
    #fields = ('date', 'subject', 'content',)
