from datetime import datetime
from pickle import TRUE
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import FileExtensionValidator



# Create your models here.

class Post(models.Model): 
    body=models.TextField()
    created_on=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)





class Comment(models.Model):
    post=models.ForeignKey('Post',related_name='comments',on_delete=models.CASCADE)
    author=models.ForeignKey(User,related_name='author',on_delete=models.DO_NOTHING)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("post_list", kwargs={"pk": self.pk})
 
    def __str__(self):
        return self.author



class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user',
                                related_name='profile', on_delete=models.CASCADE, db_constraint=False)
    name = models.CharField(max_length=30, blank=True, null=True)
    proffession = models.TextField(max_length=500, blank=True, null=True)
    birth_date=models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    picture = models.ImageField(upload_to='uploads/profile_pictures', default='uploads/profile_pictures/default.png', blank=True)
    followers = models.ManyToManyField(User, blank=True, related_name='followers')
    resume = models.FileField(upload_to='documents/',
                              default='documents/yk_sugi_resume_new.docx', blank=True, null=True, validators=[FileExtensionValidator(['pdf'])])
    video_resume = models.FileField(upload_to='documents/',
                              default='documents/video_file.mp4', blank=True, null=True, validators=[FileExtensionValidator(['mp4'])])

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()




class Jobs(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,default=1)
    company_name = models.CharField(max_length=150, default=1)
    salary=models.IntegerField(default=100000)
    location=models.TextField(default=1)
    job_title=models.CharField(max_length=150)
    created_on=models.DateField(default=timezone.now)
    description=models.TextField()
    is_active=models.BooleanField(null=True,blank=True)



class JobRequest(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    job=models.ForeignKey(Jobs,on_delete=models.CASCADE)
    request=models.TextField(default="No requests")
