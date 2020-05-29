from django.shortcuts import render
from django.forms import ModelForm
from django.template import RequestContext
from .models import Student, Staff, Gallery, School, Structure_Inventory, Ground_Inventory, Profile
from .filters import StudentFilter, StaffFilter, StructureFilter, GroundFilter

# Create your views here.
class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['adm_no', 'adm_date','class_on_adm_day', 'dob', 'gender', 'full_name', 'guardian_name', 'home_address', 'last_school','excempted_from_religious_instr', 'leaving_date', 'leaving_cert_no', 'remarks' ] 
def student(request):
    students  = Student.objects.all()
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'students':students,
        'form':form,
        }
     
    return render(request, 'student.html', context)

def student_query(request):
    students  = Student.objects.all()
    context = {
        'students':students,
        'filter' : StudentFilter(request.GET, queryset = students)
    }
    return render(request, 'student_query.html', context)


class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = ['full_name', 'tsc_no','dob', 'designation', 'job_group', 'dofa', 'id_no', 'kra_pin', 'gender','contact', 'email'] 
def staff(request):
    staff  = Staff.objects.all()
    form = StaffForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'staff':staff,
        'form':form,
        }
     
    return render(request, 'staff.html', context)

def staff_query(request):
    staff  = Staff.objects.all()
    context = {
        'staff':staff,
        'filter' : StaffFilter(request.GET, queryset = staff)
    }
    return render(request, 'staff_query.html', context)

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
        }
     
    return render(request, 'structure.html', context)

def structures_query(request):
    structures  = Structure_Inventory.objects.all()
    context = {
        'structures':structures,
        'filter' : StructureFilter(request.GET, queryset = structures)
    }
    return render(request, 'structure_query.html', context)

class GroundForm(ModelForm):
    class Meta:
        model = Ground_Inventory
        fields = ['ground_type', 'description','total_area', 'area_to_repair', 'unused_area', 'total_surface_area', 'remarks'] 
def ground(request):
    grounds  = Ground_Inventory.objects.all()
    form = GroundForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'grounds':grounds,
        'form':form,
        }
     
    return render(request, 'ground.html', context)
def ground_query(request):
    grounds  = Ground_Inventory.objects.all()
    context = {
        'grounds':grounds,
        'filter' : GroundFilter(request.GET, queryset = grounds)
    }
    return render(request, 'ground_query.html', context)







