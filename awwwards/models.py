from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class Projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=30)
    image = models.ImageField()
    description = models.TextField()
    location = models.CharField(max_length=30, null=True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title

    @classmethod
    def search_by_title(cls,search_term):
        awwwards = cls.objects.filter(title__icontains=search_term)
        return awwwards
    
    def save_project(self):
        self.save()  

    def delete_project(self):
        self.delete()

    def update_project(self):
        self.save()
    

class Profile(models.Model):
    profile_pic = models.ImageField()
    bio = models.TextField()
    contact = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.profile_pic
    
    def save_profile(self):
        self.save()  

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.save()

class Review (models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),  
    )
    project = models.ForeignKey(Projects,null=True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)
    user_name = models.CharField(max_length = 100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return self.user_name

    def save_review(self):
        self.save()  

    def delete_review(self):
        self.delete()

    def update_review(self):
        self.save()
