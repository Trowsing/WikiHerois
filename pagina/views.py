# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from .models import Heroes
from .forms import HeroesForm

favs = []

def home(request): # Listagem Inicial
    posts = Heroes.objects.all()
    query = request.GET.get("pesquisa")
    if query:
        posts = posts.filter(name__icontains=query)
    return render(request, 'home.html', {'posts': posts})

def model_upload(request): # Adicionar personagens
    if request.method == 'POST':
        form = HeroesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = HeroesForm()
    return render(request, 'model_upload.html', {'form': form})


def model_edit(request, pk): # Edição de personagens
    instance = get_object_or_404(Heroes, pk=pk) # Primary key de cada instancia
    form = HeroesForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        form.save()
        return redirect('home')
    return render(request, 'model_edit.html', {'form': form})


def model_delete(request, pk): # Apagar personagens
    delete_character = get_object_or_404(Heroes, pk=pk).delete()
    return redirect('home')


def add_favorites(request, pk): # Adição de favoritos
    posts = get_object_or_404(Heroes, pk=pk)
    if pk in favs:
        favs.remove(pk)
        posts.is_favorite=False
        posts.save()
    else:
        favs.append(pk)
        posts.is_favorite = True
        posts.save()
        return redirect('favoritos')
    return redirect('home')


def favoritos(request): # Função para listar favoritos
    all = Heroes.objects.all()
    posts = all.filter(is_favorite=True)
    return render(request, 'favoritos.html', {'posts': posts})
