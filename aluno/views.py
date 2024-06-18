from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Aluno

'''
def aluno_detail(request, pk):
    aluno = Aluno.objects.get(pk=pk)
    return render(request, 'aluno/aluno_detail.html', {'aluno': aluno})'''


class AlunoListView(ListView):
    model = Aluno
    template_name = 'aluno/aluno_list.html'
    context_object_name = 'object_list'
    ordering = ['nome_completo']

class AlunoDetailView(DetailView):
    model = Aluno
    template_name = 'aluno/aluno_detail.html'

class AlunoCreateView(CreateView):
    model = Aluno
    fields = ('nome', 'cpf', 'email',)  # campos que você deseja incluir
    template_name = 'aluno/aluno_form.html'

class AlunoUpdateView(UpdateView):
    model = Aluno
    fields = ('nome', 'cpf', 'email',)  # campos que você deseja incluir
    template_name = 'aluno/aluno_form.html'

class AlunoDeleteView(DeleteView):
    model = Aluno
    template_name = 'aluno/aluno_confirm_delete.html'
    success_url = '/aluno/'  # redireciona para a lista de alunos após exclusão