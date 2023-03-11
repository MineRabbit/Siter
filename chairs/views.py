from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Chairs, Owner


def index(request):
    latest_chairs_list = Chairs.objects.all()
    context = {'latest_chairs_list': latest_chairs_list}
    return render(request, 'chairs/index.html', context)
    # gets the list of all chairs and renders index.html given this information


def detail(request, chair_id):
    cha = get_object_or_404(Chairs, pk=chair_id)
    own = cha.owner_idowner
    return render(request, 'chairs/detail.html', {'cha': cha})
    # tries to load the chairs of id "chair_id" and triggers an error 404 if it doesn't exist


def sell(request):
    return render(request, 'chairs/sell.html')


def confirm(request):
    try:
        # Storing all the information from the form
        sna = request.POST['seller-name']
        addr = request.POST['seller-address']
        na = request.POST['name']
        pri = request.POST['price']
        whe = request.POST['wheel']
        back = request.POST['backrest']
        if back == "Yes":
            backr = True
        else :
            backr = False
    except KeyError:
        return render(request, 'chairs/detail.html', {
            'error_message': "You didn't select a choice.",
        })
    else:
        own = Owner(name=sna, address=addr)
        # Checks if the owner already exist, if not creates a new entry in the database for the new owner
        check = Owner.objects.filter(name=sna, address=addr)
        if not check:
            print("I was there")
            own.save()
            cha = Chairs(name=na, price=pri, wheels=whe, backrest=backr, owner_idowner=own)
        else:
            cha = Chairs(name=na, price=pri, wheels=whe, backrest=backr, owner_idowner=check[0])
        cha.save()
        return render(request, 'chairs/confirm.html')


def buy(request, chair_id):
    Chairs.objects.filter(id=chair_id).delete()
    return render(request, 'bought.html')




