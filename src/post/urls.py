from django.urls import path, include

from .views import PostView, SingleArticleView, HelloWorldView
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here

app_name = "posts"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('posts/', PostView.as_view()),
    path('posts/<int:pk>', SingleArticleView.as_view()),
    path('hello/', HelloWorldView.as_view(), name='hello'),
    path('token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here
    path('accounts/', include('rest_registration.api.urls')),
    path('friendship/', include('friendship.urls'))
]