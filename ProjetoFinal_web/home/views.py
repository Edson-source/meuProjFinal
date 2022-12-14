from django.shortcuts import render, redirect

from home.forms import CadastroForm
from home.models import Cadastro

# Create your views here.
def home(request):
  data = {}
  data['db'] = Cadastro.objects.all()
  return render(request, 'home.html', data)

def cadastro(request):
  data = {}
  data['formu'] = CadastroForm()
  return render(request, 'index.html', data)

def create(request):
  form = CadastroForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('/')

def view(request, pk):
  data = {}
  data['db'] = Cadastro.objects.get(pk=pk)
  return render(request, 'view.html', data)

def edit(request, pk):
  data = {}
  data['db'] = Cadastro.objects.get(pk=pk)
  data['formu'] = CadastroForm(instance=data['db'])
  return render(request, 'index.html', data)

def update(request, pk):
  data = {}
  data['db'] = Cadastro.objects.get(pk=pk)
  form = CadastroForm(request.POST or None, instance=data['db'])
  if form.is_valid():
    form.save()
  return redirect('/')

def delete(request, pk):
  db = Cadastro.objects.get(pk=pk)
  db.delete()
  return redirect('/')

