from dataclasses import field
from pyexpat import model
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedingForm
from .models import Finches, Blade


def home(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finches.objects.all()
    return render(request, 'finch/index.html' , {
        'finches': finches
    })

def detail(request,finch_id):
    finch = Finches.objects.get(id=finch_id)
    feeding_form = FeedingForm()
    return render(request, 'finch/detail.html', {'finch':finch,'feeding_form': feeding_form})

def feed_finch(request, finch_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)
    


class CreateFinch(CreateView):
    model = Finches
    fields = '__all__'

class DeleteFinch(DeleteView):
    model = Finches
    success_url = '/finches/'

class EditFinch(UpdateView):
    model = Finches
    fields = '__all__'




class BladeList(ListView):
    model = Blade

class BladeDetail(DetailView):
    model = Blade

class BladeCreate(CreateView):
    model = Blade
    fields = '__all__'

class BladeUpdate(UpdateView):
    model = Blade
    fields = '__all__'

class BladeDelete(DeleteView):
    model = Blade
    success_url = '/blades/'
# Create your views here.
