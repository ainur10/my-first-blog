from django.contrib import admin
from  article.models import Article,Comit

# Register your models here.
class CommentArticle(admin.StackedInline):
    model = Comit
    extra = 1

class ArticleSettings(admin.ModelAdmin):
    fields = ['article_title','article_text','article_date']
    inlines = [CommentArticle]
    list_filter = ['article_date']

admin.site.register(Article,ArticleSettings)