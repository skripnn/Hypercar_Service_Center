from django.views import View
from django.http.response import HttpResponse
from django.shortcuts import render


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h2>Welcome to the Hypercar Service!</h2>')


class MenuView(View):
    menu = {'change_oil': 'Change oil',
            'inflate_tires': 'Inflate tires',
            'diagnostic': 'Get diagnostic test'}
    template_name = 'tickets/base.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'menu': self.menu})
