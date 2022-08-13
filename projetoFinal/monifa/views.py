from django.shortcuts import render, redirect

from monifa.forms import CadastroForm
from monifa.models import Cadastro

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

