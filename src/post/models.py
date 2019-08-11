from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Rating(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    value = models.DecimalField(max_digits=7, decimal_places=2)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="friendship_creator_set")
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="friend_set")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)

    def get_connections(self):
        connections = Rating.objects.filter(creator=self.user)
        return connections
          
    def get_followers(self):
        followers = Rating.objects.filter(following=self.user)
        return followers

    def __str__(self):
        return "{} Profile".format(self.user.username)


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_profile, sender=User)
post_save.connect(save_profile, sender=User)


def create_rating(sender, instance, created, **kwargs):
    if created:
        target = instance.following
        followers = target.profile.get_followers() # ratings

        total = 0
        for rating in followers:
            total += rating.value

        avg = total / len(followers)

        target.profile.rating = avg

        target.profile.save()

post_save.connect(create_rating, sender=Rating)