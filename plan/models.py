from asyncio.windows_events import NULL
from email.policy import default
from operator import mod
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
def user_unicode_patch(self):
    return '%s %s' % (self.first_name, self.last_name)

class ProjectType(models.Model):
    type_ref = models.IntegerField()
    type = models.CharField(max_length=50)
class TypeOfProject(models.Model):
    project_type_ref = models.IntegerField()
    type_description = models.CharField(max_length=40)
class UnitOfWork(models.Model):
    unit_ref  = models.IntegerField()
    unit_name = models.CharField(max_length=20)
class YojanaDetails(models.Model):
    prj_ref = models.CharField(max_length=40)
    prj_name = models.CharField(max_length=100)
    prj_tole = models.CharField(max_length=50)
    prj_type = models.CharField(max_length=10)
    prj_duration = models.FloatField()
    prj_estimate = models.FloatField()
    is_active = models.BooleanField(default=True)
    is_complete = models.BooleanField(default=False)

class committee(models.Model):
    chairperson_name = models.CharField(max_length=50)
    chairperson_citizen = models.CharField(max_length=50)
    memberone_name = models.CharField(max_length=50)
    memberone_citizen = models.CharField(max_length=50)
    memberone_citizen_img = models.ImageField(upload_to = 'path',default='default.jpg')
    memberone_citizen_img = models.ImageField(upload_to = 'path',default='default.jpg')
    memberone_image = models.ImageField(upload_to = 'path',default='default.jpg')

    membertwo_name = models.CharField(max_length=50)
    membertwo_citizen = models.CharField(max_length=50)
    membertwo_citizen_img = models.ImageField(upload_to = 'path',default='default.jpg')
    membertwo_image = models.ImageField(upload_to = 'path',default='default.jpg')

    memberthree_name = models.CharField(max_length=50)
    memberthree_citizen = models.CharField(max_length=50)
    memberthree_citizen_img = models.ImageField(upload_to = 'path',default='default.jpg')
    memberthree_image = models.ImageField(upload_to = 'path',default='default.jpg')

