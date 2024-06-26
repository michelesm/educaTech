from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from cursos.models import Turma
from .models import Matricula
from .forms import MatriculaForm


@login_required
def matricula_list(request):
    matriculas = Matricula.objects.all()
    return render(request, 'matricula/matricula_list.html', {'matriculas': matriculas})


@login_required
def matricula_create(request):
    if request.method == 'POST':
        form = MatriculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('matricula_list')
    else:
        form = MatriculaForm()
    return render(request, 'matricula/matricula_form.html', {'form': form})


@login_required
def matricula_edit(request, pk):
    matricula = Matricula.objects.get(pk=pk)
    if request.method == 'POST':
        form = MatriculaForm(request.POST, instance=matricula)
        if form.is_valid():
            form.save()
            return redirect('matricula_list')
    else:
        form = MatriculaForm(instance=matricula)
    return render(request, 'matricula/matricula_form.html', {'form': form})


@login_required
def matricula_delete(request, pk):
    matricula = Matricula.objects.get(pk=pk)
    matricula.delete()
    return redirect('matricula_list')


@login_required
def matricula_detail(request, pk):
    matricula = Matricula.objects.get(pk=pk)
    return render(request, 'matricula/matricula_detail.html', {'matricula': matricula})


def get_turmas(request):
    curso_id = request.GET.get('curso_id')
    turmas = Turma.objects.filter(curso_id=curso_id)
    data = [{'id': t.id, 'nome': t.nome} for t in turmas]
    return JsonResponse({'turmas': data})