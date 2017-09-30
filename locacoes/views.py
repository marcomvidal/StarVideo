"""
Views: App 'locacoes'
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from .models import Filme, Classificacao, Genero
from .forms import FilmeForm


def filmes_index(request):
    """ Exibição de todos os filmes cadastrados """
    filmes      = Filme.objects.all().order_by('titulo')
    paginator   = Paginator(filmes, 8) # Mostrar 8 filmes por página

    page = request.GET.get('page')
    try:
        filmes = paginator.page(page)
    except PageNotAnInteger:
        filmes = paginator.page(1)
    except EmptyPage:
        filmes = paginator.page(paginator.num_pages)

    context = {
        'filmes': filmes
    }

    return render(request, 'filmes/index.html', context)


def filmes_buscar(request):
    """ Exibição dos filmes que contenham um dado título """
    busca       = request.GET.get('campo_busca')
    filmes      = Filme.objects.filter(Q(titulo__icontains=busca)).order_by('titulo')
    paginator   = Paginator(filmes, 8) # Mostrar 8 filmes por página

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


def filmes_detalhes(request, pk):
    filme = get_object_or_404(Filme, pk=pk)

    context = {
        'filme': filme
    }

    return render(request, 'filmes/detail.html', context)


def filmes_criar(request):
    """ Cadastro de filmes """
    generos         = Genero.objects.all()
    classificacoes  = Classificacao.objects.all()

    if request.method == 'POST':
        form = FilmeForm(request.POST, request.FILES)

        if form.is_valid():
            filme = form.save(commit=False)
            filme.usuario = request.user
            filme.save()
            return redirect('locacoes:filmes-index')

    form = FilmeForm()

    context = {
        'form': form,
        'generos': generos,
        'classificacoes': classificacoes,
    }
    return render(request, 'filmes/form.html', context)


def filmes_editar(request, pk):
    """Edição de um filme existente"""
    filme           = get_object_or_404(Filme, pk=pk)
    generos         = Genero.objects.all()
    classificacoes  = Classificacao.objects.all()

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


def filmes_excluir(request, pk):
    '''Exclusão de uma postagem existente'''
    filme = Filme.objects.get(pk=pk)
    filme.delete()

    return redirect('locacoes:filmes-index')
