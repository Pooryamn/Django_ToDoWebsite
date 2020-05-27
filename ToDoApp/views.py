from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login

# Create your views here.
def SignUpUser(request):
    
    if(request.method == "GET"):
        return render(request,'ToDoApp/SignUpUser.html',{'form': UserCreationForm()})
    else:
        # Create New user

        # Check if pass1 and pass2 is same
        if (request.POST['password1']==request.POST['password2']):
            
            try:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()

            except IntegrityError:
                return render(request,'ToDoApp/SignUpUser.html',{'form': UserCreationForm(),'error':'that Username has already exists!'})     

        else:
            #tell user password isnt match
            return render(request,'ToDoApp/SignUpUser.html',{'form': UserCreationForm(),'error':'Passwords did not match!'})