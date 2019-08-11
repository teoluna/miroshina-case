from rest_framework import serializers

from .models import Profile, Rating

# class PostSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Post
#         fields = ('id', 'title', 'slug', 'text', 'pub_date', 'company_id')


#     title = serializers.CharField(max_length=100)
#     slug = serializers.SlugField(max_length=50)
#     text = serializers.CharField()
#     pub_date = serializers.DateField()
#     company_id = serializers.IntegerField()

#     def create(self, validated_data):
#         return Post.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.text = validated_data.get('text', instance.text)
#         instance.slug = validated_data.get('slug', instance.slug)
#         instance.company_id = validated_data.get('company_id', instance.company_id)

#         instance.save()
#         return instance


class UserListSerializer(serializers.ModelSerializer):

    following = serializers.SerializerMethodField()
    follows_requesting_user = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            'user',
            'following',
            'follows_requesting_user',
            'follow_link',
        ]

    def get_following(self, obj):
        creator = self.context['request'].user
        following = obj.user
        connected = Rating.objects.filter(creator=creator, following=following)
        return len(connected)

    def get_follows_requesting_user(self, obj):
        creator = self.context['request'].user
        following = obj.user
        connected = Rating.objects.filter(creator=following, following=creator)
        return len(connected)