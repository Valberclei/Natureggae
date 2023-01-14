from ..models import Contact

def enviar_contact(contact):
    Contact.objects.create(nome=contact.nome, email=contact.email, message=contact.message)

def listar_contacts():
    return Contact.objects.all()

def listar_contact_id(id):
    return Contact.objects.get(id=id)

def remover_contact(contact_bd):
    contact_bd.delete()