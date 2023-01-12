from django.urls import path
from . import views


urlpatterns = [
    path('', views.news_index, name = "news_home"),
    path('create', views.create, name = "news_create"),
    path('<int:pk>', views.NewsDetail.as_view(), name = "news_detail"),
]
