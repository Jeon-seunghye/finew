from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
admin.site.register(User, UserAdmin)
UserAdmin.fieldsets += (('Custom fields', {'fields': ('age', 'money', 'salary', 'financial_product')}),)
