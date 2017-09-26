"""
Views: App 'locacoes'
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponseRedirect, HttpResponse

from .models import Filme, Classificacao, Genero
from .forms import FilmeForm


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


class FilmeIndexView(ListView):
    """ Exibição de todos os filmes cadastrados """
    template_name = 'filmes/index.html'
    context_object_name = 'filmes'

    def get_queryset(self):
        return Filme.objects.order_by('titulo')
