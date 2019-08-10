from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin


from .models import Post, Company
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404

# Create your views here.
class PostView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        company = get_object_or_404(Company, id=self.request.data.get('company_id'))
        return serializer.save(company=company)


class SingleArticleView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer