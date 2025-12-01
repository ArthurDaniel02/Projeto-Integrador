from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=255) 
    email = models.EmailField(max_length=255)
    departamento = models.CharField(max_length=255)
    ativo = models.BooleanField()
    data_cadastro = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.nome 
 
class Aluno(models.Model):
    nome = models.CharField(max_length=255) 
    email = models.EmailField(max_length=255)
    matricula = models.CharField(max_length=10)
    curso = models.CharField(max_length=255) 
    data_nascimento = models.DateField()

    STATUS_CHOICES = (
            ('M', 'Masculino'),
            ('F', 'Feminino'),
            ('PN', 'Prefiro Não Informar'),
        ) 
    genero = models.CharField(choices=STATUS_CHOICES, max_length=2,default='M') 
    def __str__(self):
        return self.nome
 
class Turma(models.Model):
    nome = models.CharField(max_length=255) 
    descricao = models.CharField(max_length=255)
    STATUS_CHOICES = (
            ('Ativa', 'Turma Ativa'),
            ('Concluída', 'Turma Concluída'),
            ('Cancelada', 'Turma Cancelada'),
        ) 
    status = models.CharField(choices=STATUS_CHOICES, default='Ativa') 
    data_inicio = models.DateField()
    data_fim = models.DateField()
    professor    = models.ForeignKey(Professor, on_delete=models.CASCADE) 
    alunoRep = models.OneToOneField(Aluno,on_delete=models.CASCADE,unique= True)
    alunos = models.ManyToManyField(Aluno, through= 'Matricula')

    def __str__(self):
        return self.nome
 
class Matricula(models.Model):
   aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
   turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
   data_matricula = models.DateField()
   @property
   def total_presencas_presente(self):
       return self.presencas.filter(status='Presente').count()
   @property
   def porcentagem_presenca(self):
       total_aulas = self.turma.presencas_turma.count()
       if total_aulas == 0:
           return 0
       return round((self.total_presencas_presente / total_aulas) * 100, 1)
  
   def __str__(self):
       return f"{self.aluno.nome} - {self.turma.nome}"
   
class presenca(models.Model):
    matricula_id = models.ForeignKey(Matricula, on_delete=models.CASCADE, related_name='presencas') 
    STATUS_CHOICES = (
            ('Presente', 'Presente'),
            ('Ausente', 'Ausente'),
            ('Justificado', 'Presença Justificada'),
        ) 
    
    status = models.CharField(choices=STATUS_CHOICES, max_length=11, default='Ausente')
    data = models.DateField()
    class Meta:
        unique_together = ('matricula', 'data')

    def __str__(self):
        return f"{self.matricula.aluno.nome} - {self.data} - {self.status}"