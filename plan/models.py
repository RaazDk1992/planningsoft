from datetime import datetime
from operator import mod
from pdb import Restart
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

class MajorSector(models.Model):
    section = models.CharField(max_length=30)
    section_en = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.section

class ProjectType(models.Model):
    sector_ref = models.ForeignKey(MajorSector,on_delete=models.RESTRICT)
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
    def __str__(self):
        return self.group_type

class Woda(models.Model):
    woda = models.CharField(max_length=3)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.woda



class YojanaDetails(models.Model):
    prj_ref = models.CharField(max_length=40)
    prj_name = models.CharField(max_length=100)
    area_ref = models.ForeignKey(Woda,on_delete=models.RESTRICT)
    prj_tole = models.CharField(max_length=50)
    sector_ref = models.ForeignKey(MajorSector,on_delete=models.RESTRICT)
    prj_type = models.ForeignKey(ProjectType, on_delete=models.RESTRICT)
    type_prj_ref = models.ForeignKey(TypeOfProject, on_delete=models.RESTRICT)
    fy_ref = models.ForeignKey(FY,on_delete= models.RESTRICT)
    affected_people = models.IntegerField()
    prj_start_date = models.CharField(max_length=80)
    prj_start_date_en = models.DateField(default=timezone.now())
    prj_completion_date = models.CharField(max_length=80)
    prj_completion_date_en = models.DateField(default=timezone.now())
    is_multiyear = models.BooleanField(default=False)
    prj_estimate = models.FloatField()
    estimate_in_letters = models.CharField(max_length=100)
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

    project_ref = models.ForeignKey(YojanaDetails,on_delete=models.RESTRICT)
    comittee_name = models.CharField(max_length=200)
    comittee_name_en = models.CharField(max_length=200)
    comittee_address = models.CharField(max_length=100)
    black_listed = models.BooleanField(default=False)


class ComitteeMembers(models.Model):
    comittee_ref = models.ForeignKey(Comittee,on_delete=models.RESTRICT)
    project_ref = models.ForeignKey(YojanaDetails,on_delete=models.RESTRICT)
    member_name = models.CharField(max_length=50)
    member_designation = models.ForeignKey(Designation,on_delete=models.RESTRICT)
    member_citizen = models.CharField(max_length=50)
    member_citizen_img = models.ImageField(upload_to = 'path',default='default.jpg')
    member_image = models.ImageField(upload_to = 'path',default='default.jpg')
    member_phone = models.CharField(max_length=12)


class Tippani(models.Model):
    prj_ref = models.ForeignKey(YojanaDetails,on_delete=models.RESTRICT)
    title = models.CharField(max_length=100)
    file_path = models.FileField(upload_to='files')

class Karyadesh(models.Model):
    prj_ref = models.ForeignKey(YojanaDetails,on_delete=models.RESTRICT)
    title = models.CharField(max_length=100)
    file_path = models.FileField(upload_to='files')

class Samjhauta(models.Model):
    prj_ref = models.ForeignKey(YojanaDetails,on_delete=models.RESTRICT)
    title = models.CharField(max_length=100)
    file_path = models.FileField(upload_to='files')

class ProgressGeneral(models.Model):
    sector_ref = models.ForeignKey(MajorSector, on_delete=models.RESTRICT)
    title = models.CharField(max_length=100)
    population = models.IntegerField()
    amt = models.FloatField()
    remarks = models.TextField(max_length=200)

class Finalize(models.Model):
    prj_ref = models.ForeignKey(YojanaDetails,on_delete=models.RESTRICT)
    to_date = models.DateField(default=timezone.now())
  



