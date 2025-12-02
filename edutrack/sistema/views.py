from rest_framework import viewsets 
from .models import Aluno, Professor, Turma, Matricula, Presenca
from .serializers import AlunoSerializer, ProfessorSerializer, TurmaSerializer, MatriculaSerializer, PresencaSerializer
from django_filters.rest_framework import DjangoFilterBackend 

class AlunoViewSet(viewsets.ModelViewSet):
 queryset = Aluno.objects.all()
 serializer_class = AlunoSerializer 

 filter_backends = [DjangoFilterBackend] 
 filterset_fields = ['nome', 'matricula', 'curso', 'genero']

class ProfessorViewSet(viewsets.ModelViewSet):
 queryset = Professor.objects.all() 
 serializer_class = ProfessorSerializer 

 filter_backends = [DjangoFilterBackend] 
 filterset_fields = ['nome', 'departamento', 'ativo']

class TurmaViewSet(viewsets.ModelViewSet):
 queryset = Turma.objects.all()
 serializer_class = TurmaSerializer 

 filter_backends = [DjangoFilterBackend] 
 filterset_fields = ['nome', 'status', 'professor_id', 'alunoRep_id']

class MatriculaViewSet(viewsets.ModelViewSet):
 queryset = Matricula.objects.all()
 serializer_class = MatriculaSerializer 

 filter_backends = [DjangoFilterBackend] 
 filterset_fields = ['turma']

class PresencaViewSet(viewsets.ModelViewSet):
 queryset = Presenca.objects.all()
 serializer_class = PresencaSerializer 

 filter_backends = [DjangoFilterBackend] 
 filterset_fields = ['matricula_id_id', 'status']
