from django.db import models

# Create your models here.
class Article(models.Model):
    class Meta():
        db_table='Article'
    article_title=models.CharField(max_length=100)
    article_text=models.TextField()
    article_date=models.DateTimeField()
    article_likes=models.IntegerField(default=0)

class Comit(models.Model):
    class Meta():
        db_table='Comit'
    comit_text=models.TextField()
    comit_articl=models.ForeignKey(Article)
