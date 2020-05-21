from django.views import View
from django.http.response import HttpResponse
from django.shortcuts import render

line_of_cars = {'change_oil': [],
                'inflate_tires': [],
                'diagnostic': []}

id_ticket = 0


class WelcomeView(View):
    def get(self):
        return HttpResponse('<h2>Welcome to the Hypercar Service!</h2>')


class MenuView(View):
    menu = {'change_oil': 'Change oil',
            'inflate_tires': 'Inflate tires',
            'diagnostic': 'Get diagnostic test'}
    template_name = 'tickets/menu.html'

    def get(self, request):
        return render(request, self.template_name, context={'menu': self.menu})


class GetTicket(View):
    template_name = 'tickets/get_ticket.html'
    ticket_type = None

    def start(self, ticket_type):
        self.ticket_type = ticket_type
        print(self.ticket_type)
        self.as_view()

    def get(self, request):
        context = self.getting_number()
        return render(request, self.template_name, context=context)

    def getting_number(self):
        global id_ticket
        if self.ticket_type in line_of_cars.keys():
            minutes = self.count_waiting_time()
            id_ticket += 1
            line_of_cars[self.ticket_type].append(id_ticket)
            return {'id_ticket': str(id_ticket),
                    'minutes': str(minutes)}

    def count_waiting_time(self):
        change_oil = len(line_of_cars['change_oil']) * 2
        inflate_tires = change_oil + len(line_of_cars['inflate_tires']) * 5
        diagnostic = inflate_tires + len(line_of_cars['diagnostic']) * 30
        if self.ticket_type == 'change_oil':
            return change_oil
        if self.ticket_type == 'inflate_tires':
            return inflate_tires
        if self.ticket_type == 'diagnostic':
            return diagnostic
