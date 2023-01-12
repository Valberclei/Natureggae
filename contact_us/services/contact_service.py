from ..models import Contact

def enviar_contact(contact):
    Contact.objects.create(nome=contact.nome, email=contact.email, message=contact.message)

def listar_contacts():
    return Contact.objects.all()