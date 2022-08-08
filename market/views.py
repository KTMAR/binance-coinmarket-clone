from django.shortcuts import render
from django.views import View
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'index.html')


class LoginView(View):
    """Инстациируем форму"""

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        context = {
            'form': form,

        }
        return render(request, 'login.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/')
        # если че то не получилось при авторизации(не валидна)
        context = {
            'form': form,
        }
        return render(request, 'login.html', context)


class RegistrationView(View):

    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        context = {
            'form': form,

        }
        return render(request, 'registration.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']

            new_user.save()
            """Что бы присвоить пассворд,нужно сначала сохранить юзера(new_user),а потом уже задать ему пароль"""
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()

            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            """Залогиним юзера"""

            login(request, user)
            return HttpResponseRedirect('/')
        context = {
            'form': form
        }
        return render(request, 'registration.html', context)
