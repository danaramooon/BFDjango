from django.shortcuts import render,redirect
from .models import Restau,Dish
from .forms import RestaurantForm,DishForm,ResRevForm,DishRevForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
# Create your views here.
def restaurant(request):
    res = Restau.objects.all()
    context={
        'restaurants':res
    }
    return render(request,"restaurant.html",context)

def restaurant_detail(request,id):
    res = Restau.objects.get(pk=id)
    context={
        'res':res
    }
    return render(request,"restaurant_detail.html",context)
@login_required
def delete_res(request,id):
    res = Restau.objects.exclude(pk=id)
    context = {
        'restaurants': res
    }
    return render(request, "restaurant.html", context)
def dishes(request,id):
    res = Restau.objects.get(pk=id)
    context = {
        'dishes':res.dishes.all()
    }
    return render(request, "dish.html",context)

def dish_detail(request,id):
    dish=Dish.objects.get(pk=id)
    context={
        'dish':dish
    }
    return render(request, "dish_detail.html",context)

def delete_dish(request,id):
    dish = Dish.objects.get(pk=id)
    dish.delete()
    return render(request, "dish.html")

def res_rev(request,id):
    res = Restau.objects.get(pk=id)
    context={
        'ress':res.reviews.all()
    }
    return render(request, "res_rev.html",context)


def dish_rev(request,id):
    res = Dish.objects.get(pk=id)
    context = {
        'ress': res.reviews.all()
    }
    return render(request, "res_rev.html", context)
def home(request):
    return render(request,"home.html")

def add_restaurant(request):
    if request.method == "POST":
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant')
    else:
        form = RestaurantForm()
    context = {
        'form' : form
    }
    return render(request,'add_restaurant.html',context)
def add_dish(request):
    if request.method == "POST":
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant')
    else:
        form = DishForm()
    context = {
        'form' : form
    }
    return render(request,'add_dish.html',context)

def add_res_rev(request):
    if request.method == "POST":
        form = ResRevForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant')
    else:
        form = ResRevForm()
    context = {
        'form' : form
    }
    return render(request,'add_res_rev.html',context)

def add_dish_rev(request):
    if request.method == "POST":
        form = DishRevForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dish')
    else:
        form = DishRevForm()
    context = {
        'form' : form
    }
    return render(request,'add_dish_rev.html',context)

def user_detail(request,id):
    try:
        owner = User.objects.get(pk=id)
    except Restau.DoesNotExist:
        raise Http404("User not found")
    context = {
        'user': owner,
        'restaurants': owner.restaurants.all()
    }
    return render(request, "detail_user.html", context)