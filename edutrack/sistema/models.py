from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=255) 
    email = models.EmailField(max_length=255)
    departamento = models.CharField(max_length=255)
    ativo = models.BooleanField()
    data_cadastro = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Professor"
        verbose_name_plural = "Professores"

    def __str__(self):
        return self.nome 
 
class Aluno(models.Model):
    nome = models.CharField(max_length=255) 
    email = models.EmailField(max_length=255)
    matriculaA = models.CharField("Matrícula", max_length=10)
    curso = models.CharField(max_length=255) 
    data_nascimento = models.DateField()

    STATUS_CHOICES = (
            ('M', 'Masculino'),
            ('F', 'Feminino'),
            ('PN', 'Prefiro Não Informar'),
        ) 
    genero = models.CharField("Gênero", choices=STATUS_CHOICES, max_length=2, default='M')
    def __str__(self):
        return self.nome
class AlunoRep(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE) 

    class Meta:
        unique_together = ('aluno',)
        verbose_name = "Aluno Representante"
        verbose_name_plural = "Alunos Representantes"

    def __str__(self):
        return self.aluno.nome 
    
class Turma(models.Model):
    nome = models.CharField(max_length=255) 
    descricao = models.CharField(max_length=255)
    STATUS_CHOICES = (
            ('Ativa', 'Turma Ativa'),
            ('Concluída', 'Turma Concluída'),
            ('Cancelada', 'Turma Cancelada'),
        ) 
    status = models.CharField(choices=STATUS_CHOICES, default='Ativa')
    data_inicio = models.DateField(auto_now_add=True)
    data_fim = models.DateField(null=True,blank=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE,limit_choices_to={'ativo': True}) 
    alunoRep = models.ForeignKey(AlunoRep,on_delete=models.SET_NULL,unique= True,null = True,blank=True)
    alunos = models.ManyToManyField(Aluno, through= 'Matricula')
    @property
    def presencas_turma(self):
       return self.presencas.filter(status='Presente').count()

    def __str__(self):
        return self.nome

class Matricula(models.Model):
   aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
   turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
   data_matricula = models.DateField(auto_now_add=True)
   @property
   def total_presencas_presente(self):
       return self.presencas.filter(status='Presente').count()
   @property
   def porcentagem_presenca(self):
       total_aulas = self.turma.presencasT.count()
       if total_aulas == 0:
           return 0
       return round((self.total_presencas_presente / total_aulas) * 100, 1)
   class Meta:
       unique_together = ('aluno', 'turma')
       verbose_name = "Matrícula"
       verbose_name_plural = "Matrículas"
  
   def __str__(self):
       return f"{self.aluno.nome} - {self.turma.nome}"
   
class Presenca(models.Model):
    matricula_id = models.ForeignKey(Matricula, on_delete=models.CASCADE, related_name='presencas') 
    STATUS_CHOICES = (
            ('Presente', 'Presente'),
            ('Ausente', 'Ausente'),
            ('Justificado', 'Presença Justificada'),
        ) 
    
    status = models.CharField(choices=STATUS_CHOICES, max_length=11, default='Ausente')
    data = models.DateField()
    class Meta:
        unique_together = ('matricula_id', 'data')
        verbose_name = "Presença"
        verbose_name_plural = "Presenças"

    def __str__(self):
        try:
            aluno_nome = self.matricula_id.aluno.nome
        except Exception:
            aluno_nome = str(self.matricula_id)
        return f"{aluno_nome} - {self.data} - {self.status}"
    
class PresencaTurma(models.Model):
    turma_id = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='presencasT') 
    status = models.BooleanField()
    data = models.DateField()
    class Meta:
        unique_together = ('turma_id', 'data')
        verbose_name = "PresençaTurma"
        verbose_name_plural = "PresençasTurma"

    def __str__(self):
        try:
            turma_nome = self.turma_id.turma.nome
        except Exception:
            turma_nome = str(self.turma_id)
        return f"{turma_nome} - {self.data} - {self.status}"
    