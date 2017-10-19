"""
Views: App 'locacoes'
"""
import re
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Filme, Classificacao, Genero, Cliente
from .forms import FilmeForm, ClienteForm


##############################################################################################################
# Módulo de Filmes
##############################################################################################################
class FilmeListView(ListView):
    """ Exibição de todos os `filmes` cadastrados. """
    model = Filme
    template_name = 'filmes/index.html'
    paginate_by = 8
    context_object_name = 'filmes'
    ordering = ['titulo']


def filmes_buscar(request):
    """ Exibição dos `filmes` que contenham um dado título. """
    busca = request.GET.get('campo_busca')
    filmes = Filme.objects.filter(Q(titulo__icontains=busca)).order_by('titulo')
    paginator = Paginator(filmes, 8) # Mostrar 8 filmes por página

    page = request.GET.get('page')
    try:
        filmes = paginator.page(page)
    except PageNotAnInteger:
        filmes = paginator.page(1)
    except EmptyPage:
        filmes = paginator.page(paginator.num_pages)

    context = {
        'filmes': filmes,
        'busca': busca
    }

    return render(request, 'filmes/index.html', context)


class FilmeDetailView(DetailView):
    """ Exibição detalhada e sem edição de um `filme`. """
    model = Filme
    template_name = 'filmes/detail.html'


@login_required
def filmes_criar(request):
    """ Cadastro de `filmes`. """
    generos = Genero.objects.all()
    classificacoes = Classificacao.objects.all()
    form = FilmeForm()

    if request.method == 'POST':
        form = FilmeForm(request.POST, request.FILES)

        if form.is_valid():
            filme = form.save(commit=False)
            filme.usuario = request.user
            filme.save()
            return redirect('locacoes:filmes-index')

    context = {
        'form': form,
        'generos': generos,
        'classificacoes': classificacoes,
    }

    return render(request, 'filmes/form.html', context)


@login_required
def filmes_editar(request, pk):
    """ Edição de um `filme` existente. """
    filme = get_object_or_404(Filme, pk=pk)
    generos = Genero.objects.all()
    classificacoes = Classificacao.objects.all()

    if request.method == 'POST':
        form = FilmeForm(request.POST, request.FILES, instance=filme)

        if form.is_valid():
            filme = form.save(commit=False)
            filme.usuario = request.user
            filme.save()
            return redirect('locacoes:filmes-index')
    else:
        form = FilmeForm(instance=filme)

    context = {
        'form': form,
        'filme': filme,
        'generos': generos,
        'classificacoes': classificacoes,
    }

    return render(request, 'filmes/form.html', context)


@method_decorator(login_required, name='dispatch')
class FilmeDeleteView(DeleteView):
    """ Exclusão de um `filme` existente. """
    model = Filme
    success_url = reverse_lazy('locacoes:filmes-index')


##############################################################################################################
# Módulo de Clientes
##############################################################################################################
class ClienteListView(ListView):
    """ Exibição de todos os `clientes` cadastrados. """
    model = Cliente
    template_name = 'clientes/index.html'
    paginate_by = 8
    context_object_name = 'clientes'
    ordering = ['nome']


def clientes_buscar(request):
    """ Exibição dos `clientes` que contenham um dado nome. """
    busca = request.GET.get('campo_busca')
    clientes = Cliente.objects.filter(Q(nome__icontains=busca)).order_by('nome')
    paginator = Paginator(clientes, 8) # Mostrar 8 clientes por página

    page = request.GET.get('page')
    try:
        clientes = paginator.page(page)
    except PageNotAnInteger:
        clientes = paginator.page(1)
    except EmptyPage:
        clientes = paginator.page(paginator.num_pages)

    context = {
        'clientes': clientes,
        'busca': busca
    }

    return render(request, 'clientes/index.html', context)


class ClienteDetailView(DetailView):
    """ Exibição detalhada e sem edição de um `cliente`. """
    model = Cliente
    template_name = 'clientes/detail.html'


@login_required
def clientes_criar(request):
    """ Cadastro de `filmes`. """
    form = ClienteForm()

    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES)

        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.usuario = request.user
            cliente.save()
            return redirect('locacoes:clientes-index')

    context = {
        'form': form,
    }

    return render(request, 'clientes/form.html', context)


@login_required
def clientes_editar(request, pk):
    """ Edição de um `cliente` existente. """
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES, instance=cliente)

        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.usuario = request.user
            cliente.save()
            return redirect('locacoes:clientes-index')
    else:
        form = ClienteForm(instance=cliente)

    context = {
        'form': form,
        'cliente': cliente,
    }

    return render(request, 'clientes/form.html', context)


@method_decorator(login_required, name='dispatch')
class ClienteDeleteView(DeleteView):
    """ Exclusão de um `filme` existente. """
    model = Cliente
    success_url = reverse_lazy('locacoes:clientes-index')
