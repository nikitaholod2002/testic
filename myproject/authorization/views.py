
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User
from  posts.views import index

def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User(email = email, password = password)
            user.save()
            return redirect(authorization)
        else:
            return HttpResponse("Invalid data")
    form = UserForm
    return render(request, 'registration.html', {'form': form})

def authorization(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
        user = User.objects.get(email = email)
        if (user.email == email and user.password == password):
            request.session['user'] = email
            return redirect(index)
        else:
            return HttpResponse("Invalid data")
    form = UserForm
    return  render(request, 'authorization.html', {'form': form})
