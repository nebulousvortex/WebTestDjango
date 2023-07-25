from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView


def lobby(request):
    return render(request, 'game/home.html', {'title': 'Игра'})


class GameHome(LoginRequiredMixin, ListView):
    template_name = 'game/home.html'
    model = None
    # context_object_name = 'game'
    login_url = reverse_lazy('not_auth')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Игра'
        return context
