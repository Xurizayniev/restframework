from django.contrib import admin
from .models import TodoModel

@admin.register(TodoModel)
class TodoModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'id']
    list_display_links = ['title']