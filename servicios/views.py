from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import CarroForm
from .forms1 import ClienteForm
from .forms2 import ServicioForm
from servicios.models import Cliente, Carro, Servicio, Detalle


def list_carro(request):
    carros= Carro.objects.all()
    return render(request, 'servicios/list_carro.html', {'carros':carros})
@login_required
def carro_detail(request, pk):
    carro = get_object_or_404(Carro, pk=pk)
    servicio = Servicio.objects.all()
    return render(request, 'servicios/carro_detail.html', {'carro': carro, 'servicio': servicio})

@login_required
def servicio_nuevo (request):
    if request.method == "POST":
        formulario = CarroForm(request.POST)
        if formulario.is_valid():
            carro = Carro.objects.create(cliente=formulario.cleaned_data['cliente'], placa=formulario.cleaned_data['placa'], marca = formulario.cleaned_data['marca'], linea = formulario.cleaned_data['linea'], modelo = formulario.cleaned_data['modelo'], color = formulario.cleaned_data['color'])
            for servicio_id in request.POST.getlist('servicios'):
                detalle = Detalle(servicio_id=servicio_id, carro_id = carro.id)
                detalle.save()
            messages.add_message(request, messages.SUCCESS, 'Servicios ingresados Exitosamente')
    else:
        formulario = CarroForm()
    return render(request, 'servicios/servicio_editar.html', {'formulario': formulario})
@login_required
def carro_edit(request, pk):
    carro = get_object_or_404(Carro, pk=pk)
    if request.method == "POST":
        formulario = CarroForm(request.POST, instance=carro)
        if formulario.is_valid():
            carro = formulario.save(commit=False)
            carro.save()

            for servicio_id in request.POST.getlist('servicios'):
                detalle = Detalle(servicio_id=servicio_id, carro_id = carro.id)
                detalle.save()
            return redirect('carro_detail', pk=carro.pk)
    else:
        formulario = CarroForm(instance=carro)
    return render(request, 'servicios/servicio_editar.html', {'formulario': formulario})
@login_required
def carro_remove(request, pk):
    carro = get_object_or_404(Carro, pk=pk)
    carro.delete()
    return redirect('list_carro')
    #aqui empieza clientes
def list_cliente(request):
    clientes=Cliente.objects.all()
    return render(request, 'clientes/list_cliente.html', {'clientes':clientes})
@login_required
def cliente_detail(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'clientes/cliente_detail.html', {'cliente': cliente})

def cliente_nuevo (request):
    if request.method == "POST":
        formulario1 = ClienteForm(request.POST)
        if formulario1.is_valid():
            cliente = Cliente.objects.create(cliente=formulario1.cleaned_data['cliente'],telefono=formulario1.cleaned_data['telefono'])
            cliente.save()
            return redirect('cliente_detail', pk=cliente.pk)
            messages.add_message(request, messages.SUCCESS, 'Cliente ingresados Exitosamente')
    else:
        formulario1 = ClienteForm()
    return render(request, 'clientes/cliente_editar.html', {'formulario1': formulario1})
@login_required
def cliente_editar(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        formulario1 = ClienteForm(request.POST, instance=cliente)
        if formulario1.is_valid():
            cliente = formulario1.save(commit=False)
            cliente.save()
            return redirect('cliente_detail', pk=cliente.pk)
    else:
        formulario1 = ClienteForm(instance=cliente)
    return render(request, 'clientes/cliente_editar.html', {'formulario1': formulario1})
@login_required
def cliente_remove(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return redirect('list_cliente')
#aqui empieza tipos de servicios
def list_tipo(request):
    tipos=Servicio.objects.all()
    return render(request, 'tipos/list_tipo.html', {'tipos':tipos})
@login_required
def tipo_detail(request, pk):
    tipo = get_object_or_404(Servicio, pk=pk)
    return render(request, 'tipos/tipo_detail.html', {'tipo': tipo})
@login_required
def tipo_nuevo (request):
    if request.method == "POST":
        formulario2 = ServicioForm(request.POST)
        if formulario2.is_valid():
            tipo = Servicio.objects.create(nombre=formulario2.cleaned_data['nombre'])
            tipo.save()
            return redirect('tipo_detail', pk=nombre.pk)
            messages.add_message(request, messages.SUCCESS, 'Servicio ingresado Exitosamente')
    else:
        formulario2 = ServicioForm()
    return render(request, 'tipos/tipo_editar.html', {'formulario2': formulario2})
@login_required
def tipo_editar(request, pk):
    tipo = get_object_or_404(Servicio, pk=pk)
    if request.method == "POST":
        formulario2 = ServicioForm(request.POST, instance=tipo)
        if formulario2.is_valid():
            tipo = formulario2.save(commit=False)
            tipo.save()
            return redirect('tipo_detail', pk=tipo.pk)
    else:
        formulario2 = ServicioForm(instance=tipo)
    return render(request, 'tipos/tipo_editar.html', {'formulario2': formulario2})
@login_required
def tipo_remove(request, pk):
    tipo = get_object_or_404(Servicio, pk=pk)
    tipo.delete()
    return redirect('list_tipo')
