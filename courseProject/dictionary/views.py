from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from . import models, forms
from django.shortcuts import render, redirect
from django.utils import timezone
from django.shortcuts import get_object_or_404


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
@login_required(login_url='authorization/login')
def dictionaryGet(request):
    words = request.user.words.all()
    words_list = []
    for word in words:
        translations = word.translation.get("values")
        trans_str = translations[0]

        for i in range(1, len(translations)):
            trans_str += " | " + translations[i]

        words_list.append({
            'word_id': word.id,
            'word': word.word,
            'translations': trans_str,
            'last_date': word.lastRead
        })

    context = {
        'words_list': words_list
    }

    return render(request, 'dictionary/get.html', context)


@login_required(login_url='authorization/login')
def createWord(request, fields=0):
    if request.method == 'POST':
        try:
            translations = {"values": [request.POST['translation']]}
            for i in range(1, fields + 1):
                translations.get("values").append(request.POST[f'translation_{i}'].strip())

            word = models.Word(
                word=request.POST['word'].strip(),
                translation=translations,
                lastRead=timezone.now()
            )
            word.save()

            request.user.words.add(word)
            request.user.save()

            return redirect('/')
        except Exception as err:
            print(err)

    context = {
        'fieldsRange': range(1, fields + 1),
        'fields': fields,
        'nextFields': fields + 1,
        'prevFields': fields - 1,
    }
    return render(request, 'dictionary/word/create.html', context)


@login_required(login_url='authorization/login')
def deleteWord(request, word_id):
    word = get_object_or_404(models.Word, id=word_id)
    if word in request.user.words.all():
        if request.method == "POST":
            word.delete()
            return redirect('/dictionary')

        translations = word.translation.get("values")
        trans_str = translations[0]

        for i in range(1, len(translations)):
            trans_str += " | " + translations[i]

        context = {
            'word': word.word,
            'translations': trans_str,
            'creation_date': word.publishDate
        }

        return render(request, 'dictionary/word/delete.html', context)
    else:
        return render(request, 'dictionary/word/fake.html', {})


def detailsWord(request, word_id):
    word = get_object_or_404(models.Word, id=word_id)
    if word in request.user.words.all():
        context = {
            'word': word
        }

        return render(request, 'dictionary/word/details.html', context)

    else:
        return render(request, 'dictionary/word/fake.html', {})


# =============   Other   ===================

@login_required(login_url='authorization/login')
def index(request):
    return render(request, 'index.html', {})

