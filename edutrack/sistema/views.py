from rest_framework import viewsets 
from .models import Aluno, Professor, Turma, Matricula, Presenca,AlunoRep, PresencaTurma
from .serializers import AlunoSerializer, ProfessorSerializer, TurmaSerializer, PresencaTurmaSerializer, MatriculaSerializer, PresencaSerializer,AlunoRepSerializer, TurmaDashboardSerializer, AtribuirProfessorSerializer, MatricularAlunoSerializer, DefinirRepresentanteSerializer
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

 @action(detail=True, methods=['get'])
 def turmas(self, request, pk=None):
     professor = self.get_object()
     turmas = Turma.objects.filter(professor=professor)
     serializer = TurmaSerializer(turmas, many=True)
     return Response(serializer.data)

class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer 

    filter_backends = [DjangoFilterBackend] 
    filterset_fields = ['nome', 'status', 'professor_id', 'alunoRep_id']

    @action(detail=True, methods=['put'], url_path='definir-representante', serializer_class=DefinirRepresentanteSerializer)
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
    
    @action(detail=True, methods=['post'], url_path='atribuir-professor', serializer_class=AtribuirProfessorSerializer)
    def atribuir_professor(self, request, pk=None):
        turma = self.get_object()
        professor_id = request.data.get("professor_id")

        if not professor_id:
            return Response({"erro": "Envie professor_id"}, status=400)

        try:
            professor = Professor.objects.get(id=professor_id)
        except Professor.DoesNotExist:
            return Response({"erro": "Professor inexistente"}, status=404)

        turma.professor = professor
        turma.save()

        return Response({"mensagem": "Professor atribuído com sucesso!"}, status=200)
    
    @action(detail=True, methods=['get'])
    def alunos(self, request, pk=None):
        turma = self.get_object()
        matriculas = Matricula.objects.filter(turma=turma)

        dados = []
        for m in matriculas:
            dados.append({
                "matricula_id": m.id,
                "data_matricula": m.data_matricula,
                "aluno": AlunoSerializer(m.aluno).data
            })

        return Response(dados)
    
    @action(detail=True, methods=['post'], url_path='matricular-aluno', serializer_class=MatricularAlunoSerializer)
    def matricular_aluno(self, request, pk=None):
        turma = self.get_object()
        aluno = Aluno.objects.filter(id=request.data.get("aluno_id")).first()

        if not aluno:
            return Response({"erro": "Aluno inexistente ou não enviado"}, status=400)

        matricula, criada = Matricula.objects.get_or_create(
            aluno=aluno,
            turma=turma
        )

        return Response({"mensagem": "Aluno matriculado com sucesso!"}, status=200)

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

class PresencaTurmaViewSet(viewsets.ModelViewSet):
    queryset = PresencaTurma.objects.all()
    serializer_class = PresencaTurmaSerializer 

    filter_backends = [DjangoFilterBackend] 
    filterset_fields = ['turma_id_id', 'status']