from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Notes
from .forms import NoteForm


class UpdateHome(LoginRequiredMixin, ListView):
    paginate_by = 3
    model = Notes
    template_name = 'database/home.html'
    context_object_name = 'notes'
    login_url = reverse_lazy('not_auth')
    ordering = ['-date']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список обновлений'
        return context


class UpdateShow(DetailView):
    model = Notes
    template_name = 'database/note.html'
    context_object_name = 'note'
    pk_url_kwarg = 'note_id'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обновление'
        return context


class UpdateCreate(CreateView):
    pass


def show_note(request, note_id):
    note = get_object_or_404(Notes, pk=note_id)

    context = {
        'note': note,
        'title': note.title,
    }

    return render(request, 'database/note.html', context=context)


def create_note(request):
    error = ''
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data_base_home')
        else:
            error = 'Неверные данные'
    form = NoteForm()
    data = {'form': form,
            'error': error
            }
    return render(request, 'database/create.html', data)


def not_auth(request):
    return render(request, 'main/not_login_user.html')
