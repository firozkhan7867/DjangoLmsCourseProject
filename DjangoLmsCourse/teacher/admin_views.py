from django.shortcuts import render,redirect
from .models import Teacher
from django.shortcuts import get_object_or_404
from subjects.models import Course,Branch,Subject
from django.contrib import messages

# Create your views here.
def add_teacher(request):
    
    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        address = request.POST.get("address")
        exp = request.POST.get("exp")
        department = request.POST.get("department")
        course = request.POST.get("course")
        language = request.POST.get("language")
        pro_skills = request.POST.get("pro_skills")
        comm_skills = request.POST.get("comm_skills")
        teach_skills = request.POST.get("teach_skills")
        about = request.POST.get("about")
        qualifications = request.POST.get("qualifications")
        achievements = request.POST.get("achievements")
        photo = request.POST.get("photo")
        
        branch = Branch.objects.get(branch_id=department)
        
        if Teacher.objects.filter(email=email).exists():
            messages.error(request,'Email is already registered')
            return redirect('add-teacher')
        else:
            if Teacher.objects.filter(username=username).exists():
                messages.error(request,'Username is already registered')
                return redirect('add-teacher')
            else:
                teacher = Teacher(email=email,username=username,first_name=first_name,last_name=last_name,
                                address=address,experience=exp,department=branch,
                                languages=language,about=about,programming_skills=pro_skills,communication_skills=comm_skills,
                                teching_skills=teach_skills,achievements=achievements,qualification=qualifications
                                )
                teacher.course = course
                teacher.save()
                user = Teacher.objects.get(email=email)
                if 'photo' in request.FILES: 
                    photo = request.FILES['photo']
                    user.profile_photo =  photo #path_and_rename(username ,photo)
                user.save()
                messages.success(request,'SuccessFully Created the Teacher ')
                return redirect('add-teacher')
    
    
    branches = Branch.objects.all()
    courses = Subject.objects.all()
    context = {
        "branchs":branches,
        "courses":courses,
    }
    return render(request,'admin/user/add_teacher.htm',context)

def manage_teacher(request):
    teachers = Teacher.objects.all()
    context = {
        "teachers":teachers,
    }
    return render(request,'admin/user/manage_teacher.htm',context)


def edit_teacher(request,username):
    teacher = get_object_or_404(Teacher,username=username)
    branches = Branch.objects.all()
    courses = Subject.objects.all()
    context = {
        "branchs":branches,
        "courses":courses,
        "teacher":teacher,
    }
    return render(request,'admin/user/edit_teacher.htm',context)





