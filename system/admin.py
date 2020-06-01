from django.contrib import admin
from .models import Student, Staff, Gallery, School, Structure_Inventory, Ground_Inventory, Profile
# Register your models here.
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Gallery)
admin.site.register(School)
admin.site.register(Structure_Inventory)
admin.site.register(Ground_Inventory)
admin.site.register(Profile)
