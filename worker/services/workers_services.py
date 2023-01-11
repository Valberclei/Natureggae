from ..models import Worker

def cadastrar_worker(worker):
    Worker.objects.create(nome=worker.nome, email=worker.email, address=worker.address
                          , data_nas=worker.data_nas, sex=worker.sex
                          , area=worker.area, level=worker.level
                          , phone=worker.phone, link_social=worker.link_social)

def listar_workers():
    return Worker.objects.all()

def listar_worker_id(id):
    return Worker.objects.get(id=id)

def atualizar_worker(worker_bd, worker_novo):
    worker_bd.nome = worker_novo.nome
    worker_bd.email = worker_novo.email
    worker_bd.address = worker_novo.address
    worker_bd.data_nas = worker_novo.data_nas
    worker_bd.sex = worker_novo.sex
    worker_bd.area = worker_novo.area
    worker_bd.level = worker_novo.level
    worker_bd.phone = worker_novo.phone
    worker_bd.link_social = worker_novo.link_social
    worker_bd.save(force_update=True)