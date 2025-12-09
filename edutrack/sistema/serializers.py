from rest_framework import serializers 
from .models import Aluno, Professor, Turma, Matricula, Presenca,AlunoRep, PresencaTurma

class AlunoSerializer(serializers.ModelSerializer):
 class Meta:
    model = Aluno
    fields = '__all__' 
class ProfessorSerializer(serializers.ModelSerializer):
 class Meta:
    model = Professor
    fields = '__all__' 
class AlunoRepSerializer(serializers.ModelSerializer):
 class Meta:
    model = AlunoRep
    fields = '__all__'    
class TurmaSerializer(serializers.ModelSerializer):
 class Meta:
    model = Turma
    fields = '__all__' 

class PresencaSerializer(serializers.ModelSerializer):
 class Meta:
    model = Presenca
    fields = '__all__' 
class PresencaTurmaSerializer(serializers.ModelSerializer):
 class Meta:
    model = PresencaTurma
    fields = '__all__' 

class MatriculaSerializer(serializers.ModelSerializer):
   total_presencas_presente = serializers.ReadOnlyField(source='total_presencas_presente')
   porcentagem_presenca = serializers.ReadOnlyField(source='porcentagem_presenca')
   presencas = PresencaSerializer(many=True, read_only=True)

   class Meta:
      model = Matricula
      fields = '__all__'

class AlunoDashboardSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(source='aluno.nome')
    matricula = serializers.CharField(source='aluno.matriculaA') 
    presencas = serializers.ReadOnlyField(source='total_presencas_presente') 
    porcentagem = serializers.ReadOnlyField(source='porcentagem_presenca')

    class Meta:
        model = Aluno
        fields = ['nome', 'matricula', 'presencas', 'porcentagem']


class TurmaDashboardSerializer(serializers.ModelSerializer):
    professor_nome = serializers.CharField(source='professor.nome')
    professor_email = serializers.CharField(source='professor.email')
    
    
    alunos_matriculados = AlunoDashboardSerializer(source='matricula_set', many=True, read_only=True)

    class Meta:
        model = Turma
        fields = [
            'id', 
            'nome', 
            'status', 
            'professor_nome', 
            'professor_email', 
            'alunoRep',
            'alunos_matriculados'
        ]

class AtribuirProfessorSerializer(serializers.Serializer):
    professor_id = serializers.PrimaryKeyRelatedField(
    queryset=Professor.objects.all()
)

class MatricularAlunoSerializer(serializers.Serializer):
    aluno_id = serializers.PrimaryKeyRelatedField(
    queryset=Aluno.objects.all()
)

class DefinirRepresentanteSerializer(serializers.Serializer):
    alunoRep = serializers.PrimaryKeyRelatedField(
    queryset=AlunoRep.objects.all()
)