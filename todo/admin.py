from django.contrib import admin
from .models import Todolist
# Register your models here.

@admin.register(Todolist)
class TodolistAdmin(admin.ModelAdmin):
   list_display = ('id','title','description','status')
   list_filter = ('status',)
   search_fields = ('title',)
   list_editable = ('status',)
   list_per_page = 5

# admin.site.register(Todolist, TodolistAdmin)