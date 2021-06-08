from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("email",'full_name','is_admin','date_joined')
    list_filter = ('is_admin','is_active')
    search_fields = ("email",'full_name')