from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def SignUpUser(request):

    return render(request,'ToDoApp/SignUpUser.html',{'form': UserCreationForm()})