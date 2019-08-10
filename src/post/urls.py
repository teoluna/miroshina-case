from django.urls import path

from .views import PostView, SingleArticleView


app_name = "posts"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('posts/', PostView.as_view()),
    path('posts/<int:pk>', SingleArticleView.as_view())
]