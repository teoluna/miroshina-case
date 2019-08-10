from rest_framework import serializers

from .models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'text', 'pub_date', 'company_id')


    title = serializers.CharField(max_length=100)
    slug = serializers.SlugField(max_length=50)
    text = serializers.CharField()
    pub_date = serializers.DateField()
    company_id = serializers.IntegerField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.company_id = validated_data.get('company_id', instance.company_id)

        instance.save()
        return instance