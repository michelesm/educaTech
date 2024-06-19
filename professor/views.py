from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from professor.ProfessorForm import ProfessorForm
from professor.models import Professor


# Create your views here.


class ProfessorListView(ListView):
    model = Professor
    template_name = 'professor/professor_list.html'
    context_object_name = 'professores'
    ordering = ['nome']


class ProfessorDetailView(DetailView):
    model = Professor
    template_name = 'professor/professor_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['professor'] = self.get_object()
        return context


class ProfessorCreateView(CreateView):
    model = Professor
    fields = ('nome', 'cpf', 'email',)  # campos que você deseja incluir
    template_name = 'professor/professor_form.html'


class ProfessorDeleteView(DeleteView):
    model = Professor
    template_name = 'professor/professor_confirm_delete.html'
    success_url = '/professor/'  # redireciona para a lista de alunos após exclusão


class ProfessorEditView(View):
    def get(self, request, pk):
        professor = Professor.objects.get(pk=pk)
        form = ProfessorForm(instance=professor)
        return render(request, 'professor/professor_form.html', {'form': form})

    def post(self, request, pk):
        aluno = Professor.objects.get(pk=pk)
        form = ProfessorForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('professor:professor_list')  # Redireciona para a lista de alunos
        else:
            print(form.errors)  # Verifique os erros de validação
        return render(request, 'aluno/aluno_form.html', {'form': form})
