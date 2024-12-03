from django.contrib import admin
from .models import User,Profile

# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]
admin.site.register(User, UserAdmin)