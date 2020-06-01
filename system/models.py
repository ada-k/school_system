from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from partial_date import PartialDateField

class School(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100, null=True)
    location = models.CharField(max_length = 50, null=True)
    image = models.ImageField(null = True, blank = True)

class Gallery(models.Model):
    name = models.CharField(max_length = 15,blank = True, null=True)
    image = models.ImageField(blank = True, null=True)

class Student(models.Model):
    GENDER_CHOICES = [
        ('F', 'FEMALE'),
        ('M', 'MALE'),
        ('I', 'INTERSEX')
    ]
    BORDER_OR_DAY = [
        ('D', 'DAY'),
        ('B', 'BORDER')
    ]
    adm_no = models.IntegerField(blank = True, null=True)
    number = models.IntegerField(blank = True, null=True)
    adm_date = PartialDateField(blank = True, null=True)
    class_on_adm_day = models.IntegerField(null=True, blank = True)
    dob = PartialDateField(blank = True, null=True)
    gender = models.CharField(max_length = 3, choices = GENDER_CHOICES, blank = True, null=True)
    full_name = models.CharField(max_length = 40, blank = True, null=True)
    guardian_name = models.CharField(max_length = 40, blank = True, null=True)
    home_address = models.CharField(max_length = 20, blank = True, null=True)
    last_school = models.CharField(max_length = 50, blank = True, null=True)
    border_or_day = models.CharField(blank = True, max_length = 10, choices = BORDER_OR_DAY, null=True)
    excempted_from_religious_instr = models.CharField(max_length  = 10, blank = True, null=True)
    leaving_date = PartialDateField(blank = True, null=True)
    leaving_cert_no = models.CharField(max_length = 15, blank = True, null=True)
    remarks = models.CharField(max_length = 40, blank = True, null=True)


class Staff(models.Model):
    GENDER_CHOICES = [
        ('F', 'FEMALE'),
        ('M', 'MALE'),
        ('I', 'INTERSEX')
    ]
    full_name = models.CharField(max_length = 30, blank = True, null=True)
    number = models.IntegerField(blank = True, null=True)
    tsc_no = models.CharField(max_length = 10, blank = True, null=True, unique = True)
    dob = PartialDateField(blank = True, null=True)
    designation = models.CharField(max_length = 20, blank = True, null=True)
    job_group = models.CharField(max_length = 30, blank = True, null=True)
    dofa = PartialDateField(blank = True, null=True)
    id_no = models.IntegerField(blank = True, null=True)
    kra_pin = models.CharField(max_length = 30, blank = True, null=True)
    gender = models.CharField(max_length = 3, choices = GENDER_CHOICES,null=True, blank = True)
    contact = models.IntegerField(blank = True, null=True)
    email = models.EmailField(max_length = 40, blank = True, null=True)

class Structure_Inventory(models.Model):
    struct_type = models.CharField(max_length = 15,blank = True, null=True)
    item_no = models.IntegerField(blank = True, null=True)
    description = models.CharField(max_length = 30, null=True)
    total_quantity = models.IntegerField(blank = True, null=True)
    quantity_to_repair = models.IntegerField(blank = True, null=True)
    quantity_to_replace = models.IntegerField(blank = True, null=True)
    unused_quantity = models.IntegerField(blank = True, null=True)
    total_surface_area = models.IntegerField(blank = True, null=True)
    remarks = models.CharField(max_length = 40, blank = True, null=True)


class Ground_Inventory(models.Model):
    ground_type = models.CharField(max_length = 15, blank = True, null=True)
    item_no = models.IntegerField(blank = True, null=True)
    description = models.CharField(max_length = 30, null=True)
    total_area = models.IntegerField(blank = True, null=True)
    area_to_repair = models.IntegerField(blank = True, null=True)
    unused_area = models.IntegerField(blank = True, null=True)
    total_surface_area = models.IntegerField(blank = True, null=True)
    remarks = models.CharField(max_length = 40, blank = True, null=True)


class Profile(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length = 20, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    dob = PartialDateField(null=True, blank=True)
    contact = models.CharField(max_length = 15, null=True)
    id_no = models.IntegerField(blank = True, null=True)
    image = models.ImageField(blank = True, null=True)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     try:
#         instance.profile.save()
#     except ObjectDoesNotExist:
#         Profile.objects.create(user=instance)
