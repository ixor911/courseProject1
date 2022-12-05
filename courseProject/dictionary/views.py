from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from . import models, forms
from django.shortcuts import render, redirect
from django.utils import timezone


@login_required(login_url='authorization/login')
def index(request):
    return render(request, 'index.html', {})


# =============   authorization   ===================

def loginUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("../")
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'authorization/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('../')


def register(request):
    form = forms.CreateUserForm()

    if request.method == 'POST':
        form = forms.CreateUserForm(request.POST)
        if request.POST['password1'] == request.POST['password2']:
            user = models.User(username=request.POST['username'],
                        email=request.POST['email'],
                        password=request.POST['password1'])

            user.save()
            login(request, user)
            return redirect('../')

    context = {'form': form}

    return render(request, 'authorization/register.html', context)


# =============   Dictionary   ===================

def createWord(request):
    if request.method == 'POST':
        try:
            word = models.Word(
                word=request.POST['word'],
                translation=request.POST['translation'],
                lastRead=timezone.now()
            )
            word.save()

            request.user.words.add(word)
            request.user.save()

            return redirect('../../')
        except Exception as err:
            print(err)

    context = {}
    return render(request, 'word/wordCreate.html', context)



