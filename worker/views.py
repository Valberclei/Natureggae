from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from .forms import WorkerForm
from .entidades.worker import Worker
from .services import workers_services

def success(request):
    return render(request, 'workers/success.html')
@login_required
@permission_required('is_superuser')
def listar_workers(request):

    workers = workers_services.listar_workers()
    return render(request, 'workers/listar_workers.html', {"workers": workers})

@login_required()
def cadastrar_worker(request):
    if request.method == "POST":
        form_worker = WorkerForm(request.POST)
        if form_worker.is_valid():
            nome = form_worker.cleaned_data["nome"]
            email = form_worker.cleaned_data["email"]
            address = form_worker.cleaned_data["address"]
            data_nas = form_worker.cleaned_data["data_nas"]
            sex = form_worker.cleaned_data["sex"]
            area = form_worker.cleaned_data["area"]
            level = form_worker.cleaned_data["level"]
            phone = form_worker.cleaned_data["phone"]
            link_social = form_worker.cleaned_data["link_social"]

            worker_novo = Worker(nome=nome, email=email, address=address, data_nas=data_nas, sex=sex, area=area, level=level, phone=phone, link_social=link_social)
            workers_services.cadastrar_worker(worker_novo)
            return redirect('success')
    else:
        form_worker = WorkerForm()
    return render(request, 'workers/form_worker.html', {"form_worker": form_worker})

def atualizar_worker(request, id):
    worker_bd = workers_services.listar_worker_id(id)
    form_worker = WorkerForm(request.POST or None, instance=worker_bd)
    if form_worker.is_valid():
        nome = form_worker.cleaned_data["nome"]
        email = form_worker.cleaned_data["email"]
        address = form_worker.cleaned_data["address"]
        data_nas = form_worker.cleaned_data["data_nas"]
        sex = form_worker.cleaned_data["sex"]
        area = form_worker.cleaned_data["area"]
        level = form_worker.cleaned_data["level"]
        phone = form_worker.cleaned_data["phone"]
        link_social = form_worker.cleaned_data["link_social"]

        worker_novo = Worker(nome=nome, email=email, address=address, data_nas=data_nas, sex=sex, area=area, level=level, phone=phone, link_social=link_social)
        workers_services.atualizar_worker(worker_bd, worker_novo)
        return redirect('success')
    return render(request, 'workers/form_worker.html', {"form_worker": form_worker})