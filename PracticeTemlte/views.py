from django.shortcuts import render
from django.http import HttpResponse
from .models import TravelPlaces

def index(request):
    # t_place=TravelPlaces()
    # t_place.location='Mumbai'
    # t_place.price='700'
    # t_place.img='destination_1.jpg'
    # t_place.description='City of that never sleeps'
    # t_place.offer=True

    # t_place1=TravelPlaces()
    # t_place1.location='Banarash'
    # t_place1.price='500'
    # t_place1.img='destination_2.jpg'
    # t_place1.description='City of Gods'
    # t_place1.offer=False

    # t_place2=TravelPlaces()
    # t_place2.location='Delhi'
    # t_place2.price='650'
    # t_place2.img='destination_2.jpg'
    # t_place2.description='City with divercity of peoples'
    # t_place2.offer=False



    t_places=TravelPlaces.objects.all()#[t_place,t_place1,t_place2]
    return render(request,'index.html',{'t_places':t_places})

