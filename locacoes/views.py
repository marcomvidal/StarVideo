"""
Views: App 'locacoes'
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponseRedirect, HttpResponse

from .models import Filme
from .forms import FilmeForm


def filmes_create(request):
    """ Cadastro de filmes """

    if request.method == 'POST':
        form = FilmeForm(request.POST, request.FILES)

        if form.is_valid():
            filme = form.save(commit=False)
            filme.usuario = request.user
            filme.save()

            return HttpResponseRedirect('/filmes/sucesso/')

    form = FilmeForm()

    context = {
        'form': form
    }
    return render(request, 'filmes/form.html', context)


def filmes_edit(request, pk):
    """Edição de um filme existente"""
    filme = get_object_or_404(Filme, pk=pk)

    if request.POST:
        form = FilmeForm(request.POST, instance=filme)

        if form.is_valid():
            filme = form.save(commit=False)
            filme.usuario = request.user
            filme.save()

            return HttpResponseRedirect('/filmes/sucesso/')
    else:
        form = FilmeForm(instance=filme)

    context = {
        'form': form
    }

    return render(request, 'filmes/form.html', context)


class FilmeIndexView(ListView):
    """ Exibição de todos os filmes cadastrados no banco de dados. """
    template_name = 'filmes/index.html'
    context_object_name = 'filmes'

    def get_queryset(self):
        return Filme.objects.order_by('titulo')


def success(request):
    return HttpResponse("Sucesso!")


def fail(request):
    return HttpResponse("Falha!")