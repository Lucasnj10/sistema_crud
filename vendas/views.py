from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm
from .models import Venda
from .forms import VendaForm

# Listar clientes
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'vendas/cliente_list.html', {'clientes': clientes})

# Criar cliente
def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'vendas/cliente_form.html', {'form': form})

# Editar cliente
def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'vendas/cliente_form.html', {'form': form})

# Deletar cliente
def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'vendas/cliente_confirm_delete.html', {'cliente': cliente})

def venda_list(request):
    vendas = Venda.objects.all()
    return render(request, 'vendas/venda_list.html', {'vendas': vendas})

def venda_create(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('venda_list')
    else:
        form = VendaForm()
    return render(request, 'vendas/venda_form.html', {'form': form})

def venda_update(request, pk):
    venda = get_object_or_404(Venda, pk=pk)
    if request.method == 'POST':
        form = VendaForm(request.POST, instance=venda)
        if form.is_valid():
            form.save()
            return redirect('venda_list')
    else:
        form = VendaForm(instance=venda)
    return render(request, 'vendas/venda_form.html', {'form': form})

def venda_delete(request, pk):
    venda = get_object_or_404(Venda, pk=pk)
    if request.method == 'POST':
        venda.delete()
        return redirect('venda_list')
    return render(request, 'vendas/venda_confirm_delete.html', {'venda': venda})

def home_redirect(request):
    return redirect('cliente_list')

