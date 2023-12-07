from django.shortcuts import render, redirect
from .models import Students
from django.contrib import messages

# Create your views here.

def home(request):

    if request.method == "GET":
        return render(request, 'home.html')
    else:
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['number']
        password = request.POST['password']

        setData = Students(name = name, email = email, mobile = mobile, password = password)
        setData.save()

        messages.success(request, f"'{name}' Account is Created successfuly !")

        return render(request, 'home.html')

def student(request):

    students = Students.objects.all()

    return render(request, 'students.html', {'students' : students})

def update(request, id):
    
    stud = Students.objects.get(id = id)

    if request.method == "POST":

        data = request.POST

        name = data.get('name')
        email = data.get('email')
        mobile = data.get('number')
        password = data.get('password')

        stud.name = name
        stud.email = email
        stud.mobile = mobile
        stud.password = password
        stud.save()

        messages.info(request, f"'{name}' Account is Updated Successfuly !")

    context = { 'student': stud }
    return render(request, "update.html", context)

def delete(request, id):

    stud = Students.objects.get(id=id)
    messages.info(request, f"'{stud.name}' Account is Deleted Successfuly !")
    stud.delete()
    return redirect("/students/")


