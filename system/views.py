from django.shortcuts import render
from django.forms import ModelForm
from django.template import RequestContext
from .models import Student, Staff, Gallery, School, Structure_Inventory, Ground_Inventory, Profile
from .filters import StudentFilter, StaffFilter, StructureFilter, GroundFilter

# Create your views here.
class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['adm_no', 'adm_date','class_on_adm_day', 'dob', 'gender', 'full_name', 'guardian_name', 'home_address,', 'last_school','excempted_from_religious_instr', 'leaving_date', 'leaving_cert_no', 'remarks' ] 
def student(request):
    students  = Student.objects.all()
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'students':students,
        'form':form,
        'filter' : StudentFilter(request.GET, queryset = lads)
        }
     
    return render(request, 'student.html', context)


class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = ['full_name', 'tsc_no','dob', 'designation', 'job_group', 'dofa', 'id_no', 'kra_pin,', 'gender','contact', 'email'] 
def staff(request):
    staff  = Staff.objects.all()
    form = StaffForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'staff':staff,
        'form':form,
        'filter' : StaffFilter(request.GET, queryset = lads)
        }
     
    return render(request, 'staff.html', context)

def gallery(request):
    context = {
        'images': Gallery.objects.all()
    }
    return render(request, 'gallery.html', context)

def school(request):
    context = {
        'schools': School.objects.all()
    }
    return render(request, 'school.html', context)

def profile(request):
    pass

class StructureForm(ModelForm):
    class Meta:
        model = Structure_Inventory
        fields = ['struct_type', 'description','total_quantity', 'quantity_to_repair', 'quantity_to_replace', 'unused_quantity', 'total_surface_area', 'remarks'] 
def structures(request):
    structures  = Structure_Inventory.objects.all()
    form = StructureForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'structures':structures,
        'form':form,
        'filter' : StructureFilter(request.GET, queryset = lads)
        }
     
    return render(request, 'structure.html', context)

class GroundForm(ModelForm):
    class Meta:
        model = Ground_Inventory
        fields = ['ground_type', 'description','total_area', 'area_to_repair', 'unused_area', 'total_surface_area', 'remarks'] 
def staff(request):
    grounds  = Ground_Inventory.objects.all()
    form = GroundForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'grounds':grounds,
        'form':form,
        'filter' : GroundFilter(request.GET, queryset = lads)
        }
     
    return render(request, 'ground.html', context)






