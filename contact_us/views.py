from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from .entity.contact import Contact
from .services import contact_service

def success_contact(request):
    return render(request, 'contacts/success_contact.html')

def listar_contacts(request):

    contacts = contact_service.listar_contacts()
    return render(request, 'contacts/listar_contacts.html', {"contacts": contacts})


@login_required()
def enviar_contact(request):
    if request.method == "POST":
        form_contact = ContactForm(request.POST)
        if form_contact.is_valid():
            nome = form_contact.cleaned_data["nome"]
            email = form_contact.cleaned_data["email"]
            message = form_contact.cleaned_data["message"]

            message_nova = Contact(nome=nome, email=email, message=message)
            contact_service.enviar_contact(message_nova)
            return redirect('success_contact')
    else:
        form_contact = ContactForm()
    return render(request, 'contacts/form_contact.html', {"form_contact": form_contact})
