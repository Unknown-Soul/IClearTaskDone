from celery import shared_task
from os import system
from django.http import HttpResponse
from .models import IP

@shared_task(bind=True)
def test_func(self, ip, hour, minute, second):
    response = system("ping "+ip+" -n 3")
    print(ip)
    print(hour)
    if response == 0:
        try:
            i = IP(ip=ip,hour=hour,minute=minute,second=second,status="UP")
            i.save()
            return "UP"
        except Exception as e:
            print(e)
            return "Exception"
    else:
        i = IP(ip=ip[0],hour=ip[1],minute=ip[2],second=ip[3],status="DOWN")
        i.save()
    return "Down"


@shared_task(bind=True)
def test_funct(self):
    for i in range(10):
        print(i)
    return "Down"
