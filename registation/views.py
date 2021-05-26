from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserTrack
from django.urls import reverse

def Tracking(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        birthday = request.POST.get('birthday')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        nid = request.POST.get('nid')

        is_exist = UserTrack.objects.filter(email=email)
        if is_exist:
            messages.add_message(request, messages.WARNING, 'This email already has data')

        create_track = UserTrack.objects.create(fname=fname, lname=lname, birthday=birthday, email=email, phone_number=phone, gender=gender, nid=nid)
        create_track.save()
        messages.add_message(request, messages.SUCCESS, 'Your registation is complete')
        return redirect(reverse('usertrack:tracking'))

    return render(request, 'index.html')