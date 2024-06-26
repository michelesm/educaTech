from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .alunoForm import AlunoForm
from .models import Aluno


@method_decorator(login_required, name='dispatch')
class AlunoListView(ListView):
    model = Aluno
    template_name = 'aluno/aluno_list.html'
    context_object_name = 'object_list'
    ordering = ['nome_completo']


@method_decorator(login_required, name='dispatch')
class AlunoDetailView(DetailView):
    model = Aluno
    template_name = 'aluno/aluno_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aluno'] = self.get_object()
        return context


class AlunoCreateView(CreateView):
    model = Aluno
    fields = ('nome', 'cpf', 'email',)  # campos que você deseja incluir
    template_name = 'aluno/aluno_form.html'


@method_decorator(login_required, name='dispatch')
class AlunoDeleteView(DeleteView):
    model = Aluno
    template_name = 'aluno/aluno_confirm_delete.html'
    success_url = '/aluno/'  # redireciona para a lista de alunos após exclusão


@method_decorator(login_required, name='dispatch')
class AlunoEditView(View):
    def get(self, request, pk):
        aluno = Aluno.objects.get(pk=pk)
        form = AlunoForm(instance=aluno)
        return render(request, 'aluno/aluno_form.html', {'form': form})

    def post(self, request, pk):
        aluno = Aluno.objects.get(pk=pk)
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('aluno:aluno_list')  # Redireciona para a lista de alunos
        else:
            print(form.errors)  # Verifique os erros de validação
        return render(request, 'aluno/aluno_form.html', {'form': form})

'''
class AlunoUpdateView(UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'aluno/aluno_form.html'
    success_url = reverse_lazy('aluno:aluno_list')

    def get_object(self, queryset=None):
        return get_object_or_404(Aluno, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AlunoForm(instance=self.get_object())
        return context
'''