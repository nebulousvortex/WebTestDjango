from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RegisterUserForm, LoginUserForm
from .utils import DataMixin


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = "main/register.html"
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = "main/login.html"

    def get_success_url(self):
        return reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))


def index(request):
    data = {
        'title': 'Главная страница',
        'text': 'Текст передачи',
        'values': ['One', 'Two', 'Three'],
        'information': {
            'name': 'Fedor',
            'age': '22'
        }
    }
    return render(request, 'main/main.html', data)


def about(request):
    return render(request, 'main/about.html')


def archive(request, year):
    if int(year) > 2024:
        return redirect("home")
    return HttpResponse(f'<h1> Архив по годам </h1> <p>{year}</p>')


def logout_user(request):
    logout(request)
    return redirect('login')
