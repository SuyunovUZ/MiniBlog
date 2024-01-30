from django.contrib import admin
from .models import Author, Tag, About, Article, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    list_display_links = ('id', 'title', 'created_at')
    search_fields = ['title', 'author']
    filter_horizontal = ['tag']


admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(About)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
