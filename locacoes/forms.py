"""
Forms: App 'locacoes'
"""
from django import forms
from .models import Filme, Classificacao, Genero


class FilmeForm(forms.ModelForm):
    data_lancamento = forms.DateTimeField(required=False)
    capa            = forms.ImageField(required=False)
    blockbuster     = forms.BooleanField(required=False, initial=True)

    class Meta:
        model = Filme
        fields = ('titulo',
                  'sinopse',
                  'quantidade',
                  'data_lancamento',
                  'blockbuster',
                  'capa',
                  'classificacao',
                  'genero',
                  )
