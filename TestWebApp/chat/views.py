from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView

from chat.models import Messages


def lobby(request):
    return render(request, 'chat/home.html', {'title': 'Чатик'})


class ChatHome(LoginRequiredMixin, ListView):
    queryset = Messages.objects.all()
    template_name = 'chat/home.html'
    context_object_name = 'chat'
    login_url = reverse_lazy('not_auth')
    # ordering = ['date']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Чатик'
        return context