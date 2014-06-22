from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=300, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    mylikes = models.IntegerField(default=0)    

    def __unicode__(self):
        return self.title

class Fantasy(models.Model):
    page = models.ForeignKey(Category)
    entry = models.CharField(max_length=500)
    # url = models.URLField()
    # views = models.IntegerField(default=0)
    # mylikes = models.IntegerField(default=0)    

    def __unicode__(self):
        return self.title        

class UserProfile(models.Model):
    # A required line - links a UserProfile to User.
    user = models.OneToOneField(User, primary_key=True)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username      