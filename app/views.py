from django.shortcuts import render
from app.models import *
# Create your views here.
def displaydata(request):
    tpo =Topic.objects.all()
    d={'tpo':tpo}
    return render(request,'displaydata.html',d)

