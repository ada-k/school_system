from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class School(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 50)

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
    adm_no = models.CharField(max_length = 20, blank = True)
    adm_date = models.DateField(blank = True)
    class_on_adm_day = models.IntegerField()
    dob = models.DateField(blank = True)
    gender = models.CharField(max_length = 3, choices = GENDER_CHOICES, blank = True)
    full_name = models.CharField(max_length = 40, blank = True)
    guardian_name = models.CharField(max_length = 40, blank = True)
    home_address = models.CharField(max_length = 20, blank = True)
    last_school = models.CharField(max_length = 50, blank = True, choices = BORDER_OR_DAY)
    excempted_from_religious_instr = models.CharField(max_length  = 10, blank = True)
    leaving_date = models.DateField(blank = True)
    leaving_cert_no = models.CharField(max_length = 15, blank = True)
    remarks = models.TextField(max_length = 40, blank = True)


class Staff(models.Model):
    GENDER_CHOICES = [
        ('F', 'FEMALE'),
        ('M', 'MALE'),
        ('I', 'INTERSEX')
    ]
    full_name = models.CharField(max_length = 20, blank = True)
    tsc_no = models.CharField(max_length = 10, blank = True)
    dob = models.DateField(blank = True)
    designation = models.CharField(max_length = 10, blank = True)
    job_group = models.CharField(max_length = 10, blank = True)
    dofa = models.CharField(max_length = 10, blank = True)
    id_no = models.IntegerField(blank = True)
    kra_pin = models.IntegerField(blank = True)
    gender = models.CharField(max_length = 3, choices = GENDER_CHOICES, blank = True)
    contact = models.IntegerField(blank = True)
    email = models.EmailField(max_length = 40, blank = True)

class Structure_Inventory(models.Model):
    struct_type = models.CharField(max_length = 15,blank = True)
    description = models.CharField(max_length = 30)
    total_quantity = models.IntegerField(blank = True)
    quantity_to_repair = models.IntegerField(blank = True)
    quantity_to_replace = models.IntegerField(blank = True)
    unused_quantity = models.IntegerField(blank = True)
    total_surface_area = models.IntegerField(blank = True)
    remarks = models.TextField(max_length = 40, blank = True)

class Gallery(models.Model):
    name = models.CharField(max_length = 15,blank = True)
    image = models.ImageField(blank = True)

class Ground_Inventory(models.Model):
    ground_type = models.CharField(max_length = 15, blank = True)
    description = models.CharField(max_length = 30)
    total_area = models.IntegerField(blank = True)
    area_to_repair = models.IntegerField(blank = True)
    unused_area = models.IntegerField(blank = True)
    total_surface_area = models.IntegerField(blank = True)
    remarks = models.TextField(max_length = 40, blank = True)

class Profile(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length = 20)
    location = models.CharField(max_length=30, blank=True)
    dob = models.DateField(null=True, blank=True)
    contact = models.CharField(max_length = 15)
    id_no = models.IntegerField(blank = True)
    image = models.ImageField(blank = True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)
