from django.shortcuts import render, redirect
from .models import *
import os
from django.db.models import Q
from django.contrib import messages
# Create your views here.


def home(request):
    if request.method == 'GET':
        src = request.GET.get('src')
        if src:
            prof = Profile.objects.filter(name__icontains=src)
        elif src==None:
            prof = Profile.objects.all()
        else:
            prof = Profile.objects.all()

    return render(request, "home.html", {'prof': prof})


def delete(request, id):
    prof = Profile.objects.get(id=id)
    if prof.image != 'def.png':
        os.remove(prof.image.path)
    prof.delete()
    return redirect('home')


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('img')
        email = request.POST.get('email')
        phone_number = request.POST.get('num')
        gender = request.POST.get('gender')
        address = request.POST.get('add')
        religion = request.POST.get('religion')
        blood_group = request.POST.get('blood_group')
        date_of_birth = request.POST.get('birth')
        is_alive = request.POST.get('is_alive')

        if Profile.objects.filter(Q(name=name) | Q(email=email)).exists():
            messages.warning(request, "this name or email already taken.")
            return redirect('create')
        else:
            if image:
                if is_alive == '1':
                    prof = Profile.objects.create(name=name, image=image, email=email, phone_number=phone_number,
                                                gender=gender, address=address, religion=religion,
                                                blood_group=blood_group, date_of_birth=date_of_birth)
                    
                    prof.save()
                    messages.success(request, "Account Created.")
                    return redirect('home')
                else:
                    prof = Profile.objects.create(name=name, image=image, email=email, phone_number=phone_number,
                                                gender=gender, address=address, religion=religion,
                                                blood_group=blood_group, date_of_birth=date_of_birth, is_alive=False)
                    prof.save()
                    messages.success(request, "Account Created.")
                    return redirect('home')
            else:
                if is_alive == '1':
                    prof = Profile.objects.create(name=name, email=email, phone_number=phone_number,
                                                gender=gender, address=address, religion=religion,
                                                blood_group=blood_group, date_of_birth=date_of_birth)
                    prof.save()
                    messages.success(request, "Account Created.")
                    return redirect('home')
                else:
                    prof = Profile.objects.create(name=name, email=email, phone_number=phone_number,
                                                gender=gender, address=address, religion=religion,
                                                blood_group=blood_group, date_of_birth=date_of_birth, is_alive=False)
                    prof.save()
                    messages.success(request, "Account Created.")
                    return redirect('home')
    return render(request, 'create.html')


def single_page(request, id):
    prof = Profile.objects.get(id=id)
    return render (request, 'single_profile.html', locals())

    
def update_page(request, id):
    prof = Profile.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('img')
        email = request.POST.get('email')
        phone_number = request.POST.get('num')
        gender = request.POST.get('gender')
        address = request.POST.get('add')
        religion = request.POST.get('religion')
        blood_group = request.POST.get('blood_group')
        date_of_birth = request.POST.get('birth')
        is_alive = request.POST.get('is_alive')
        if prof.image != 'def.png':
            os.remove(prof.image.path)
            prof.image = image
        prof.name = name
        prof.email = email
        prof.phone_number = phone_number
        prof.gender = gender
        prof.address = address
        prof.religion = religion
        prof.blood_group = blood_group
        prof.date_of_birth = date_of_birth
        if is_alive != '1':
            prof.is_alive = False

        prof.save()
        return redirect('home')
    return render (request, 'update.html', locals())