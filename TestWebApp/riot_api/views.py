from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
import requests as req


def lobby(request):
    api_key = 'RGAPI-e0b7eb38-d249-4a43-b2c2-439603b6b'
    api_url = 'https://ru.api.riotgames.com/lol/summoner/v4/summoners/by-name/HappyMaser'
    correct_url = api_url + '?api_key=' + api_key
    resp = req.get(correct_url)

    match_url = 'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/pZzbGYE-1J3iEZif3znCxHsjYvpxpxcQTCuTDLCHTDtDj9Ht3KRQM_rnh74O0N2EexMkz56egVimkg/ids?start=0&count=20'
    match_url += '&api_key=' + api_key
    resp = req.get(match_url)

    cur_match_url = 'https://europe.api.riotgames.com/lol/match/v5/matches/RU_451842274'
    cur_match_url += '?api_key=' + api_key
    resp = req.get(cur_match_url)
    print(resp.json()['info']['participants'])
    return render(request, 'riot_api/home.html', {'title': 'Райоты', 'data': resp.json()['info']['participants'][0]})


class GameHome(LoginRequiredMixin, ListView):
    template_name = 'riot_api/home.html'
    model = None
    # context_object_name = 'game'
    login_url = reverse_lazy('not_auth')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Райоты'
        return context