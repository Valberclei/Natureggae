from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CandidatoForm
from .entidades.candidato import Candidato
from .services import candidato_service

# Create your views here.
def listar_candidatos(request):
    candidatos = candidato_service.listar_candidatos()

    return render(request, 'candidatos/listar_candidatos.html',
                  {"candidatos": candidatos})

@login_required
def cadastrar_candidato(request):
    if request.method == "POST":
        form_candidato = CandidatoForm(request.POST)
        if form_candidato.is_valid():
            nome = form_candidato.cleaned_data["nome"]
            sexo = form_candidato.cleaned_data["sexo"]
            idade = form_candidato.cleaned_data["idade"]
            nivel = form_candidato.cleaned_data["nivel"]
            formacao = form_candidato.cleaned_data["formacao"]
            pix = form_candidato.cleaned_data["pix"]
            celular = form_candidato.cleaned_data["celular"]
            candidato_novo = Candidato(nome=nome, sexo=sexo, idade=idade, nivel=nivel, formacao=formacao, pix=pix, celular=celular)
            candidato_service.cadastrar_candidato(candidato_novo)
            return redirect('users-register')
    else:
        form_candidato = CandidatoForm()
    return render(request, 'candidatos/form_candidato.html', {"form_candidato": form_candidato})

def editar_candidato(request, id):
    candidato_bd = candidato_service.listar_candidato_id(id)
    form_candidato = CandidatoForm(request.POST or None, instance=candidato_bd)
    if form_candidato.is_valid():
        nome = form_candidato.cleaned_data["nome"]
        sexo = form_candidato.cleaned_data["sexo"]
        idade = form_candidato.cleaned_data["idade"]
        nivel = form_candidato.cleaned_data["nivel"]
        formacao = form_candidato.cleaned_data["formacao"]
        pix = form_candidato.cleaned_data["pix"]
        celular = form_candidato.cleaned_data["celular"]
        candidato_novo = Candidato(nome=nome, sexo=sexo, idade=idade, nivel=nivel, formacao=formacao, pix=pix,
                                   celular=celular)
        candidato_service.editar_candidato(candidato_bd, candidato_novo)
        return redirect('home')
    return render(request, 'candidatos/form_candidato.html', {"form_candidato": form_candidato})

def remover_candidato(request, id):
    candidato_db = candidato_service.listar_candidato_id(id)
    if request.method == "POST":
        candidato_service.remover_candidato(candidato_db)
        return redirect('home')
    return render(request, 'candidatos/confirma_exclusao.html', {'candidato': candidato_db})