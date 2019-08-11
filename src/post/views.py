from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Profile, Rating
from .serializers import UserListSerializer
from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User

from friendship.models import FriendshipRequest, Friend, Follow


# # Create your views here.
# class PostView(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def perform_create(self, serializer):
#         company = get_object_or_404(Company, id=self.request.data.get('company_id'))
#         return serializer.save(company=company)


# class SingleArticleView(RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class HelloWorldView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        return Response({'message': 'Hello World'})


class RateBloggerView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        value = request.data.get('value')

        other_user = get_object_or_404(User, id=self.request.data.get('user_id'))

        rating = Rating.objects.create(creator=self.request.user, value=value, following=other_user)
        
        return Response({'message': 'ok'})


class UserListAPIView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserListSerializer