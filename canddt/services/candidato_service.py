from ..models import Candidato

def cadastrar_candidato(candidato):
    Candidato.objects.create(nome=candidato.nome, sexo=candidato.sexo, idade=
                             candidato.idade, nivel=candidato.nivel, formacao=
                             candidato.formacao, pix=candidato.pix, celular=
                             candidato.celular)

def listar_candidatos():
    return Candidato.objects.all()

def listar_candidato_id(id):
    return Candidato.objects.get(id=id)

def editar_candidato(candidato_bd, candidato_novo):
    candidato_bd.nome = candidato_novo.nome
    candidato_bd.sexo = candidato_novo.sexo
    candidato_bd.idade = candidato_novo.idade
    candidato_bd.nivel = candidato_novo.nivel
    candidato_bd.formacao = candidato_novo.formacao
    candidato_bd.pix = candidato_novo.pix
    candidato_bd.celular = candidato_novo.celular
    candidato_bd.save(force_update=True)

def remover_candidato(candidato_bd):
    candidato_bd.delete()