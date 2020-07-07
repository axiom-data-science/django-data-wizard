from django.contrib import admin

from data_wizard.admin import ImportActionModelAdmin
from .models import FileSource, URLSource


@admin.register(FileSource)
class FileSourceAdmin(ImportActionModelAdmin):
    list_display = [
        'name', 'file', 'date'
    ]
    list_filter = ['date']


@admin.register(URLSource)
class URLSourceAdmin(ImportActionModelAdmin):
    list_display = [
        'name', 'url', 'date'
    ]
    list_filter = ['date']
