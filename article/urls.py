from django.conf.urls import url,include
from article import views
urlpatterns = [
    #url(r'^articles/all/', views.articles),
    url(r'^articles/get/(?P<article_id>[0-9]+)/$', views.article),
    url(r'^', views.articles),

]