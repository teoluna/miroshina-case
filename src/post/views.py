from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Profile, Rating
from .serializers import UserListSerializer, RatingListSerializer
from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User

from friendship.models import FriendshipRequest, Friend, Follow

from rest_framework import filters

from django.db.models import Max

from rest_framework.authtoken.models import Token

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

        other_user = get_object_or_404(User, username=self.request.data.get('user_id'))

        rating = Rating.objects.create(creator=self.request.user, value=value, following=other_user)
        
        return Response({'message': 'ok'})


class UserListAPIView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserListSerializer

class RatingListAPIView(ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingListSerializer
    filter_backends = (filters.OrderingFilter,)
    search_fields = ['value']
    ordering_fields = ['value', 'created']

    def get_queryset(self):
        queryset = Rating.objects.all()
        value_max = self.request.query_params.get('value_max', None)
        value_min = self.request.query_params.get('value_min', None)

        search = self.request.query_params.get('search', None)
        
        if value_max is not None:
            queryset = queryset.filter(value__lte=value_max)
        
        if value_min is not None:
            queryset = queryset.filter(value__gte=value_min)

        if search is not None:
            queryset = queryset.filter(creator__username__contains=search) | queryset.filter(following__username__contains=search)

        return queryset

class MaxValueAPIView(APIView):
    def get(self, request):
        return Response(Rating.objects.aggregate(Max('value')))

class AuthWithoutPasswordAPIView(APIView):
    def post(self, request):
        login = self.request.data.get('login');
        user = User.objects.filter(username=login).first()
        
        if user is None:
            user = User.objects.create(username=login, password=login)

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key
        })

class ProfileRatingAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        
        profile = Profile.objects.filter(user=self.request.user).first()

        if profile is None:
            profile = Profile.objects.create(user=self.request.user)

        return Response({
            'username': self.request.user.username,
            'rating': profile.rating
        })
        