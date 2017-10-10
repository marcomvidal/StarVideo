"""
Views: App 'locacoes'
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Filme, Classificacao, Genero
from .forms import FilmeForm


class FilmeListView(ListView):
    """ Exibição de todos os `filmes` cadastrados. """
    model = Filme
    template_name = 'filmes/index.html'
    paginate_by = 8
    context_object_name = 'filmes'
    ordering = ['titulo']


def filmes_buscar(request):
    """ Exibição dos `filmes` que contenham um dado título. """
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


class FilmeDetailView(DetailView):
    """ Exibição detalhada e sem edição de um `filme`. """
    model = Filme
    template_name = 'filmes/detail.html'
     

def filmes_criar(request):
    """ Cadastro de `filmes`. """
    generos = Genero.objects.all()
    classificacoes = Classificacao.objects.all()

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


class FilmeDeleteView(DeleteView):
    """ Exclusão de um `filme` existente. """
    model = Filme
    success_url = reverse_lazy('locacoes:filmes-index')
