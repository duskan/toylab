from django.contrib import admin

from blog.models import Post


# Register your models here.
@admin.register(Post)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'subtitle', 'user', 'ctime']
    list_display_links = ['id', 'title']
    list_per_page = 10
    search_fields = ['id', 'title', 'subtitle', 'user', 'ctime']
