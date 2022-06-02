from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Inventory
# Create your views here.

def Courses(request):
    inventoryList = Inventory.objects.all()
    il = loader.get_template('inlists/items.html')
    context = {
        'inventoryList' : inventoryList
    }
    return HttpResponse(il.render(context, request))