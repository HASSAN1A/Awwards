from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
import datetime as dt
from django.db.models.signals import post_save
from django.dispatch import receiver
import statistics

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = ImageField(blank=True, manual_crop="")
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=60, blank=True)
    contact = models.CharField(max_length=60,blank=True)
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()



class Project(models.Model):
    """
    Project class to define project Objects
    """
    title = models.CharField(max_length=155)
    url = models.URLField(max_length=255)
    description = models.TextField(max_length=255)
    technologies = models.CharField(max_length=200, blank=True)
    cover_photo = ImageField(blank=True, manual_crop="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 


    class Meta:
        ordering = ['upload_date'] 

    def save_project(self):
      '''
      Saves project instance to db
      '''
      self.save()


    @classmethod
    def get_all_projects(cls):
      '''
      Returns all project objects from db
      '''
      projects=cls.objects.all()
      return projects 


    @classmethod
    def get_project_by_id(cls,id):
      '''
      Returns project based on its id
      '''
      project=cls.objects.get(id=id)
      return project



    @classmethod
    def delete_project(cls,id):
      '''
      Deletes project based on its id
      '''
      cls.objects.filter(id=id).delete()
      

    @classmethod
    def search_project(cls,prj_title):
      '''
      Allows us to search for a project using its title.
      '''
      projects=cls.objects.filter(title__icontains=prj_title)
      return projects



    @classmethod
    def filter_by_userid(cls,user_id):
      """
      Allows us to filter projects by the user posted.
      """
      projects=cls.objects.filter(user_id=user_id)
      return projects

  
class Rating(models.Model):
    rating = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )

    design = models.IntegerField(choices=rating,  blank=True)
    usability = models.IntegerField(choices=rating, blank=True)
    content = models.IntegerField(choices=rating, blank=True)
    score = models.FloatField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)


    def save_rating(self):
        self.save()


    @classmethod
    def get_project_ratings(cls, id):
        ratings = Rating.objects.filter(project_id=id).all()
        return ratings

    def __str__(self):
        return str(self.id)
