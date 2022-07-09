from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
def user_unicode_patch(self):
    return '%s %s' % (self.first_name, self.last_name)


class Office(models.Model):
    officeName = models.CharField(max_length = 200)
    officeAddress = models.CharField(max_length = 100)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.officeName
        
class Designation(models.Model):
    designation = models.CharField(max_length=100)
    designation_en = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.designation
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sanketNo = models.CharField(max_length=30, blank=True)
    contactNo = models.CharField(max_length=13, blank=True)
    is_active = models.BooleanField(default=False)

class relmap(models.Model):
    offRef = models.ForeignKey(Office, on_delete=models.RESTRICT)
    uRef = models.OneToOneField(User,on_delete=models.RESTRICT)

class FY(models.Model):
    fy = models.CharField(max_length=30)
    fy_np = models.CharField(max_length=30)
    isactive = models.BooleanField(default=True)
    def __str__(self):
        return self.fy_np
    class Meta:
        unique_together = ('fy', 'fy_np','isactive',)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Doc(models.Model):
    doc_ref = models.CharField(max_length=20)
    doc_name = models.CharField(max_length=100)
    doc_body = models.TextField(max_length=2000)
    is_active = models.BooleanField(default=True)
class ProjectType(models.Model):
    type = models.CharField(max_length=50)
    type_en = models.CharField(max_length=100)
    isActive = models.BooleanField(default=True)
    def __str__(self):
        return self.type
class TypeOfProject(models.Model):
    type_description = models.CharField(max_length=40)
    type_description_en = models.CharField(max_length=40)
    isActive = models.BooleanField(default=True)
    def __str__(self):
        return self.type_description
class UnitOfWork(models.Model):
   
    unit_name = models.CharField(max_length=20)
    unit_name_en = models.CharField(max_length=20)
    def __str__(self):
        return self.unit_name
class ResponsibleGroup(models.Model):
    group_type = models.CharField(max_length=100)
    group_type_en = models.CharField(max_length=100)


class YojanaDetails(models.Model):
    prj_ref = models.CharField(max_length=40)
    prj_name = models.CharField(max_length=100)
    prj_tole = models.CharField(max_length=50)
    prj_type = models.ForeignKey(ProjectType, on_delete=models.RESTRICT)
    type_prj_ref = models.ForeignKey(TypeOfProject, on_delete=models.RESTRICT)
    fy_ref = models.ForeignKey(FY,on_delete= models.RESTRICT)
    affected_people = models.IntegerField()
    prj_duration = models.FloatField()
    prj_estimate = models.FloatField()
    is_active = models.BooleanField(default=True)
    is_complete = models.BooleanField(default=False)
    time_stamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.prj_name
class count(models.Model):
    fy_ref = models.ForeignKey(FY,on_delete = models.RESTRICT)
    count = models.IntegerField()
    count_np = models.CharField(max_length=10)
    def __str__(self):
        return self.count
class Comittee(models.Model):
    comittee_name = models.CharField(max_length=200)
    comittee_name_en = models.CharField(max_length=200)
    comittee_address = models.CharField(max_length=100)
    black_listed = models.BooleanField(default=False)


class ComitteeMembers(models.Model):
    comittee_ref = models.ForeignKey(Comittee,on_delete=models.RESTRICT)
    project_ref = models.ForeignKey(YojanaDetails,on_delete=models.RESTRICT)
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

