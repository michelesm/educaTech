from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Curso, Turma
from .forms import CursoForm


@method_decorator(login_required, name='dispatch')
class CursoListView(ListView):
    model = Curso
    template_name = 'cursos/cursos_list.html'
    queryset = Curso.objects.all()
    context_object_name = 'cursos'
    ordering = ['nome_curso']



def cursos_list(request):
    cursos = Curso.objects.all()
    selected_curso = None

    if request.method == 'POST' and 'curso_id' in request.POST:
        selected_curso_id = request.POST['curso_id']
        selected_curso = get_object_or_404(Curso, pk=selected_curso_id)

    return render(request, 'cursos/cursos_list.html', {
        'cursos': cursos,
        'selected_curso': selected_curso
    })


@method_decorator(login_required, name='dispatch')
class CursoCreateView(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'cursos/cursos_create.html'
    success_url = '/cursos/'


@method_decorator(login_required, name='dispatch')
class CursoDetailView(DetailView):
    model = Curso
    template_name = 'cursos/cursos_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aluno'] = self.get_object()
        return context


@method_decorator(login_required, name='dispatch')
class CursoUpdateView(LoginRequiredMixin, UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'cursos/cursos_update.html'
    success_url = '/cursos/'


@method_decorator(login_required, name='dispatch')
class CursoDeleteView(LoginRequiredMixin, DeleteView):
    model = Curso
    template_name = 'cursos/cursos_delete.html'
    success_url = '/cursos/'

@method_decorator(login_required, name='dispatch')
class TurmaListView(ListView):
    model = Turma
    template_name = 'cursos/turmas_list.html'
    context_object_name = 'turmas'

    def get_queryset(self):
        cursos = Curso.objects.all()
        turmas = []
        for curso in cursos:
            turmas_curso = Turma.objects.filter(curso=curso)
            turmas.append((curso, turmas_curso))
        return turmas


@method_decorator(login_required, name='dispatch')
class TurmaDetailView(DetailView):
    model = Turma
    template_name = 'cursos/turma_detail.html'
    context_object_name = 'turma'