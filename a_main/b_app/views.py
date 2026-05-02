from django.shortcuts import render
from .models import *

# Create your views here.



def home_page(request):
    if request.method=='POST':
        data=request.POST
        dep_name=data.get('dep_name')





        Departmet.objects.create(
        dep_name=dep_name,

        )

    return render(request,'home.html')