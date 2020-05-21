from django.shortcuts import render

# Create your views here.
def SignUpUser(request):
    return render(request,'ToDoApp/SignUpUser.html')