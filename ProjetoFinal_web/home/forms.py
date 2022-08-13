from django.forms import ModelForm
from home.models import Cadastro

class CadastroForm(ModelForm):
  class Meta:
    model = Cadastro
    fields = ['username', 'email', 'senha']