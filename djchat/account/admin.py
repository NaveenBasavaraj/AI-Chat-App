from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from server.models import Category, Server, Channel
from account.models import Account
# Register your models here.

admin.site.register(Category)
admin.site.register(Server)
admin.site.register(Channel)
admin.site.register(Account)
