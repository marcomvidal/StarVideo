"""
Forms: App 'locacoes'
"""
from django import forms
from .models import Filme, Cliente, Locacao


class FilmeForm(forms.ModelForm):
    """ Formulário do model `Filme`. """
    data_lancamento = forms.DateTimeField(required=False)
    capa = forms.ImageField(required=False)
    blockbuster = forms.BooleanField(required=False, initial=True)

    class Meta:
        model = Filme
        fields = (
                  'titulo',
                  'sinopse',
                  'quantidade',
                  'data_lancamento',
                  'blockbuster',
                  'capa',
                  'classificacao',
                  'genero',
                 )


class ClienteForm(forms.ModelForm):
    """ Formulário do model `Cliente`. """
    data_nascimento = forms.DateTimeField()
    rg = forms.CharField(required=False, min_length=9)
    cpf = forms.CharField(required=False, min_length=9)
    complemento = forms.CharField(required=False)
    email = forms.CharField(required=False)
    foto = forms.ImageField(required=False)
    banido = forms.BooleanField(required=False, initial=False)

    class Meta:
        model = Cliente
        fields = (
                  'nome',
                  'data_nascimento',
                  'rg',
                  'cpf',
                  'foto',
                  'endereco',
                  'numero',
                  'complemento',
                  'cep',
                  'uf',
                  'cidade',
                  'ddd',
                  'telefone',
                  'email',
                  'banido',
                 )

class LocacaoForm(forms.ModelForm):
    """ Formulário do model `Locação`. """
    data_inicio = forms.DateTimeField(required=True)
    data_fim = forms.DateTimeField(required=True)
    pago = forms.BooleanField(required=False, initial=False)
    multa = forms.DecimalField(max_digits=5, decimal_places=2, required=False)

    class Meta:
        model = Locacao
        fields = (
                  'data_inicio',
                  'data_fim',
                  'pago',
                  'multa',
                  'status_locacao',
                 )

class LocacaoClienteForm(forms.ModelForm):
    """ Formulário para seleção do `cliente` para a `locação`. """

    class Meta:
        model = Locacao
        fields = (
                  'cliente',
                 )

class LocacaoFilmeForm(forms.ModelForm):
    """ Formulário para seleção do `filme` para a `locação`. """

    class Meta:
        model = Locacao
        fields = (
                  'filmes',
                 )