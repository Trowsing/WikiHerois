# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from .models import Presentation
from django import forms
from django.views.generic import DeleteView
from .forms import PresentationForm


def home(request): # Listagem Inicial
    posts = Presentation.objects.all()
    query = request.GET.get("pesquisa")
    if query:
        posts = posts.filter(name__icontains=query)
    return render(request, 'home.html', {'posts': posts})

def model_upload(request): # Adicionar personagens
    if request.method == 'POST':
        form = PresentationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PresentationForm()
    return render(request, 'model_upload.html', {'form': form})


def model_edit(request, pk): # Edição de personagens
    instance = get_object_or_404(Presentation, pk=pk) # Primary key de cada instancia
    form = PresentationForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        form.save()
        return redirect('home')
    return render(request, 'model_edit.html', {'form': form})


def model_delete(request, pk): # Apagar personagens
    delete_character = get_object_or_404(Presentation, pk=pk).delete()
    return redirect('home')


def favorites(request):
# Listar todos - Definir os favoritos - Mostrar favoritos em favorites.html
    posts = Presentation.objects.all()
    favorites = posts.filter(is_favorite=True)
    if posts.is_favorite:
        posts.is_favorite=False
    else:
        posts.is_favorite=True
    return render(request, 'home.html', {'posts': posts})
