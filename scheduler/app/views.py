from django.shortcuts import render,redirect
from .task import test_func
from django.http import HttpResponse
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json
from .forms import IP as IPform
from .forms import UserRegistration as UserForm
import re, random, sys
from .models import IP as IPModel
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def test(request):
    test_func.delay()
    return HttpResponse("Done")


def registerView(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'register.html', {'form': form})
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})


def authlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        email = authenticate(request, email=email, password=password)
        if email is not None:
            login(request, email)
            if request.path != "/app/login":
               print('Login Successful')
            return redirect('/app/ping/')
        else:
            print('Please Enter Valid the Id and Password')
    context = {}
    return render(request, 'login.html', context)


@login_required(login_url='/app/login')
def scheduleTask(request):
    schedule, created = CrontabSchedule.objects.get_or_create(
        hour=5, minute=10)
    ip = "8.8.8.8"
    task = PeriodicTask.objects.create(
        crontab=schedule, name="schedule_task_"+"28", task="app.task.test_funct" , args=json.dumps([ip]))
    return HttpResponse("Done")


@login_required(login_url='/app/login')
def IP(request):
    if request.method == "POST":
        form = IPform(request.POST)
        if form.is_valid():
            ip = form.cleaned_data['ip']
            hourg = int(form.cleaned_data['hour'])
            minuteg = int(form.cleaned_data['minute'])
            secondg = int(form.cleaned_data['minute'])
            regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
            if hourg < 0 or hourg > 24:
                return HttpResponse("Inavlid Hour")
            if minuteg < 0 or minuteg > 60:
                return HttpResponse("Inavlid minute")
            if secondg < 0 or secondg > 60:
                return HttpResponse("Inavlid second")
            if re.search(regex, ip):
                print("Hree in view")
                schedule, created = CrontabSchedule.objects.get_or_create(
                    hour=hourg, minute=minuteg)
                total = str(PeriodicTask.objects.all().count()+1) + \
                    str(random.randint(0, sys.maxsize))
                print(total)
                task = PeriodicTask.objects.create(
                    crontab=schedule, name="schedule_task_"+total, task="app.task.test_func", args=json.dumps([ip,str(hourg),str(minuteg),str(secondg)]))
                return redirect('/app/status')
            else:
                return HttpResponse("Inavlid IP")
    form = IPform()
    return render(request, 'ping.html', {'form': form})


@login_required(login_url='/app/login')
def authlogout(request):
    logout(request)
    return redirect('/app/login')

@login_required(login_url='/app/login')
def viewStatus(request):
    alldata = IPModel.objects.all()
    ls = []
    for data in alldata:
        ls.append(data)
    return render(request, 'status.html', {'form': ls})