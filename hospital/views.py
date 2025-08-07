from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Doctor, Patient, Appointment

# Create your views here.
def About(request):
    return render(request, 'about.html')

def Home(request):
    return render(request, 'home.html')


def Contact(request):
    return render(request, 'contact.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request, 'index.html')

def Login(request):
    error = ""
    if request.method == 'POST':
        u= request.POST['uname']
        p= request.POST['pwd']
        user= authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
                
            else:
                error = "yes"
        except:
            error = "yes"
    d={'error': error}
    return render(request, 'login.html', d)


def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    
    logout(request)
    return redirect('admin_login')


def View_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc= Doctor.objects.all()
    d={'doc': doc}
    return render(request, 'view_doctor.html',d)


def Delete_doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')

def Add_doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n= request.POST['uname']
        m= request.POST['mobile']
        sp= request.POST['special']
        try:
            Doctor.objects.create(name=n, Mobile=m, special=sp)
            error = "no"

        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_doctor.html', d)


def View_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    doc= Patient.objects.all()
    d={'doc': doc}
    return render(request, 'view_patient.html',d)

def Delete_patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')

def Add_patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n= request.POST['uname']
        m= request.POST['mobile']
        g= request.POST['gender']
        a= request.POST['address']
        try:
           Patient.objects.create(name=n, mobile=m, gender=g, address=a)
           error = "no"

        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_patient.html', d)


def Add_appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    doctors = Doctor.objects.all()
    patients = Patient.objects.all()

    if request.method == 'POST':
        doctor_name = request.POST['doctor']
        patient_name = request.POST['patient']
        date = request.POST['date']
        time = request.POST['time']

        doctor = Doctor.objects.filter(name=doctor_name).first()
        patient = Patient.objects.filter(name=patient_name).first()

        try:
            Appointment.objects.create(
                doctor=doctor,
                patient=patient,
                date=date,
                time=time
            )
            error = "no"
        except:
            error = "yes"

    return render(request, 'add_appointment.html', {
        'doctors': doctors,
        'patients': patients,
        'error': error
    })



def View_appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    doc= Appointment.objects.all()
    d={'doc': doc}
    return render(request, 'view_appointment.html',d)

def Delete_appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    app = Appointment.objects.get(id=pid)
    app.delete()
    return redirect('view_appointment')