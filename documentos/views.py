from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from.models import Documento
from.forms import DocumentoForm

@login_required
def documento_list(request):
    documentos = Documento.objects.all()
    return render(request, 'documento/documento_list.html', {'documentos': documentos})

@login_required
def documento_create(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('documento_list')
    else:
        form = DocumentoForm()
    return render(request, 'documento/documento_form.html', {'form': form})

@login_required
def documento_edit(request, pk):
    documento = Documento.objects.get(pk=pk)
    if request.method == 'POST':
        form = DocumentoForm(request.POST, instance=documento)
        if form.is_valid():
            form.save()
            return redirect('documento_list')
    else:
        form = DocumentoForm(instance=documento)
    return render(request, 'documento/documento_form.html', {'form': form})

@login_required
def documento_delete(request, pk):
    documento = Documento.objects.get(pk=pk)
    documento.delete()
    return redirect('documento_list')