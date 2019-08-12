from django.urls import path, include

from .views import HelloWorldView, RateBloggerView, UserListAPIView, RatingListAPIView, MaxValueAPIView
from .views import AuthWithoutPasswordAPIView, ProfileRatingAPIView
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here

app_name = "posts"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    # path('posts/', PostView.as_view()),
    # path('posts/<int:pk>', SingleArticleView.as_view()),
    path('hello/', HelloWorldView.as_view(), name='hello'),
    path('token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here
    path('accounts/', include('rest_registration.api.urls')),
    path('rate/', RateBloggerView.as_view()),
    path('list/', UserListAPIView.as_view()),
    path('ratings/', RatingListAPIView.as_view()),
    path('ratings/max/', MaxValueAPIView.as_view()),
    path('auth/', AuthWithoutPasswordAPIView.as_view()),
    path('profile/', ProfileRatingAPIView.as_view())
]