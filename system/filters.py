import django_filters

from .models import Student, Staff, Gallery, School, Structure_Inventory, Ground_Inventory, Profile


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = {
            'full_name' : ['exact'],
            'adm_no': ['exact'],
            'gender': ['exact'],
            'guardian_name' : ['icontains'],
            # 'adm_date': ['year__lt', 'year__gt']
            'border_or_day': ['exact'],
            'home_address': ['icontains']
        }

class StaffFilter(django_filters.FilterSet):
    class Meta:
        model = Staff
        fields = {
            'full_name': ['exact'],
            'tsc_no': ['icontains'],
            'designation': ['icontains'],
            'job_group': ['icontains'],
            'gender': ['exact'],
        }

class StructureFilter(django_filters.FilterSet):
    class Meta:
        model = Structure_Inventory
        fields = {
            'description': ['icontains'],
            'struct_type': ['icontains'],
            'total_quantity': ['exact'],
            'remarks':['icontains']
        }

class GroundFilter(django_filters.FilterSet):
    class Meta:
        model = Ground_Inventory
        fields = {
            'description': ['icontains'],
            'ground_type': ['icontains'],
            'total_area': ['exact'],
            'remarks':['icontains']
        }

