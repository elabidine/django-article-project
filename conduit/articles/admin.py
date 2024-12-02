from django.contrib import admin
from .models import Article,Comment
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):               # new
    readonly_fields = ("uuid_field","slug")
admin.site.register(Article,ArticleAdmin)

admin.site.register(Comment)