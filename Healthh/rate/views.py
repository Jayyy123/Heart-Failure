from django.shortcuts import redirect, render
from .models import Details, HeartFailure
from .forms import HeartForm
import numpy as np
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models.signals import pre_save,post_delete
from django.dispatch import receiver
from django.contrib import messages
from django.contrib.auth.models import User
import pickle




def home(request):
    return render(request, 'rate/home.html')

def predict(request):
    return render(request, 'rate/predict.html')
    
@login_required(redirect_field_name="loginpage")
def forms(request):
    a = HeartForm()
    with open('hrm', 'rb') as f:
        hr = pickle.load(f)
    if request.method == 'POST':
        a = HeartForm(request.POST, request.FILES)

        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        username = request.POST.get('nick_name')
        age = request.POST.get('age')
        anaemia = request.POST.get('anaemia')
        creatinine_phosphokinase = request.POST.get('creatinine_phosphokinase')
        diabetes = request.POST.get('diabetes')
        ejection_fraction = request.POST.get('ejection_fraction')
        high_blood_pressure = request.POST.get('high_blood_pressure')
        platelets = request.POST.get('platelets')
        serum_creatinine = request.POST.get('serum_creatinine')
        serum_sodium = request.POST.get('serum_sodium')
        sex = request.POST.get('sex')
        smoking = request.POST.get('smoking')
        time = request.POST.get('time')
        values = np.array([age, anaemia, creatinine_phosphokinase, diabetes,
           ejection_fraction, high_blood_pressure, platelets,
           serum_creatinine, serum_sodium, sex, smoking, time]).reshape(1,-1)

        c = hr.predict(values)
        i = c[0]
        HeartFailure.objects.create(first_name = firstname, last_name = lastname, username = username, result = i)
        if a.is_valid():
            a.save()
        return redirect('database')
    
        # return redirect('database')
        # print(request.POST)
        # model = pickle.load('pred.pickle')

    return render(request, 'rate/form.html', {'a':a})

@login_required( redirect_field_name= "loginpage")
def database(request):
    f = HeartFailure.objects.all()
    return render(request, 'rate/database.html', {'f':f})

def deletebase(request,pk):
    a = HeartFailure.objects.get(id = pk)
    a.delete()
    return redirect('database')


def loginuser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username = username)
        except:
            print(request, "username does not exist")
        
        user = authenticate(request, username =username, password = password)
        if user is not None:
            login(request, user)
            return redirect("forms")
    return render(request, "rate/loginpage.html")

def logoutuser(request):
    logout(request)
    return redirect("loginpage")


def result(request,pk):
    # a = Details.objects.get(id = pk)
    # c = HeartForm(instance = a)
    d = HeartFailure.objects.get(id=pk)
    # b = []
    # with open('hrm', 'rb') as f:
    #     hr = pickle.load(f)
        
    return render(request, 'rate/result.html', {'d':d})

def mode(request):
    return render(request, 'rate/mode.html')
def about(request):
    return render(request, 'rate/about.html')
def multi(request,pk):
    a = HeartFailure.objects.get(id = pk)
    return render(request, 'rate/multi.html', {'a': a})

        # b.append(Details.objects.all())

    # b.append(request.GET["age"])
    # b.append(request.GET['anaemia'])
    # b.append(request.GET['creatinine_phosphokinase'])
    # b.append(request.GET['diabetes'])
    # b.append(request.GET['ejection_fraction'])
    # b.append(request.GET['high_blood_pressure'])
    # b.append(request.GET['platelets'])
    # b.append(request.GET['serum_creatinine'])
    # b.append(request.GET['serum_sodium'])
    # b.append(request.GET['sex'])
    # b.append(request.GET['smoking'])
    # b.append(request.GET['time'])
    # if request.method == 'POST':
    #     c = HeartForm(request.POST,request.FILES, instance = a)
    #     if a.is_valid():
            # a.save()
    # b.append(request.GET["age"])
    # b.append(request.GET['anaemia'])
    # b.append(request.GET['creatinine_phosphokinase'])
    # b.append(request.GET['diabetes'])
    # b.append(request.GET['ejection_fraction'])
    # b.append(request.GET['high_blood_pressure'])
    # b.append(request.GET['platelets'])
    # b.append(request.GET['serum_creatinine'])
    # b.append(request.GET['serum_sodium'])
    # b.append(request.GET['sex'])
    # b.append(request.GET['smoking'])
    # b.append(request.GET['time'])
    # c = hr.predict([b])
