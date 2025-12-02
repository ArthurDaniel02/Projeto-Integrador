from django.contrib import admin
from .models import Aluno, Professor, Turma, Presenca, Matricula
from rest_framework.authtoken.models import Token

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
 list_display = ['nome', 'email', 'matricula', 'curso','data_nascimento', 'genero']
 search_fields = ['nome', 'email', 'matricula', 'curso','data_nascimento']
 list_filter = ['curso', 'genero']

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
 list_display = ['nome', 'email', 'departamento', 'ativo','data_cadastro']
 search_fields = ['nome', 'email', 'departamento', 'ativo','data_cadastro']#teste ativo
 list_filter = ['departamento', 'ativo']


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
 list_display = ['nome', 'descricao', 'status', 'professor','alunoRep_nome','data_inicio','data_fim']#testar qualquer coisa tira descricao
 search_fields = ['nome', 'status', 'professor','alunoRep_nome','data_inicio','data_fim']
 list_filter = ['status', 'alunoRep_id']

@admin.register(Presenca)
class PresencaAdmin(admin.ModelAdmin):
 list_display = ['matricula_aluno_matricula','status','data'] 
 search_fields = ['matricula_aluno_matricula','status','data'] 
 list_filter = ['status'] 


@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
 list_display = ['aluno_nome','turma_nome','data_matricula'] 
 search_fields = ['aluno_nome','turma_nome','data_matricula'] 
 


admin.site.register(Token)