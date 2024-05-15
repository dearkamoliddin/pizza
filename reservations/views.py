from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from reservations.forms import ReservationForm
from datetime import datetime


class ReserveView(CreateView):
    template_name = 'reservation.html'
    form_class = ReservationForm

    def get_success_url(self):
        return reverse_lazy('pages:home')

    def form_valid(self, form):
        reservation = form.save(commit=False)
        data = form.cleaned_data

        date = str(data.get('date')).split('-')[::-1]
        date = '-'.join(date)
        date = datetime.strptime(date, '%d-%m-%Y').date()
        reservation.date = date
        reservation.save()
        return render(self.request, 'success.html')






    def form_invalid(self, form):
        print(form.errors)
        print(str(form.cleaned_data.get('date')))
        return render(self.request, 'form-errors.html', {'form': form})





