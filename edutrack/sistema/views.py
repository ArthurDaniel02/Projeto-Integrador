from rest_framework import viewsets 
from .models import Aluno, Professor, Turma, Matricula, Presenca,AlunoRep
from .serializers import AlunoSerializer, ProfessorSerializer, TurmaSerializer, MatriculaSerializer, PresencaSerializer,AlunoRepSerializer, TurmaDashboardSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class AlunoViewSet(viewsets.ModelViewSet):
 queryset = Aluno.objects.all()
 serializer_class = AlunoSerializer 

 filter_backends = [DjangoFilterBackend] 
 filterset_fields = ['nome', 'matriculaA', 'curso', 'genero']

class AlunoRepViewSet(viewsets.ModelViewSet):
 queryset = AlunoRep.objects.all()
 serializer_class = AlunoRepSerializer 
 
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

    @action(detail=True, methods=['put'], url_path='definir-representante')
    def definir_representante(self, request, pk=None):
        turma = self.get_object()
        aluno_rep_id = request.data.get("alunoRep")

        if not aluno_rep_id:
            return Response({"detail": "Envie o campo alunoRep"}, status=400)

        turma.alunoRep_id = aluno_rep_id
        turma.save()

        return Response({"detail": "Representante definido!", "alunoRep": aluno_rep_id}, status=200)
    
    @action(detail=True, methods=['get'], url_path='representante')
    def representante(self, request, pk=None):
        turma = self.get_object() 
        alunorep = getattr(turma, 'alunoRep', None)
        
        if not alunorep:
            return Response({'representante': None}, status=200) 
        
        return Response(AlunoRepSerializer(alunorep, context={'request': request}).data, status=200)
    
    @action(detail=True, methods=['get'])
    def dashboard(self, request, pk=None):
        turma = self.get_object()
        serializer = TurmaDashboardSerializer(turma)

        return Response(serializer.data)

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
