from django.contrib import admin 
from django.urls import path, include 
from rest_framework.routers import DefaultRouter 
from sistema.views import AlunoViewSet, ProfessorViewSet, TurmaViewSet, MatriculaViewSet, PresencaViewSet 
router = DefaultRouter()
router.register(r'alunos', AlunoViewSet) 
router.register(r'professores', ProfessorViewSet) 
router.register(r'turmas', TurmaViewSet) 
router.register(r'matriculas', MatriculaViewSet) 
router.register(r'presencas', PresencaViewSet) 

urlpatterns = [
 path('admin/', admin.site.urls), 
 path('api/', include(router.urls)), 
]
