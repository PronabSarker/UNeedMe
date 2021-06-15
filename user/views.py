from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError
from .models import User, Message, Profile
from random import choice







from django.http.response import JsonResponse

from django.db.models import Q
import json

@login_required
def chatroom(request, pk:int):
    other_user = get_object_or_404(User, pk=pk)
    messages = Message.objects.filter(
        Q(receiver=request.user, sender=other_user)
    )
    messages.update(seen=True)
    messages = messages | Message.objects.filter(Q(receiver=other_user, sender=request.user) )
    return render(request, "chatroom.html", {"other_user": other_user, "messages": messages})


@login_required
def ajax_load_messages(request, pk):
    other_user = get_object_or_404(User, pk=pk)
    messages = Message.objects.filter(seen=False).filter(
        Q(receiver=request.user, sender=other_user)
    )
    message_list = [{
        "sender": message.sender.username,
        "message": message.message,
        "sent": message.sender == request.user
    } for message in messages]
    messages.update(seen=True)
    
    if request.method == "POST":
        message = json.loads(request.body)
        m = Message.objects.create(receiver=other_user, sender=request.user, message=message)
        message_list.append({
            "sender": request.user.username,
            "message": m.message,
            "sent": True,
        })
    print(message_list)
    return JsonResponse(message_list, safe=False)
















# Create your views here.
def index(request):
    return render(request,"index.html")
def contactus(request):
    return render(request,"contactus.html")
@login_required
def sector(request):
    obj = Profile.objects.all().exclude(id=request.user.id).exclude(id=1)
    return render(request,"sector.html", {'obj': obj})



def othersprofile(request, id):
    obj = Profile.objects.get(pk=id)
    return render(request,"othersprofile.html", {'obj': obj})


@login_required
def location(request):
    obj = Profile.objects.all().exclude(id=request.user.id).exclude(id=1)
    return render(request,"location.html", {'obj': obj})

@login_required
def profile(request,id):
    obj = get_object_or_404(User, pk=id)
    if request.method == "POST":
        q = get_object_or_404(Profile, pk=id)
        try: 
            image = request.FILES['image']
            q.image=image
        except MultiValueDictKeyError:
            pass
        full_name = request.POST['full_name']
        
        phone = request.POST['phone']
        location = request.POST['location']
        sector = request.POST['sector']
        about = request.POST['about']

        

        institute1 = request.POST['institute1']
        institute2 = request.POST['institute2']
        institute3 = request.POST['institute3']
        #institute4 = request.POST['institute4']

        degree1 = request.POST['degree1']
        degree2 =request.POST['degree2']
        degree3 = request.POST['degree3']
        #degree4 = request.POST['full_name']

        year1 = request.POST['year1']
        year2 = request.POST['year2']
        year3 = request.POST['year3']
        #year4 = request.POST['year4']

        grade1 = request.POST['grade1']
        grade2 = request.POST['grade2']
        grade3 = request.POST['grade3']
        #grade4 = request.POST['grade4']

        skills = request.POST['skills']
        certifications = request.POST['certifications']

        companyname1 = request.POST['companyname1']
        companyname2 = request.POST['companyname2']
        companyname3 = request.POST['companyname3']

        position1 = request.POST['position1']
        position2 = request.POST['position2']
        position3 = request.POST['position3']

        duty1 = request.POST['duty1']
        duty2 = request.POST['duty2']
        duty3 = request.POST['duty3']

        timeperiod1 = request.POST['timeperiod1']
        timeperiod2 = request.POST['timeperiod2']
        timeperiod3 = request.POST['timeperiod3']

        project = request.POST.get('project', False)
        interest = request.POST['interest']


        
        #q.image= image
        q.full_name = full_name
        q.phone = phone
        q.location = location
        q.sector = sector
        
        q.about = about

        q.institute1 = institute1
        q.institute2 = institute2
        q.institute3 = institute3
        #q.institute4 = institute4

        q.degree1 = degree1
        q.degree2 = degree2
        q.degree3 = degree3
        #q.degree4 = degree4

        q.year1 = year1
        q.year2 = year2
        q.year3 = year3
        #q.year4 = year4

        q.grade1 = grade1
        q.grade2 = grade2
        q.grade3 = grade3
        #q.grade4 = grade4

        q.skills = skills
        q.certifications = certifications

        q.companyname1 = companyname1
        q.companyname2 = companyname2
        q.companyname3 = companyname3

        q.position1 = position1
        q.position2 = position2
        q.position3 = position3

        q.duty1 = duty1
        q.duty2 = duty2
        q.duty3 = duty3

        q.timeperiod1 = timeperiod1
        q.timeperiod2 = timeperiod2
        q.timeperiod3 = timeperiod3

        q.project = project
        q.interest = interest

        q.save()
        return redirect('/')

    return render(request, "profile.html", {'obj': obj})


    
def search(request):
    if request.method == 'POST':
        src = request.POST['query']
        if src:
            obj = Profile.objects.filter(Q(full_name__icontains=src) | Q(sector__icontains=src) | Q(location__icontains=src))
            if obj:
                return render(request,"search.html", {'obj': obj})
            else:
                messages.error(request, 'No search result')
        else:
            return render(request,"search.html", {})
    return render(request,"search.html", {})


def khulna(request):
    
    src = 'khulna'
    if src:
        obj = Profile.objects.filter(Q(location__icontains=src))
        if obj:
            return render(request,"khulna.html", {'obj': obj})
        else:
            messages.error(request, 'No search result')
    else:
        return render(request,"khulna.html", {})
    return render(request,"khulna.html", {})



'''def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        myuser = auth.authenticate(username=username, password=password)
        if myuser is not None:
            auth.login(request, myuser)
            return redirect('sector')
        else:
            return redirect('login')

    else:
        return render(request, 'login.html')'''

'''def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password2 == password:
            if User.objects.filter(username=request.POST['email']).exists():
                return HttpResponse("Username Exist")
            elif User.objects.filter(email=request.POST['email']).exists():
                return HttpResponse("Email Exist")
            else:
                myuser = User.objects.create_user(username=username, email=email, password=password)
                myuser.save()
                auth.login(request, myuser)
                #messages.success(request, "Account created successfully")
                return redirect('profile')

        else:

            return HttpResponse('input error')
    else:
        return render(request, 'signup.html')'''